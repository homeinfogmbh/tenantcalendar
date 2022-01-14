"""Common functions."""

from datetime import datetime
from typing import Optional

from peewee import ModelSelect

from comcatlib import User
from mdb import Company, Customer, Tenement

from tenantcalendar.orm import CustomerEvent, UserEvent


__all__ = [
    'list_customer_events',
    'get_customer_event',
    'list_user_events',
    'get_user_event',
    'list_own_events',
    'get_own_event'
]


def list_customer_events(
        customer: Customer, *,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None
) -> ModelSelect:
    """Lists user events."""

    condition = CustomerEvent.customer == customer

    if start is not None:
        condition &= CustomerEvent.start >= start

    if end is not None:
        condition &= CustomerEvent.end < end

    return CustomerEvent.select().join(Customer).join(Company).where(condition)


def get_customer_event(ident: int, customer: Customer) -> CustomerEvent:
    """Returns the given event of a customer."""

    return list_customer_events(customer).where(
        CustomerEvent.id == ident).get()


def list_user_events(
        customer: Customer, *,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None
) -> ModelSelect:
    """Lists user events."""

    condition = Tenement.customer == customer

    if start is not None:
        condition &= UserEvent.start >= start

    if end is not None:
        condition &= UserEvent.end < end

    return UserEvent.select().join(User).join(Tenement).where(condition)


def get_user_event(ident: int, customer: Customer) -> UserEvent:
    """Returns the given event of a customer."""

    return list_user_events(customer).where(UserEvent.id == ident).get()


def list_own_events(
        user: User, *,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None
) -> ModelSelect:
    """Lists user events."""

    condition = UserEvent.user == user

    if start is not None:
        condition &= UserEvent.start >= start

    if end is not None:
        condition &= UserEvent.end < end

    return UserEvent.select().join(User).join(Tenement).where(condition)


def get_own_event(ident: int, user: User) -> UserEvent:
    """Returns the given event of a particular user."""

    return list_own_events(user).where(UserEvent.id == ident).get()
