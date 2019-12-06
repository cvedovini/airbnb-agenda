from icalendar import Calendar, Event, Alarm
from datetime import datetime
from urllib2 import urlopen, Request


def get_checkin_agenda(url): 
    req = Request(url)
    req.add_header('User-agent', 'Mozilla 5.10')

    gcal = Calendar.from_ical(urlopen(req).read().decode('utf-8'))
    agenda = Calendar()

    agenda['prodid'] = gcal['prodid']
    agenda['version'] = '2.0'
    agenda['calscale'] = 'GREGORIAN'
    agenda['method'] = 'PUBLISH'

    for c in gcal.walk():
        if c.name == 'VEVENT' and 'description' in c:
            check_in = Event()
            check_in['summary'] = "CHECKIN - " + c['summary']
            check_in['description'] = c['description']
            check_in['location'] = c['location']
            check_in['dtstart'] = check_in['dtend'] = c['dtstart']
            check_in['uid'] = "checkin-" + c['uid']
            agenda.add_component(check_in)

    return agenda


def get_checkout_agenda(url): 
    req = Request(url)
    req.add_header('User-agent', 'Mozilla 5.10')

    gcal = Calendar.from_ical(urlopen(req).read().decode('utf-8'))
    agenda = Calendar()

    agenda['prodid'] = gcal['prodid']
    agenda['version'] = '2.0'
    agenda['calscale'] = 'GREGORIAN'
    agenda['method'] = 'PUBLISH'

    for c in gcal.walk():
        if c.name == "VEVENT" and 'location' in c:
            check_out = Event()
            check_out['summary'] = "CHECKOUT - " + c['summary']
            check_out['description'] = c['description']
            check_out['location'] = c['location']
            check_out['dtstart'] = check_out['dtend'] = c['dtend']
            check_out['uid'] = "checkout-" + c['uid']
            agenda.add_component(check_out)

    return agenda
