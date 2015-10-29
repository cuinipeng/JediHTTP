#     Copyright 2015 Cedraro Andrea <a.cedraro@gmail.com>
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#    limitations under the License.

from jedihttp import handlers, hmaclib
from jedihttp.hmac_plugin import HmacPlugin
from webtest import TestApp
from nose.tools import ok_
from hamcrest import assert_that

def test_handle_without_params():
  secret = "secret"
  handle = '/ready'
  handlers.app.install( HmacPlugin( secret ) )
  app = TestApp( handlers.app )

  headers = {}
  hmachelper = hmaclib.JediHTTPHmacHelper( secret )
  hmachelper.SignRequestHeaders( headers,
                                 method = 'POST',
                                 path = handle,
                                 body = '' )

  response = app.post( handle, headers = headers )

  ok_( response )
  assert_that( hmachelper.IsResponseAuthenticated( response.headers,
                                                   response.body ) )
