import PySimpleGUI as sg
from datetime import datetime
import csv
from event_creator import event
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
events = [[],[],[],[],[],[],[]]
sorted_weeks = []
# Create a layout for the calendar
layout = [[sg.Text('Weekly Calendar')],
          [sg.Text('Monday', size=(10, 1)), sg.Listbox(values=[], enable_events=True, key='Monday', size=(20, 6)),
           sg.Text('Tuesday', size=(10, 1)), sg.Listbox(values=[], enable_events=True, key='Tuesday', size=(20, 6)),
           sg.Text('Wednesday', size=(10, 1)), sg.Listbox(values=[], enable_events=True, key='Wednesday', size=(20, 6)),
           sg.Text('Thursday', size=(10, 1)), sg.Listbox(values=[], enable_events=True, key='Thursday', size=(20, 6)),
           sg.Text('Friday', size=(10, 1)), sg.Listbox(values=[], enable_events=True, key='Friday', size=(20, 6)),
           sg.Text('Saturday', size=(10, 1)), sg.Listbox(values=[], enable_events=True, key='Saturday', size=(20, 6)),
           sg.Text('Sunday', size=(10, 1)), sg.Listbox(values=[], enable_events=True, key='Sunday', size=(20, 6))],
          [sg.Button('Add Event'), sg.Button('Cancel')]
        ]
window = sg.Window('Weekly Calendar', layout, finalize=True)
# Create the window

def add_existing_events_to_calendar(events):
    for i in range(7):
        window[days_of_week[i]].update(events[i])

def sort_by_weeks(events):
    sorted_weeks = [ [] for i in range(max(event.get_week_num() for event in events) + 1)]
    for event in events:
        sorted_weeks[event.get_week_num()].append(event)
    for week_of_events in sorted_weeks:
        for event in week_of_events:
            print(event.NAME)
        print('\n')

def read_existing_events():
    event_test = []
    with open('assignments.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row == ['Assignment Name','Due Date','Summary']:
                continue
            name, date, summary = row
            datetime_of_event = datetime.strptime(date,'%Y-%m-%d %H:%M')
            events[datetime_of_event.weekday()].append(name)
            event_test.append(event(name,datetime_of_event,summary))
    sort_by_weeks(event_test)
    add_existing_events_to_calendar(events)

def start():
    # Event loop to display the window
    has_run = False
    while True:
        if not has_run:
            read_existing_events()
            has_run = True
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event == 'Add Event':
            # Show a window to add an event
            event_layout = [[sg.Text('Event Name'), sg.Input()],
                            [sg.Text('Day'), sg.InputCombo(values=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])],
                            [sg.Text('Time of Event (HH:MM)'),sg.InputText('',size=(10,20)) ],
                            [sg.Button('Add'), sg.Button('Cancel')]]
            event_window = sg.Window('Add Event', event_layout)
            event_event, event_values = event_window.read()
            event_window.close()
            if event_event in (sg.WIN_CLOSED, 'Cancel'):
                continue
            # Add the event to the corresponding day
            #add_event_to_calendar(event_values[0],event_values[1])
            events[days_of_week.index(event_values[1])].append(event_values[0])
            add_existing_events_to_calendar(events)
    # Close the window
    window.close()
