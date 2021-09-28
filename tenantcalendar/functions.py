"""Common functions."""

from datetime import datetime
from typing import Optional

from peewee import ModelSelect

from comcatlib import User
from mdb import Customer, Tenement

from tenantcalendar.orm import Event


__all__ = ['list_events', 'get_event']


def list_events(customer: Customer, *, start: Optional[datetime] = None,
                end: Optional[datetime] = None) -> ModelSelect:
    """Lists events of a customer."""

    condition = Tenement.customer == customer

    if start is not None:
        condition &= Event.start >= start

    if end is not None:
        condition &= Event.end < end

    return Event.select().join(User).join(Tenement).where(condition)


def get_event(ident: int, customer: Customer) -> Event:
    """Returns the given event of a customer."""

    return list_events(customer).where(Event.id == ident).get()
