import sqlite3
from appointments import Appointment

conn = sqlite3.connect(':memory:')

# conn = sqlite3.connect('appointments.db')

c = conn.cursor()

c.execute("""CREATE TABLE appointments (
            id integer,
            patient_id integer,
            doctor_id integer
            datetime text
            reason text
            status text
            )""")

# add appointment
def add_apt(apt):
    with conn:
        pass


# remove appointment
def rem_apt(apt):
    with conn:
        pass


# update appointment time
def update_time(apt, time):
    with conn:
        pass


# get appointment by patient_id
def get_apt_patient(patient_id):
    pass


# get appointment by doctor_id
def get_apt_doctor(doctor_id):
    pass
