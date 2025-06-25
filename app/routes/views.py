from flask import Blueprint, render_template, redirect, url_for
from ..models import Patient, Appointment, db
from ..forms import PatientForm, AppointmentForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(
            full_name=form.full_name.data,
            age=form.age.data,
            gender=form.gender.data,
            complaint=form.complaint.data
        )
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('main.patients'))
    return render_template('register.html', form=form)

@main.route('/patients')
def patients():
    patients_list = Patient.query.all()
    return render_template('patients.html', patients=patients_list)

@main.route('/appointment', methods=['GET', 'POST'])
def appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        appt = Appointment(
            patient_name=form.patient_name.data,
            doctor=form.doctor.data,
            date=form.date.data,
            time=form.time.data
        )
        db.session.add(appt)
        db.session.commit()
        return redirect(url_for('main.appointments'))
    return render_template('appointment.html', form=form)

@main.route('/appointments')
def appointments():
    appts = Appointment.query.order_by(Appointment.date, Appointment.time).all()
    return render_template('appointments.html', appointments=appts)
