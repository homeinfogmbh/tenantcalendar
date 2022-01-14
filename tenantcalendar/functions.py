"""Common functions."""

from datetime import datetime
from typing import Iterable, Iterator, Optional, Union

from peewee import Select

from cmslib import Group, Groups, get_groups_lineage as ggl_user
from comcatlib import User, get_groups_lineage as ggl_deployment
from hwdb import Deployment
from mdb import Company, Customer, Tenement

from tenantcalendar.orm import CustomerEvent
from tenantcalendar.orm import DeploymentCustomerEvent
from tenantcalendar.orm import GroupCustomerEvent
from tenantcalendar.orm import UserCustomerEvent
from tenantcalendar.orm import UserEvent


__all__ = [
    'list_customer_events',
    'get_customer_event',
    'list_user_events',
    'get_user_event',
    'list_own_events',
    'get_own_event',
    'get_events_for'
]


def list_customer_events(
        customer: Customer, *,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None
) -> Select:
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
) -> Select:
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
) -> Select:
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


def _get_events_for_groups(groups: Iterable[Group]) -> Select:
    """Select events for the given groups."""

    return CustomerEvent.select().join(GroupCustomerEvent).where(
        GroupCustomerEvent.group << set(groups)
    )


def get_events_for_group(group: Group) -> Iterator[CustomerEvent]:
    """Yield events for the given group."""

    yield from _get_events_for_groups(
        Groups.for_customer(group.customer).lineage(group)
    )


def _get_events_for_user(user: User) -> Select:
    """Select customer events for the given user."""

    return CustomerEvent.select().join(UserCustomerEvent).where(
        UserCustomerEvent.user == user
    )


def get_events_for_user(user: User) -> Iterator[CustomerEvent]:
    """Yields events for the respective user."""

    yield from _get_events_for_user(user)
    yield from _get_events_for_groups(ggl_user(user))


def _get_events_for_deployment(deployment: Deployment) -> Select:
    """Select customer events for the given deployment
    and all groups it is contained in.
    """

    return CustomerEvent.select().join(DeploymentCustomerEvent).where(
        DeploymentCustomerEvent.deployment == deployment
    )


def get_events_for_deployment(
        deployment: Deployment
) -> Iterator[CustomerEvent]:
    """Select customer events for the given deployment
    and all groups it is contained in.
    """

    yield from _get_events_for_deployment(deployment)
    yield from _get_events_for_groups(ggl_deployment(deployment))


def get_events_for(
        target: Union[Group, User, Deployment]
) -> Iterator[CustomerEvent]:
    """Selects events for the given target."""

    if isinstance(target, Group):
        return get_events_for_group(target)

    if isinstance(target, User):
        return get_events_for_user(target)

    if isinstance(target, Deployment):
        return get_events_for_deployment(target)

    raise TypeError(f'Cannot select events for invalid type {type(target)}')
