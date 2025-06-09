import sqlite3
from appointments import Appointment

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('appointments.db')

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
        c.execute("INSERT INTO appointments VALUES (:id, :pid, :did, :dt, "
                  ":reason, :stat)",
                  {'id': apt.id, 'pid': apt.patient_id, 'did': apt.doctor_id,
                   'dt': apt.datetime, 'reason': apt.reason,
                   'stat': apt.status})


# remove appointment
def rem_apt(apt):
    with conn:
        c.execute("DELETE from appointments WHERE id = :id",
                  {'id': apt.id})


# update appointment time
def update_time(apt, time):
    with conn:
        c.execute("UPDATE appointments SET datetime = :dt WHERE id = :id",
                  {'dt': time, 'id': apt.id})


# get appointment by patient_id
def get_apt_patient(patient_id):
    c.execute("SELECT * FROM appointments WHERE patient_id =:pid",
              {'pid': patient_id})
    return c.fetchall()


# get appointment by doctor_id
def get_apt_doctor(doctor_id):
    c.execute("SELECT * FROM appointments WHERE doctor_id =:did",
              {'did': doctor_id})
    return c.fetchall()
