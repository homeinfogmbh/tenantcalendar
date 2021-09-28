"""Object-relational mappings."""

from __future__ import annotations
from typing import Union

from peewee import DateTimeField, ForeignKeyField

from comcatlib import User
from peeweeplus import HTMLCharField, JSONModel, MySQLDatabase

from tenantcalendar.config import CONFIG
from tenantcalendar.exceptions import MissingContactInfo


__all__ = ['Event']


DATABASE = MySQLDatabase.from_config(CONFIG)


class TenantCalendarModel(JSONModel):   # pylint: disable=R0903
    """Base model for this database."""

    class Meta:     # pylint: disable=C0115,R0903
        database = DATABASE
        schema = database.database


class Event(TenantCalendarModel):
    """An event entry."""

    user = ForeignKeyField(User, column_name='user', on_delete='CASCADE')
    title = HTMLCharField(30)
    email = HTMLCharField(64, null=True)
    phone = HTMLCharField(64, null=True)
    start = DateTimeField()
    end = DateTimeField()
    text = HTMLCharField(640)

    @classmethod
    def from_json(cls, json: dict, user: Union[User, int], **kwargs) -> Event:
        """Creates an event from a JSON-ish dict."""
        event = super().from_json(json, **kwargs)
        event.user = user
        return event

    def save(self, *args, **kwargs) -> int:
        """Saves the record."""
        if self.email or self.phone:
            return super().save(*args, **kwargs)

        raise MissingContactInfo('Must specify either email or phone.')
