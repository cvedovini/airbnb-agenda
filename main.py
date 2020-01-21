#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from airbnb_agenda import get_checkin_agenda, get_checkout_agenda

class MainHandler(webapp2.RequestHandler):
    def get(self):      
        if self.request.get('ics'):
            name = self.request.get('name') or ''

            if self.request.get('event') == 'checkout':
                agenda = get_checkout_agenda(self.request.get('ics'), name)
            else:
                agenda = get_checkin_agenda(self.request.get('ics'), name)

            self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'
            self.response.write(agenda.to_ical())
        else:
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.out.write('<html><body><form action="" method="get">')
            self.response.out.write('<p><input type="text" size="128" name="ics" placeholder="Source ICS url"></p>')
            self.response.out.write('<p><select name="event"><option value="checkin">Checkin</option><option value="checkout">Check-out</option></select></p>')
            self.response.out.write('<p><input type="text" size="128" name="name" placeholder="Name of your listing"></p>')
            self.response.out.write('<p><button type="submit">Submit</button></p>')
            self.response.out.write('</form></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
