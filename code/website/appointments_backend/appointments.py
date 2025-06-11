class Appointment:

    def __init__(self, id, patient_id, doctor_id, datetime, reason, status):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.datetime = datetime
        self.reason = reason
        self.status = status


    @property
    def get_apt_id(self):
        return '{}'.format(self.id)

    def get_patient_id(self):
        return '{}'.format(self.patient_id)

    def get_doctor_id(self):
        return '{}'.format(self.doctor_id)

    def get_datetime(self):
        return '{}'.format(self.datetime)

    def get_reason(self):
        return '{}'.format(self.reason)

    def get_status(self):
        return '{}'.format(self.status)

    def __repr__(self):
        return "Appointment {}: patient {} with {} @ {} for {} with " \
               "status: {}".format(self.id, self.patient_id, self.doctor_id,
                                   self.datetime, self.reason, self.status)
