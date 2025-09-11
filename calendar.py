#!/home/agenda/env/bin/python
from icalendar import Calendar
from airbnb_agenda import get_checkin_agenda
from settings import LISTINGS_ICS

agenda = Calendar()

agenda['version'] = '2.0'
agenda['calscale'] = 'GREGORIAN'
agenda['method'] = 'PUBLISH'

for name, url in LISTINGS_ICS:
    get_agenda(agenda, url, name)

print(agenda.to_ical().decode("utf-8"))