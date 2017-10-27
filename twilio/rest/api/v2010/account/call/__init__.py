# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.api.v2010.account.call.feedback import FeedbackList
from twilio.rest.api.v2010.account.call.feedback_summary import FeedbackSummaryList
from twilio.rest.api.v2010.account.call.notification import NotificationList
from twilio.rest.api.v2010.account.call.recording import RecordingList


class CallList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the CallList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the Account responsible for creating this Call

        :returns: twilio.rest.api.v2010.account.call.CallList
        :rtype: twilio.rest.api.v2010.account.call.CallList
        """
        super(CallList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid,}
        self._uri = '/Accounts/{account_sid}/Calls.json'.format(**self._solution)

        # Components
        self._feedback_summaries = None

    def create(self, to, from_, method=values.unset, fallback_url=values.unset,
               fallback_method=values.unset, status_callback=values.unset,
               status_callback_event=values.unset,
               status_callback_method=values.unset, send_digits=values.unset,
               if_machine=values.unset, timeout=values.unset, record=values.unset,
               recording_channels=values.unset,
               recording_status_callback=values.unset,
               recording_status_callback_method=values.unset,
               sip_auth_username=values.unset, sip_auth_password=values.unset,
               machine_detection=values.unset,
               machine_detection_timeout=values.unset, url=values.unset,
               application_sid=values.unset):
        """
        Create a new CallInstance

        :param unicode to: Phone number, SIP address or client identifier to call
        :param unicode from_: Twilio number from which to originate the call
        :param unicode method: HTTP method to use to fetch TwiML
        :param unicode fallback_url: Fallback URL in case of error
        :param unicode fallback_method: HTTP Method to use with FallbackUrl
        :param unicode status_callback: Status Callback URL
        :param unicode status_callback_event: The status_callback_event
        :param unicode status_callback_method: HTTP Method to use with StatusCallback
        :param unicode send_digits: Digits to send
        :param unicode if_machine: Action to take if a machine has answered the call
        :param unicode timeout: Number of seconds to wait for an answer
        :param bool record: Whether or not to record the Call
        :param unicode recording_channels: The recording_channels
        :param unicode recording_status_callback: The recording_status_callback
        :param unicode recording_status_callback_method: The recording_status_callback_method
        :param unicode sip_auth_username: The sip_auth_username
        :param unicode sip_auth_password: The sip_auth_password
        :param unicode machine_detection: Enable machine detection or end of greeting detection
        :param unicode machine_detection_timeout: Number of miliseconds to wait for machine detection
        :param unicode url: Url from which to fetch TwiML
        :param unicode application_sid: ApplicationSid that configures from where to fetch TwiML

        :returns: Newly created CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallInstance
        """
        data = values.of({
            'To': to,
            'From': from_,
            'Url': url,
            'ApplicationSid': application_sid,
            'Method': method,
            'FallbackUrl': fallback_url,
            'FallbackMethod': fallback_method,
            'StatusCallback': status_callback,
            'StatusCallbackEvent': status_callback_event,
            'StatusCallbackMethod': status_callback_method,
            'SendDigits': send_digits,
            'IfMachine': if_machine,
            'Timeout': timeout,
            'Record': record,
            'RecordingChannels': recording_channels,
            'RecordingStatusCallback': recording_status_callback,
            'RecordingStatusCallbackMethod': recording_status_callback_method,
            'SipAuthUsername': sip_auth_username,
            'SipAuthPassword': sip_auth_password,
            'MachineDetection': machine_detection,
            'MachineDetectionTimeout': machine_detection_timeout,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return CallInstance(self._version, payload, account_sid=self._solution['account_sid'],)

    def stream(self, to=values.unset, from_=values.unset,
               parent_call_sid=values.unset, status=values.unset,
               start_time_before=values.unset, start_time=values.unset,
               start_time_after=values.unset, end_time_before=values.unset,
               end_time=values.unset, end_time_after=values.unset, limit=None,
               page_size=None):
        """
        Streams CallInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode to: Phone number or Client identifier to filter `to` on
        :param unicode from_: Phone number or Client identifier to filter `from` on
        :param unicode parent_call_sid: Parent Call Sid to filter on
        :param CallInstance.Status status: Status to filter on
        :param datetime start_time_before: StartTime to filter on
        :param datetime start_time: StartTime to filter on
        :param datetime start_time_after: StartTime to filter on
        :param datetime end_time_before: EndTime to filter on
        :param datetime end_time: EndTime to filter on
        :param datetime end_time_after: EndTime to filter on
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.CallInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            to=to,
            from_=from_,
            parent_call_sid=parent_call_sid,
            status=status,
            start_time_before=start_time_before,
            start_time=start_time,
            start_time_after=start_time_after,
            end_time_before=end_time_before,
            end_time=end_time,
            end_time_after=end_time_after,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, to=values.unset, from_=values.unset,
             parent_call_sid=values.unset, status=values.unset,
             start_time_before=values.unset, start_time=values.unset,
             start_time_after=values.unset, end_time_before=values.unset,
             end_time=values.unset, end_time_after=values.unset, limit=None,
             page_size=None):
        """
        Lists CallInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode to: Phone number or Client identifier to filter `to` on
        :param unicode from_: Phone number or Client identifier to filter `from` on
        :param unicode parent_call_sid: Parent Call Sid to filter on
        :param CallInstance.Status status: Status to filter on
        :param datetime start_time_before: StartTime to filter on
        :param datetime start_time: StartTime to filter on
        :param datetime start_time_after: StartTime to filter on
        :param datetime end_time_before: EndTime to filter on
        :param datetime end_time: EndTime to filter on
        :param datetime end_time_after: EndTime to filter on
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.CallInstance]
        """
        return list(self.stream(
            to=to,
            from_=from_,
            parent_call_sid=parent_call_sid,
            status=status,
            start_time_before=start_time_before,
            start_time=start_time,
            start_time_after=start_time_after,
            end_time_before=end_time_before,
            end_time=end_time,
            end_time_after=end_time_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, to=values.unset, from_=values.unset,
             parent_call_sid=values.unset, status=values.unset,
             start_time_before=values.unset, start_time=values.unset,
             start_time_after=values.unset, end_time_before=values.unset,
             end_time=values.unset, end_time_after=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CallInstance records from the API.
        Request is executed immediately

        :param unicode to: Phone number or Client identifier to filter `to` on
        :param unicode from_: Phone number or Client identifier to filter `from` on
        :param unicode parent_call_sid: Parent Call Sid to filter on
        :param CallInstance.Status status: Status to filter on
        :param datetime start_time_before: StartTime to filter on
        :param datetime start_time: StartTime to filter on
        :param datetime start_time_after: StartTime to filter on
        :param datetime end_time_before: EndTime to filter on
        :param datetime end_time: EndTime to filter on
        :param datetime end_time_after: EndTime to filter on
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallPage
        """
        params = values.of({
            'To': to,
            'From': from_,
            'ParentCallSid': parent_call_sid,
            'Status': status,
            'StartTime<': serialize.iso8601_datetime(start_time_before),
            'StartTime': serialize.iso8601_datetime(start_time),
            'StartTime>': serialize.iso8601_datetime(start_time_after),
            'EndTime<': serialize.iso8601_datetime(end_time_before),
            'EndTime': serialize.iso8601_datetime(end_time),
            'EndTime>': serialize.iso8601_datetime(end_time_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return CallPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CallInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CallPage(self._version, response, self._solution)

    @property
    def feedback_summaries(self):
        """
        Access the feedback_summaries

        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryList
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryList
        """
        if self._feedback_summaries is None:
            self._feedback_summaries = FeedbackSummaryList(
                self._version,
                account_sid=self._solution['account_sid'],
            )
        return self._feedback_summaries

    def get(self, sid):
        """
        Constructs a CallContext

        :param sid: Call Sid that uniquely identifies the Call to fetch

        :returns: twilio.rest.api.v2010.account.call.CallContext
        :rtype: twilio.rest.api.v2010.account.call.CallContext
        """
        return CallContext(self._version, account_sid=self._solution['account_sid'], sid=sid,)

    def __call__(self, sid):
        """
        Constructs a CallContext

        :param sid: Call Sid that uniquely identifies the Call to fetch

        :returns: twilio.rest.api.v2010.account.call.CallContext
        :rtype: twilio.rest.api.v2010.account.call.CallContext
        """
        return CallContext(self._version, account_sid=self._solution['account_sid'], sid=sid,)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CallList>'


class CallPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the CallPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique id of the Account responsible for creating this Call

        :returns: twilio.rest.api.v2010.account.call.CallPage
        :rtype: twilio.rest.api.v2010.account.call.CallPage
        """
        super(CallPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CallInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.call.CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallInstance
        """
        return CallInstance(self._version, payload, account_sid=self._solution['account_sid'],)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CallPage>'


class CallContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, sid):
        """
        Initialize the CallContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param sid: Call Sid that uniquely identifies the Call to fetch

        :returns: twilio.rest.api.v2010.account.call.CallContext
        :rtype: twilio.rest.api.v2010.account.call.CallContext
        """
        super(CallContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'sid': sid,}
        self._uri = '/Accounts/{account_sid}/Calls/{sid}.json'.format(**self._solution)

        # Dependents
        self._recordings = None
        self._notifications = None
        self._feedback = None

    def delete(self):
        """
        Deletes the CallInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def fetch(self):
        """
        Fetch a CallInstance

        :returns: Fetched CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CallInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def update(self, url=values.unset, method=values.unset, status=values.unset,
               fallback_url=values.unset, fallback_method=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Update the CallInstance

        :param unicode url: URL that returns TwiML
        :param unicode method: HTTP method to use to fetch TwiML
        :param CallInstance.UpdateStatus status: Status to update the Call with
        :param unicode fallback_url: Fallback URL in case of error
        :param unicode fallback_method: HTTP Method to use with FallbackUrl
        :param unicode status_callback: Status Callback URL
        :param unicode status_callback_method: HTTP Method to use with StatusCallback

        :returns: Updated CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallInstance
        """
        data = values.of({
            'Url': url,
            'Method': method,
            'Status': status,
            'FallbackUrl': fallback_url,
            'FallbackMethod': fallback_method,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return CallInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    @property
    def recordings(self):
        """
        Access the recordings

        :returns: twilio.rest.api.v2010.account.call.recording.RecordingList
        :rtype: twilio.rest.api.v2010.account.call.recording.RecordingList
        """
        if self._recordings is None:
            self._recordings = RecordingList(
                self._version,
                account_sid=self._solution['account_sid'],
                call_sid=self._solution['sid'],
            )
        return self._recordings

    @property
    def notifications(self):
        """
        Access the notifications

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationList
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationList
        """
        if self._notifications is None:
            self._notifications = NotificationList(
                self._version,
                account_sid=self._solution['account_sid'],
                call_sid=self._solution['sid'],
            )
        return self._notifications

    @property
    def feedback(self):
        """
        Access the feedback

        :returns: twilio.rest.api.v2010.account.call.feedback.FeedbackList
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackList
        """
        if self._feedback is None:
            self._feedback = FeedbackList(
                self._version,
                account_sid=self._solution['account_sid'],
                call_sid=self._solution['sid'],
            )
        return self._feedback

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CallContext {}>'.format(context)


class CallInstance(InstanceResource):
    """  """

    class Event(object):
        INITIATED = "initiated"
        RINGING = "ringing"
        ANSWERED = "answered"
        COMPLETED = "completed"

    class Status(object):
        QUEUED = "queued"
        RINGING = "ringing"
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        BUSY = "busy"
        FAILED = "failed"
        NO_ANSWER = "no-answer"
        CANCELED = "canceled"

    class UpdateStatus(object):
        CANCELED = "canceled"
        COMPLETED = "completed"

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the CallInstance

        :returns: twilio.rest.api.v2010.account.call.CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallInstance
        """
        super(CallInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'annotation': payload['annotation'],
            'answered_by': payload['answered_by'],
            'api_version': payload['api_version'],
            'caller_name': payload['caller_name'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'direction': payload['direction'],
            'duration': payload['duration'],
            'end_time': deserialize.rfc2822_datetime(payload['end_time']),
            'forwarded_from': payload['forwarded_from'],
            'from_': payload['from'],
            'from_formatted': payload['from_formatted'],
            'group_sid': payload['group_sid'],
            'parent_call_sid': payload['parent_call_sid'],
            'phone_number_sid': payload['phone_number_sid'],
            'price': deserialize.decimal(payload['price']),
            'price_unit': payload['price_unit'],
            'sid': payload['sid'],
            'start_time': deserialize.rfc2822_datetime(payload['start_time']),
            'status': payload['status'],
            'subresource_uris': payload['subresource_uris'],
            'to': payload['to'],
            'to_formatted': payload['to_formatted'],
            'uri': payload['uri'],
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'sid': sid or self._properties['sid'],}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CallContext for this CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallContext
        """
        if self._context is None:
            self._context = CallContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique id of the Account responsible for creating this Call
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def annotation(self):
        """
        :returns: The annotation provided for the Call
        :rtype: unicode
        """
        return self._properties['annotation']

    @property
    def answered_by(self):
        """
        :returns: If this call was initiated with answering machine detection, either `human` or `machine`. Empty otherwise.
        :rtype: unicode
        """
        return self._properties['answered_by']

    @property
    def api_version(self):
        """
        :returns: The API Version the Call was created through
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def caller_name(self):
        """
        :returns: If this call was an incoming call to a phone number with Caller ID Lookup enabled, the caller's name. Empty otherwise.
        :rtype: unicode
        """
        return self._properties['caller_name']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def direction(self):
        """
        :returns: A string describing the direction of the call. `inbound` for inbound calls, `outbound-api` for calls initiated via the REST API or `outbound-dial` for calls initiated by a `Dial` verb.
        :rtype: unicode
        """
        return self._properties['direction']

    @property
    def duration(self):
        """
        :returns: The duration
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def end_time(self):
        """
        :returns: The end time of the Call. Null if the call did not complete successfully.
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def forwarded_from(self):
        """
        :returns: If this Call was an incoming call forwarded from another number, the forwarding phone number (depends on carrier supporting forwarding). Empty otherwise.
        :rtype: unicode
        """
        return self._properties['forwarded_from']

    @property
    def from_(self):
        """
        :returns: The phone number, SIP address or Client identifier that made this Call. Phone numbers are in E.164 format (e.g. +16175551212). SIP addresses are formatted as `name@company.com`. Client identifiers are formatted `client:name`.
        :rtype: unicode
        """
        return self._properties['from_']

    @property
    def from_formatted(self):
        """
        :returns: The phone number, SIP address or Client identifier that made this Call. Formatted for display.
        :rtype: unicode
        """
        return self._properties['from_formatted']

    @property
    def group_sid(self):
        """
        :returns: A 34 character Group Sid associated with this Call. Empty if no Group is associated with the Call.
        :rtype: unicode
        """
        return self._properties['group_sid']

    @property
    def parent_call_sid(self):
        """
        :returns: A 34 character string that uniquely identifies the Call that created this leg.
        :rtype: unicode
        """
        return self._properties['parent_call_sid']

    @property
    def phone_number_sid(self):
        """
        :returns: If the call was inbound, this is the Sid of the IncomingPhoneNumber that received the call. If the call was outbound, it is the Sid of the OutgoingCallerId from which the call was placed.
        :rtype: unicode
        """
        return self._properties['phone_number_sid']

    @property
    def price(self):
        """
        :returns: The charge for this call, in the currency associated with the account. Populated after the call is completed. May not be immediately available.
        :rtype: unicode
        """
        return self._properties['price']

    @property
    def price_unit(self):
        """
        :returns: The currency in which `Price` is measured.
        :rtype: unicode
        """
        return self._properties['price_unit']

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def start_time(self):
        """
        :returns: The start time of the Call. Null if the call has not yet been dialed.
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def status(self):
        """
        :returns: The status
        :rtype: CallInstance.Status
        """
        return self._properties['status']

    @property
    def subresource_uris(self):
        """
        :returns: Call Instance Subresources
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    @property
    def to(self):
        """
        :returns: The phone number, SIP address or Client identifier that received this Call. Phone numbers are in E.164 format (e.g. +16175551212). SIP addresses are formatted as `name@company.com`. Client identifiers are formatted `client:name`.
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def to_formatted(self):
        """
        :returns: The phone number, SIP address or Client identifier that received this Call. Formatted for display.
        :rtype: unicode
        """
        return self._properties['to_formatted']

    @property
    def uri(self):
        """
        :returns: The URI for this resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    def delete(self):
        """
        Deletes the CallInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch a CallInstance

        :returns: Fetched CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallInstance
        """
        return self._proxy.fetch()

    def update(self, url=values.unset, method=values.unset, status=values.unset,
               fallback_url=values.unset, fallback_method=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Update the CallInstance

        :param unicode url: URL that returns TwiML
        :param unicode method: HTTP method to use to fetch TwiML
        :param CallInstance.UpdateStatus status: Status to update the Call with
        :param unicode fallback_url: Fallback URL in case of error
        :param unicode fallback_method: HTTP Method to use with FallbackUrl
        :param unicode status_callback: Status Callback URL
        :param unicode status_callback_method: HTTP Method to use with StatusCallback

        :returns: Updated CallInstance
        :rtype: twilio.rest.api.v2010.account.call.CallInstance
        """
        return self._proxy.update(
            url=url,
            method=method,
            status=status,
            fallback_url=fallback_url,
            fallback_method=fallback_method,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
        )

    @property
    def recordings(self):
        """
        Access the recordings

        :returns: twilio.rest.api.v2010.account.call.recording.RecordingList
        :rtype: twilio.rest.api.v2010.account.call.recording.RecordingList
        """
        return self._proxy.recordings

    @property
    def notifications(self):
        """
        Access the notifications

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationList
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationList
        """
        return self._proxy.notifications

    @property
    def feedback(self):
        """
        Access the feedback

        :returns: twilio.rest.api.v2010.account.call.feedback.FeedbackList
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackList
        """
        return self._proxy.feedback

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CallInstance {}>'.format(context)
