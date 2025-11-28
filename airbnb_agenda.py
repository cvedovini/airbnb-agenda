from icalendar import Calendar, Event, Alarm
from datetime import datetime
import requests


def get_description(e):
    start = e.start.strftime("%A, %b %d, %Y")
    end = e.end.strftime("%A, %b %d, %Y")
    nights = e.duration.days - 1

    return """Checkin: %s
Checkout: %s
Nights: %d

%s""" % (start, end, nights, e['description'])


def get_agenda(agenda, url, name): 
    headers = { 'User-agent': 'Mozilla 5.10', }
    res = requests.get(url, headers=headers)

    gcal = Calendar.from_ical(res.text)
    agenda['prodid'] = gcal['prodid']

    for c in gcal.walk():
        if c.name == 'VEVENT' and 'description' in c:
            check_in = Event()
            check_in['summary'] = name
            check_in['description'] = get_description(c)
            # check_in['location'] = c['location']
            check_in['dtstart'] = c['dtstart']
            check_in['dtend'] = c['dtend']
            check_in['uid'] = "checkin-" + c['uid']
            agenda.add_component(check_in)

    return agenda


def get_checkin_agenda(agenda, url, name): 
    headers = { 'User-agent': 'Mozilla 5.10', }
    res = requests.get(url, headers=headers)

    gcal = Calendar.from_ical(res.text)
    agenda['prodid'] = gcal['prodid']

    for c in gcal.walk():
        if c.name == 'VEVENT' and 'description' in c:
            check_in = Event()
            check_in['summary'] = "CHECKIN - " + name
            check_in['description'] = get_description(c)
            # check_in['location'] = c['location']
            check_in['dtstart'] = check_in['dtend'] = c['dtstart']
            check_in['uid'] = "checkin-" + c['uid']
            agenda.add_component(check_in)

    return agenda


def get_checkout_agenda(agenda, url, name): 
    headers = { 'User-agent': 'Mozilla 5.10', }
    res = requests.get(url, headers=headers)

    gcal = Calendar.from_ical(res.text)
    agenda['prodid'] = gcal['prodid']

    for c in gcal.walk():
        if c.name == "VEVENT" and 'description' in c:
            check_out = Event()
            check_out['summary'] = "CHECKOUT - " + name
            check_out['description'] = get_description(c)
            # check_out['location'] = c['location']
            check_out['dtstart'] = check_out['dtend'] = c['dtend']
            check_out['uid'] = "checkout-" + c['uid']
            agenda.add_component(check_out)

    return agenda
