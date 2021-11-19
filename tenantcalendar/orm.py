"""Object-relational mappings."""

from __future__ import annotations
from datetime import datetime
from typing import Union

from peewee import DateTimeField, ForeignKeyField

from comcatlib import User
from mdb import Customer
from peeweeplus import HTMLCharField, JSONModel, MySQLDatabase

from tenantcalendar.config import CONFIG
from tenantcalendar.dom import Event as EventDOM
from tenantcalendar.exceptions import MissingContactInfo


__all__ = ['CUSTOMER_FIELDS', 'USER_FIELDS', 'CustomerEvent', 'UserEvent']


DATABASE = MySQLDatabase.from_config(CONFIG)
CUSTOMER_FIELDS = {'title', 'start', 'end', 'text'}
USER_FIELDS = {'title', 'email', 'phone', 'start', 'end', 'text'}


class TenantCalendarModel(JSONModel):   # pylint: disable=R0903
    """Base model for this database."""

    class Meta:     # pylint: disable=C0115,R0903
        database = DATABASE
        schema = database.database


class Event(TenantCalendarModel):   # pylint: disable=R0903
    """Common event base."""

    title = HTMLCharField(30)
    text = HTMLCharField(640)
    start = DateTimeField()
    end = DateTimeField()
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField(null=True)

    def to_dom(self) -> EventDOM:
        """Returns an XML DOM."""
        event = EventDOM()
        event.id = self.id
        event.title = self.title
        event.text = self.text
        event.start = self.start
        event.end = self.end
        event.created = self.created
        event.modified = self.modified
        return event


class CustomerEvent(Event):
    """A customer-defined event."""

    class Meta:     # pylint: disable=R0903,C0115
        table_name = 'customer_event'

    customer = ForeignKeyField(
        Customer, column_name='customer', on_delete='CASCADE')

    @classmethod
    def from_json(cls, json: dict, customer: Union[Customer, int],
                  **kwargs) -> CustomerEvent:
        """Creates an event from a JSON-ish dict."""
        event = super().from_json(json, **kwargs)
        event.customer = customer
        return event

    def patch_json(self, json: dict, **kwargs) -> CustomerEvent:
        """Creates an event from a JSON-ish dict."""
        event = super().patch_json(json, **kwargs)
        event.modified = datetime.now()
        return event


class UserEvent(Event):
    """A user-defined event."""

    class Meta:     # pylint: disable=R0903,C0115
        table_name = 'user_event'

    user = ForeignKeyField(User, column_name='user', on_delete='CASCADE')
    email = HTMLCharField(64, null=True)
    phone = HTMLCharField(64, null=True)

    @classmethod
    def from_json(cls, json: dict, user: Union[User, int],
                  **kwargs) -> UserEvent:
        """Creates an event from a JSON-ish dict."""
        event = super().from_json(json, **kwargs)
        event.user = user
        return event

    def patch_json(self, json: dict, **kwargs) -> UserEvent:
        """Creates an event from a JSON-ish dict."""
        event = super().patch_json(json, **kwargs)
        event.modified = datetime.now()
        return event

    def save(self, *args, **kwargs) -> int:
        """Saves the record."""
        if self.email or self.phone:
            return super().save(*args, **kwargs)

        raise MissingContactInfo('Must specify either email or phone.')
