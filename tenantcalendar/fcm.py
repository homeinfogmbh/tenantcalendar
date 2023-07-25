"""Firebase Cloud Messaging API."""

from logging import getLogger
from typing import Iterator, Union

from firebase_admin.messaging import BatchResponse

from comcatlib import User
from comcatlib.fcm import APP_NAME
from comcatlib.fcm import CAPTIONS
from comcatlib.fcm import URLCode
from comcatlib.fcm import expand_groups
from comcatlib.fcm import get_tokens
from comcatlib.fcm import groups_users
from comcatlib.fcm import multicast_message

from tenantcalendar.orm import CustomerEvent
from tenantcalendar.orm import GroupCustomerEvent
from tenantcalendar.orm import UserCustomerEvent


__all__ = ["notify"]


def notify(customer_event: CustomerEvent) -> BatchResponse:
    """Multicast customer event to users."""

    getLogger("teantcalendar").info("Notifying customer event: %s", customer_event)
    return multicast_message(
        [token.token for token in get_tokens(set(affected_users(customer_event)))],
        url_code=URLCode.EVENTS,
        title=f"{APP_NAME}: {CAPTIONS[URLCode.EVENTS]}",
        body=customer_event.title,
    )


def affected_users(
    customer_event: Union[CustomerEvent, int]
) -> Iterator[Union[User, int]]:
    """Return a set of users affected by the
    change to the respective chart mapping.
    """

    for user_customer_event in UserCustomerEvent.select().where(
        UserCustomerEvent.event == customer_event
    ):
        yield user_customer_event.user

    yield from groups_users(
        expand_groups(
            {
                group_customer_event.group
                for group_customer_event in GroupCustomerEvent.select().where(
                    GroupCustomerEvent.event == customer_event
                )
            }
        )
    )
