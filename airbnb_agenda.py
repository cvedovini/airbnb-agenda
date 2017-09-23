from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
from urllib2 import urlopen, Request

url = "https://www.airbnb.com/calendar/ical/11094613.ics?s=fd5bd3c7667036b0cba9298d60c488b0"

req = Request(url)
req.add_header('User-agent', 'Mozilla 5.10')

gcal = Calendar.from_ical(urlopen(req).read().decode('utf-8'))
agenda = Calendar()

agenda['prodid'] = gcal['prodid']
agenda['version'] = '2.0'

for c in gcal.walk():
    if c.name == "VEVENT" and 'location' in c:
		check_in = Event()
		check_in['summary'] = c['summary']
		check_in['description'] = "CHECKIN"
		check_in['location'] = c['location']
		check_in['dtstart'] = check_in['dtend'] = c['dtstart']
		check_in['uid'] = "checkin-" + c['uid']
		agenda.add_component(check_in)

		check_out = Event()
		check_out['summary'] = c['summary']
		check_out['description'] = "CHECKOUT"
		check_out['location'] = c['location']
		check_out['dtstart'] = check_out['dtend'] = c['dtend']
		check_out['uid'] = "checkout-" + c['uid']
		agenda.add_component(check_out)

print agenda.to_ical()
