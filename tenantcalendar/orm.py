"""Object-relational mappings."""

from __future__ import annotations
from datetime import datetime
from typing import Union

from peewee import DateTimeField, ForeignKeyField

from cmslib import Group
from comcatlib import User
from hwdb import Deployment
from mdb import Customer
from peeweeplus import EMailField
from peeweeplus import HTMLCharField
from peeweeplus import HTMLTextField
from peeweeplus import JSONModel
from peeweeplus import MySQLDatabaseProxy
from peeweeplus import PhoneNumberField

from tenantcalendar.exceptions import MissingContactInfo


__all__ = [
    "CUSTOMER_FIELDS",
    "USER_FIELDS",
    "CustomerEvent",
    "DeploymentCustomerEvent",
    "GroupCustomerEvent",
    "UserCustomerEvent",
    "UserEvent",
]


DATABASE = MySQLDatabaseProxy("tenantcalendar")
CUSTOMER_FIELDS = {"title", "start", "end", "text"}
USER_FIELDS = {"title", "email", "phone", "start", "end", "text"}


class TenantCalendarModel(JSONModel):
    """Base model for this database."""

    class Meta:
        database = DATABASE
        schema = database.database


class Event(TenantCalendarModel):
    """Common event base."""

    title = HTMLCharField(255)
    text = HTMLTextField()
    start = DateTimeField()
    end = DateTimeField()
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField(null=True)

    def patch_json(self, json: dict, **kwargs) -> Event:
        """Creates an event from a JSON-ish dict."""
        super().patch_json(json, **kwargs)
        self.modified = datetime.now()
        return self


class CustomerEvent(Event):
    """A customer-defined event."""

    class Meta:
        table_name = "customer_event"

    customer = ForeignKeyField(Customer, column_name="customer", on_delete="CASCADE")

    @classmethod
    def from_json(
        cls, json: dict, customer: Union[Customer, int], **kwargs
    ) -> CustomerEvent:
        """Creates an event from a JSON-ish dict."""
        event = super().from_json(json, **kwargs)
        event.customer = customer
        return event


class GroupCustomerEvent(TenantCalendarModel):
    """Mapping table for groups and customer events."""

    class Meta:
        table_name = "group_customer_event"

    group = ForeignKeyField(
        Group, column_name="group", backref="events", on_delete="CASCADE"
    )
    event = ForeignKeyField(
        CustomerEvent, column_name="event", backref="groups", on_delete="CASCADE"
    )


class UserCustomerEvent(TenantCalendarModel):
    """Mapping table for groups and customer events."""

    class Meta:
        table_name = "user_customer_event"

    user = ForeignKeyField(
        User, column_name="user", backref="events", on_delete="CASCADE"
    )
    event = ForeignKeyField(
        CustomerEvent, column_name="event", backref="groups", on_delete="CASCADE"
    )


class DeploymentCustomerEvent(TenantCalendarModel):
    """Mapping table for deployments and customer events."""

    class Meta:
        table_name = "deployment_customer_event"

    deployment = ForeignKeyField(
        Deployment, column_name="deployment", backref="events", on_delete="CASCADE"
    )
    event = ForeignKeyField(
        CustomerEvent, column_name="event", backref="groups", on_delete="CASCADE"
    )


class UserEvent(Event):
    """A user-defined event."""

    class Meta:
        table_name = "user_event"

    user = ForeignKeyField(User, column_name="user", on_delete="CASCADE")
    email = EMailField(64, null=True)
    phone = PhoneNumberField(64, null=True)

    @classmethod
    def from_json(cls, json: dict, user: Union[User, int], **kwargs) -> UserEvent:
        """Creates an event from a JSON-ish dict."""
        event = super().from_json(json, **kwargs)
        event.user = user
        return event

    def save(self, *args, **kwargs) -> int:
        """Saves the record."""
        if self.email or self.phone:
            return super().save(*args, **kwargs)

        raise MissingContactInfo("Must specify either email or phone.")
