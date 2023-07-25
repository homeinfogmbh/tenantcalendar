"""Tenant calendar for ComCat."""

from tenantcalendar.dom import events
from tenantcalendar.errors import ERRORS
from tenantcalendar.exceptions import MissingContactInfo
from tenantcalendar.fcm import notify
from tenantcalendar.functions import add_to_deployment
from tenantcalendar.functions import add_to_group
from tenantcalendar.functions import add_to_user
from tenantcalendar.functions import get_customer_event
from tenantcalendar.functions import get_deployment_customer_event
from tenantcalendar.functions import get_deployment_customer_events
from tenantcalendar.functions import get_events_for
from tenantcalendar.functions import get_group_customer_event
from tenantcalendar.functions import get_group_customer_events
from tenantcalendar.functions import get_own_event
from tenantcalendar.functions import get_user_customer_event
from tenantcalendar.functions import get_user_customer_events
from tenantcalendar.functions import get_user_event
from tenantcalendar.functions import list_customer_events
from tenantcalendar.functions import list_user_events
from tenantcalendar.functions import list_own_events
from tenantcalendar.orm import CustomerEvent
from tenantcalendar.orm import DeploymentCustomerEvent
from tenantcalendar.orm import GroupCustomerEvent
from tenantcalendar.orm import UserCustomerEvent
from tenantcalendar.orm import UserEvent


__all__ = [
    "ERRORS",
    "MissingContactInfo",
    "CustomerEvent",
    "DeploymentCustomerEvent",
    "GroupCustomerEvent",
    "UserCustomerEvent",
    "UserEvent",
    "add_to_deployment",
    "add_to_group",
    "add_to_user",
    "get_customer_event",
    "get_deployment_customer_event",
    "get_deployment_customer_events",
    "get_events_for",
    "get_group_customer_event",
    "get_group_customer_events",
    "get_own_event",
    "get_user_customer_event",
    "get_user_customer_events",
    "get_user_event",
    "list_customer_events",
    "list_user_events",
    "list_own_events",
    "notify",
]
