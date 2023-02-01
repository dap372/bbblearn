import blackboard_calendar as bbcalendar
import main_gui
calendar = bbcalendar.download_calendar('https://learn.dcollege.net/webapps/calendar/calendarFeed/c2d84bf6673c402cb557f2a84ddabd87/learn.ics',True)
bbcalendar.write_as_csv('assignments.csv',calendar)
main_gui.start()