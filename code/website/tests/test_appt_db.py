"""
Unit tests for appointments database.

@ai-generated
Tool: GitHub Copilot
Prompt: N/A
Generated on: 2025-06-03
Modified by: Adriel Domingo
Modifications: PEP8 compliance
Verified:  reviewed
"""

import os
import shutil
from django.test import TestCase
from appointments import Appointment
import appointments_db

DB_PATH = 'appointments.db'
DB_BACKUP_PATH = 'appointments.db.bak'

class AppointmentsDBTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Backup the real DB if it exists
        if os.path.exists(DB_PATH):
            shutil.copyfile(DB_PATH, DB_BACKUP_PATH)
        # Ensure table exists (if running for the first time)
        try:
            appointments_db.c.execute("SELECT 1 FROM appointments LIMIT 1")
        except Exception:
            appointments_db.c.execute("""CREATE TABLE IF NOT EXISTS appointments 
            (
                id integer,
                patient_id integer,
                doctor_id integer,
                datetime text,
                reason text,
                status text
            )""")
            appointments_db.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Restore the real DB after tests
        if os.path.exists(DB_BACKUP_PATH):
            shutil.move(DB_BACKUP_PATH, DB_PATH)
        super().tearDownClass()

    def setUp(self):
        # Clear all appointments before each test (test isolation)
        appointments_db.c.execute("DELETE FROM appointments")
        appointments_db.conn.commit()

    def test_add_appointment_by_patient(self):
        apt = Appointment(id=1, patient_id=100, doctor_id=200,
                          datetime="2025-06-03 10:00", reason="Checkup",
                          status="Scheduled")
        appointments_db.add_apt(apt)
        results = appointments_db.get_apt_patient(100)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], 100)  # patient_id

    def test_add_and_get_appointment_by_doctor(self):
        apt = Appointment(id=2, patient_id=101, doctor_id=201,
                          datetime="2025-06-04 09:00", reason="Consult",
                          status="Scheduled")
        appointments_db.add_apt(apt)
        results = appointments_db.get_apt_doctor(201)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][2], 201)  # doctor_id

    def test_remove_appointment(self):
        apt = Appointment(id=3, patient_id=102, doctor_id=202,
                          datetime="2025-06-05 14:00", reason="Follow-up",
                          status="Scheduled")
        appointments_db.add_apt(apt)
        appointments_db.rem_apt(apt)
        results = appointments_db.get_apt_patient(102)
        self.assertEqual(len(results), 0)

    def test_update_time(self):
        apt = Appointment(id=4, patient_id=103, doctor_id=203,
                          datetime="2025-06-06 15:00", reason="Test",
                          status="Scheduled")
        appointments_db.add_apt(apt)
        appointments_db.update_time(apt, "2025-06-07 16:00")
        results = appointments_db.get_apt_patient(103)
        self.assertEqual(results[0][3], "2025-06-07 16:00")