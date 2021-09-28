"""Common functions."""

from peewee import ModelSelect

from comcatlib import User
from mdb import Customer, Tenement

from tenantcalendar.orm import Event


__all__ = ['list_events', 'get_event']


def list_events(customer: Customer) -> ModelSelect:
    """Lists events of a customer."""

    return Event.select().join(User).join(Tenement).where(
        Tenement.customer == customer)


def get_event(ident: int, customer: Customer) -> Event:
    """Returns the given event of a customer."""

    return list_events(customer).where(Event.id == ident).get()
