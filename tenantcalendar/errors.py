"""Common errors."""

from wsgilib import JSONMessage

from tenantcalendar.exceptions import MissingContactInfo
from tenantcalendar.orm import Event


__all__ = ['ERRORS']


ERRORS = {
    Event.DoesNotExist: lambda _: JSONMessage('No such event.', status=404),
    MissingContactInfo: lambda _: JSONMessage(
        'Must either specify email address or phone number.', status=400)
}
