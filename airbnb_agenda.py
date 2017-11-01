from icalendar import Calendar, Event, Alarm
from datetime import datetime
from urllib2 import urlopen, Request


def get_agenda(url): 
	req = Request(url)
	req.add_header('User-agent', 'Mozilla 5.10')

	gcal = Calendar.from_ical(urlopen(req).read().decode('utf-8'))
	agenda = Calendar()

	agenda['prodid'] = gcal['prodid']
	agenda['version'] = '2.0'

	alarm1 = Alarm()
	alarm1['action'] = 'EMAIL'
	alarm1['description'] = 'This is an event reminder'
	alarm1['summary'] = 'Alarm notification'
	alarm1['attendee'] = 'mailto:claude@vedovini.net'
	alarm1['trigger'] = '-P1DT0H0M0S'

	alarm2 = Alarm()
	alarm2['action'] = 'EMAIL'
	alarm2['description'] = 'This is an event reminder'
	alarm2['summary'] = 'Alarm notification'
	alarm2['attendee'] = 'mailto:claude@vedovini.net'
	alarm2['trigger'] = '-P5DT0H0M0S'

	for c in gcal.walk():
	    if c.name == "VEVENT" and 'location' in c:
			check_in = Event()
			check_in['summary'] = "IN - " + c['summary']
			check_in['description'] = c['description']
			check_in['location'] = c['location']
			check_in['dtstart'] = check_in['dtend'] = c['dtstart']
			check_in['uid'] = "checkin-" + c['uid']
			check_in.add_component(alarm1)
			check_in.add_component(alarm2)
			agenda.add_component(check_in)

			check_out = Event()
			check_out['summary'] = "OUT - " + c['summary']
			check_out['description'] = c['description']
			check_out['location'] = c['location']
			check_out['dtstart'] = check_out['dtend'] = c['dtend']
			check_out['uid'] = "checkout-" + c['uid']
			check_out.add_component(alarm1)
			agenda.add_component(check_out)

	return agenda
