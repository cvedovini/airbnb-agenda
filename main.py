from airbnb_agenda import get_checkin_agenda, get_checkout_agenda

def application (environ, start_response):

    # Sorting and stringifying the environment key, value pairs
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]

"""
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
"""
