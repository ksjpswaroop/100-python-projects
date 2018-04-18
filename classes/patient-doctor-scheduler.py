'''
Patient / Doctor Scheduler
Create a patient class and a doctor class. Have a doctor that can handle multiple patients and setup a scheduling program where a doctor can only handle 16 patients during an 8 hr work day.
'''

class Doctor:

    def __init__(self, first_name, last_name, speciality):
        self.first_name = first_name
        self.last_name = last_name
        self.speciality = speciality
        self.appointment = Appointment()

    def is_available(self, date):
        self.appointment.is_available(date)

    def make_appointment(self, date, patient_record):
        self.appointment.add_appointment(date, patient_record)


class Patient:

    def __init__(self, id, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.patient_record = {"First name": first_name,
                               "Last name": last_name,
                               "ID": id}


class Appointment(object):

    def __init__(self):
        self.appointments = {}

    def is_available(self, date):
        return date not in self.appointments

    def add_appointment(self, date, patient_record):
        self.appointments[date] = patient_record
