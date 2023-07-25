"""Common errors."""

from wsgilib import JSONMessage

from tenantcalendar.exceptions import MissingContactInfo
from tenantcalendar.orm import CustomerEvent, UserEvent


__all__ = ["ERRORS"]


ERRORS = {
    CustomerEvent.DoesNotExist: lambda _: JSONMessage(
        "No such customer event.", status=404
    ),
    UserEvent.DoesNotExist: lambda _: JSONMessage("No such user event.", status=404),
    MissingContactInfo: lambda _: JSONMessage(
        "Must either specify email address or phone number.", status=400
    ),
}
