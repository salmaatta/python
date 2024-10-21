#class patient
class Patient:
    def __init__(self, patient_id, name, age, gender, contact_info, medical_history=None):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_info = contact_info
        self.medical_history = medical_history if medical_history is not None else []

    def update_contact_info(self, new_contact_info):
        self.contact_info = new_contact_info

    def view_details(self):
        print(f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Contact: {self.contact_info}")

    def add_medical_history(self, history_entry):
        self.medical_history.append(history_entry)

    def view_medical_history(self):
        for entry in self.medical_history:
            print(entry)


class Doctor:
    def __init__(self, doctor_id, name, specialization, experience, contact_info, availability=True):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.experience = experience
        self.contact_info = contact_info
        self.availability = availability

    def view_details(self):
        print(f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}, Experience: {self.experience} years")

    def manage_availability(self, available):
        self.availability = available


class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time, status='Scheduled'):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def reschedule(self, new_date, new_time):
        self.date = new_date
        self.time = new_time

    def view_details(self):
        print(f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.date}, Time: {self.time}, Status: {self.status}")


class Billing:
    def __init__(self, bill_id, consultation_fee, medication_fee, other_services_fee):
        self.bill_id = bill_id
        self.consultation_fee = consultation_fee
        self.medication_fee = medication_fee
        self.other_services_fee = other_services_fee
        self.total_cost = self.calculate_total()

    def calculate_total(self):
        return self.consultation_fee + self.medication_fee + self.other_services_fee

    def apply_discount(self, discount):
        self.total_cost -= discount

    def view_bill(self):
        print(f"Bill ID: {self.bill_id}, Total Cost: {self.total_cost}")


class ClinicManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.bills = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

    def generate_bill(self, bill):
        self.bills.append(bill)

    def find_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def find_doctor_by_id(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        return None

    def display_menu(self):
        print("\n--- Clinic Management System Menu ---")
        print("1. Add Patient")
        print("2. View Patient Details")
        print("3. Add Doctor")
        print("4. View Doctor Details")
        print("5. Schedule Appointment")
        print("6. View Appointment Details")
        print("7. Generate Bill")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_patient_prompt()
            elif choice == '2':
                self.view_patient_details()
            elif choice == '3':
                self.add_doctor_prompt()
            elif choice == '4':
                self.view_doctor_details()
            elif choice == '5':
                self.schedule_appointment_prompt()
            elif choice == '6':
                self.view_appointment_details()
            elif choice == '7':
                self.generate_bill_prompt()
            elif choice == '8':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_patient_prompt(self):
        patient_id = int(input("Enter patient ID: "))
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        gender = input("Enter patient gender: ")
        contact_info = input("Enter patient contact info: ")
        patient = Patient(patient_id, name, age, gender, contact_info)
        self.add_patient(patient)
        print("Patient added successfully.")

    def view_patient_details(self):
        patient_id = int(input("Enter patient ID to view: "))
        patient = self.find_patient_by_id(patient_id)
        if patient:
            patient.view_details()
        else:
            print("Patient not found.")

    def add_doctor_prompt(self):
        doctor_id = int(input("Enter doctor ID: "))
        name = input("Enter doctor name: ")
        specialization = input("Enter doctor specialization: ")
        experience = int(input("Enter doctor years of experience: "))
        contact_info = input("Enter doctor contact info: ")
        doctor = Doctor(doctor_id, name, specialization, experience, contact_info)
        self.add_doctor(doctor)
        print("Doctor added successfully.")

    def view_doctor_details(self):
        doctor_id = int(input("Enter doctor ID to view: "))
        doctor = self.find_doctor_by_id(doctor_id)
        if doctor:
            doctor.view_details()
        else:
            print("Doctor not found.")

    def schedule_appointment_prompt(self):
        appointment_id = int(input("Enter appointment ID: "))
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM AM/PM): ")

        patient = self.find_patient_by_id(patient_id)
        doctor = self.find_doctor_by_id(doctor_id)

        if patient and doctor:
            appointment = Appointment(appointment_id, patient, doctor, date, time)
            self.schedule_appointment(appointment)
            print("Appointment scheduled successfully.")
        else:
            print("Invalid patient or doctor ID.")

    def view_appointment_details(self):
        appointment_id = int(input("Enter appointment ID to view: "))
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                appointment.view_details()
                break
        else:
            print("Appointment not found.")

    def generate_bill_prompt(self):
        bill_id = int(input("Enter bill ID: "))
        consultation_fee = float(input("Enter consultation fee: "))
        medication_fee = float(input("Enter medication fee: "))
        other_services_fee = float(input("Enter other services fee: "))
        bill = Billing(bill_id, consultation_fee, medication_fee, other_services_fee)
        self.generate_bill(bill)
        bill.view_bill()
        print("Bill generated successfully.")

        if __name__ == "__main__":
    # Create an instance of the ClinicManagementSystem
            clinic = ClinicManagementSystem()

    # Add some demo patients and doctors
    patient1 = Patient(1, "John Doe", 30, "Male", "123-456-7890")
    doctor1 = Doctor(101, "Dr. Smith", "Cardiology", 10, "987-654-3210")
    
    add_patient(patient1)

    # Create an appointment
    appointment1 = Appointment(201, patient1, doctor1, "2024-10-22", "10:00 AM")
    clinic.schedule_appointment(appointment1)

    # Generate a bill
    bill1 = Billing(301, 100, 50, 20)
    clinic.generate_bill(bill1)

    # View some details
    patient1.view_details()
    doctor1.view_details()
    appointment1.view_details()
    bill1.view_bill()


