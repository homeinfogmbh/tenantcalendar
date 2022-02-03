"""Common functions."""

from datetime import datetime
from typing import Iterable, Iterator, Optional, Union

from peewee import Expression, Select
from werkzeug.local import LocalProxy

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
    'get_events_for',
    'add_to_group',
    'remove_from_group',
    'add_to_user',
    'remove_from_user',
    'add_to_deployment',
    'remove_from_deployment',
    'get_deployment_customer_events',
    'get_group_customer_events',
    'get_user_customer_events'
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


def _get_events_for_groups(
        groups: Iterable[Group], *,
        condition: Union[bool, Expression] = True
) -> Select:
    """Select events for the given groups."""

    return CustomerEvent.select().join(GroupCustomerEvent).where(
        condition & (GroupCustomerEvent.group << set(groups))
    )


def get_events_for_group(
        group: Group, *,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None
) -> Iterator[CustomerEvent]:
    """Yield events for the given group."""

    condition = True

    if start is not None:
        condition &= CustomerEvent.start >= start

    if end is not None:
        condition &= CustomerEvent.end <= end

    yield from _get_events_for_groups(
        Groups.for_customer(group.customer).lineage(group),
        condition=condition
    )


def _get_events_for_user(
        user: User, *,
        condition: Union[bool, Expression] = True
) -> Select:
    """Select customer events for the given user."""

    return CustomerEvent.select().join(UserCustomerEvent).where(
        condition & (UserCustomerEvent.user == user)
    )


def get_events_for_user(
        user: User, *,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None
) -> Iterator[CustomerEvent]:
    """Yields events for the respective user."""

    condition = True

    if start is not None:
        condition &= CustomerEvent.start >= start

    if end is not None:
        condition &= CustomerEvent.end <= end

    yield from _get_events_for_user(user, condition=condition)
    yield from _get_events_for_groups(ggl_user(user), condition=condition)


def _get_events_for_deployment(
        deployment: Deployment, *,
        condition: Union[bool, Expression] = True
) -> Select:
    """Select customer events for the given deployment
    and all groups it is contained in.
    """

    return CustomerEvent.select().join(DeploymentCustomerEvent).where(
        condition & (DeploymentCustomerEvent.deployment == deployment)
    )


def get_events_for_deployment(
        deployment: Deployment, *,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None
) -> Iterator[CustomerEvent]:
    """Select customer events for the given deployment
    and all groups it is contained in.
    """

    condition = True

    if start is not None:
        condition &= CustomerEvent.start >= start

    if end is not None:
        condition &= CustomerEvent.end <= end

    yield from _get_events_for_deployment(deployment, condition=condition)
    yield from _get_events_for_groups(
        ggl_deployment(deployment), condition=condition
    )


def get_events_for(
        target: Union[Group, User, Deployment], *,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None
) -> Iterator[CustomerEvent]:
    """Selects events for the given target."""

    if isinstance(target, LocalProxy):
        return get_events_for(
            target._get_current_object(), start=start, end=end
        )

    if isinstance(target, Group):
        return get_events_for_group(target, start=start, end=end)

    if isinstance(target, User):
        return get_events_for_user(target, start=start, end=end)

    if isinstance(target, Deployment):
        return get_events_for_deployment(target, start=start, end=end)

    raise TypeError(f'Cannot select events for invalid type {type(target)}')


def add_to_group(event: CustomerEvent, group: Group) -> GroupCustomerEvent:
    """Add an event to a group."""

    try:
        return GroupCustomerEvent.get(
            (GroupCustomerEvent.event == event )
            & (GroupCustomerEvent.group == group)
        )
    except GroupCustomerEvent.DoesNotExist:
        gce = GroupCustomerEvent(event=event, group=group)
        gce.save()
        return gce


def remove_from_group(event: CustomerEvent, group: Group) -> bool:
    """Remove an event from a group."""

    try:
        gce = GroupCustomerEvent.get(
            (GroupCustomerEvent.event == event )
            & (GroupCustomerEvent.group == group)
        )
    except GroupCustomerEvent.DoesNotExist:
        return False

    gce.delete_instance()
    return True


def add_to_user(event: CustomerEvent, user: User) -> UserCustomerEvent:
    """Add an event to a user."""

    try:
        return UserCustomerEvent.get(
            (UserCustomerEvent.event == event)
            & (UserCustomerEvent.user == user)
        )
    except UserCustomerEvent.DoesNotExist:
        uce = UserCustomerEvent(event=event, user=user)
        uce.save()
        return uce


def remove_from_user(event: CustomerEvent, user: User) -> bool:
    """Remove an event from a user."""

    try:
        uce = UserCustomerEvent.get(
            (UserCustomerEvent.event == event)
            & (UserCustomerEvent.user == user)
        )
    except UserCustomerEvent.DoesNotExist:
        return False

    uce.delete_instance()
    return True


def add_to_deployment(
        event: CustomerEvent,
        deployment: Deployment
) -> DeploymentCustomerEvent:
    """Add an event to a deployment."""

    try:
        return DeploymentCustomerEvent.get(
            (DeploymentCustomerEvent.event == event)
            & (DeploymentCustomerEvent.deployment == deployment)
        )
    except DeploymentCustomerEvent.DoesNotExist:
        dce = DeploymentCustomerEvent(event=event, deployment=deployment)
        dce.save()
        return dce


def remove_from_deployment(
        event: CustomerEvent,
        deployment: Deployment
) -> bool:
    """Remove an event from a deployment."""

    try:
        dce = DeploymentCustomerEvent.get(
            (DeploymentCustomerEvent.event == event)
            (DeploymentCustomerEvent.deployment == deployment)
        )
    except DeploymentCustomerEvent.DoesNotExist:
        return False

    dce.delete_instance()
    return True


def get_deployment_customer_events(customer: Union[Customer, int]) -> Select:
    """Select deployment customer event mappings."""

    return DeploymentCustomerEvent.select().join(Deployment).where(
        Deployment.customer == customer
    )


def get_group_customer_events(customer: Union[Customer, int]) -> Select:
    """Select group customer event mappings."""

    return GroupCustomerEvent.select().join(Group).where(
        Group.customer == customer
    )


def get_user_customer_events(customer: Union[Customer, int]) -> Select:
    """Select user customer event mappings."""

    return UserCustomerEvent.select().join(User).join(Tenement).where(
        Tenement.customer == customer
    )
