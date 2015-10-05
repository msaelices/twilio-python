# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.http.response import Response


class SandboxTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2008-08-01",
                "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
                "date_updated": "Fri, 18 Feb 2011 17:37:18 +0000",
                "phone_number": "4155992671",
                "pin": "66528411",
                "sms_method": "POST",
                "sms_url": "http://demo.twilio.com/welcome/sms",
                "status_callback": null,
                "status_callback_method": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
                "voice_method": "POST",
                "voice_url": "http://www.digg.com"
            }
            '''
        ))
        
        self.twilio.api.v2010.accounts.get(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                             .sandbox.fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json'
        ))
