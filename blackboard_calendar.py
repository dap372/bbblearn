from tabulate import tabulate
import requests
import datetime
import csv
from ics import Calendar

# function to sort the event list by due date
def sort(event_list):
    return sorted(event_list, key=lambda x: x[1], reverse=False)

# function to parse the events into a table format
def parse_to_table(events):
    event_info = []
    for event in events:
        event_array = []
        event_array.append(event.name)
        # convert the due date to datetime object
        due_date = datetime.datetime.strptime(str(event.begin.datetime).split(':00-')[0], "%Y-%m-%d %H:%M")
        # If the due date of the assingment is before the current date, continue onto the next assignment
        if due_date < datetime.datetime.now():
            continue
        event_array.append(str(event.begin.datetime).split(':00-')[0])
        # Remove any existing html prefixes or suffixes that might exist
        description = str(event.description).removeprefix('<p>').removesuffix('</p>')
        # Check if there is no description, if so replace 'None' with blankspace
        if description == 'None':
            description = ''
        event_array.append(description)
        event_info.append(event_array)
    event_info = sort(event_info)
    event_info.insert(0,['Assignment Name','Due Date','Summary'])
    return event_info

# A function that given a .ics url downloads all events within the character
# 'as_table' refers to whether the data should be returned raw or parsed into a table
def download_calendar(url, as_table):
    # Download the calendar from the URL
    r = requests.get(url)
    # Parse the calendar into an ics.Calendar object
    calendar = Calendar(r.text)
    # Convert the calendar into an array
    events = [event for event in calendar.events]
    event_info = parse_to_table(events)
    return event_info if as_table else events

def write_as_csv(file_name,event_info):
    if '.csv' not in file_name:
        file_name += '.csv'
    writer = csv.writer(open(file_name,'w+'))
    for row in event_info:
        writer.writerow(row)

def organize_data(data):
    return tabulate(data,headers='firstrow',tablefmt='fancy_grid')

def test():
    event_info = download_calendar('https://learn.dcollege.net/webapps/calendar/calendarFeed/c2d84bf6673c402cb557f2a84ddabd87/learn.ics',True)
    write_as_csv('assignments.csv',event_info)
    # print the event_info in tabular format
    print(organize_data(event_info))
