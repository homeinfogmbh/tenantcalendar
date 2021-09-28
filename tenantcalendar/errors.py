"""Common errors."""

from wsgilib import JSONMessage

from tenantforum.exceptions import MissingContactInfo
from tenantforum.orm import Event


__all__ = ['ERRORS']


ERRORS = {
    Event.DoesNotExist: lambda _: JSONMessage('No such event.', status=404),
    MissingContactInfo: lambda _: JSONMessage(
        'Must either specify email address or phone number.', status=400)
}
