import PySimpleGUI as sg      
import csv
layout = [[sg.Text('My one-shot window.')],      
                 [sg.Text('Calendar Name'),sg.InputText()],
                 [sg.Text('Calendar URL '),sg.InputText()],
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()

calendar_name = values[0]
url = values[1]
print(f'{calendar_name=}\n{url=}')

def add_url_to_csv(line):
    # Check if line already exists in CSV
    with open('calendars.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row == line:
                print("Line already exists in CSV.")
                sg.popup('This calendar has already been added')
                return

    # If line does not exist, add it to CSV
    with open('calendars.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(line)
        print("Line added to CSV.")
        sg.popup('This calendar has been added')

add_url_to_csv([calendar_name, url])