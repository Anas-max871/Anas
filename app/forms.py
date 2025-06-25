from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.fields import DateField, TimeField
from wtforms.validators import DataRequired, NumberRange, ValidationError

class PatientForm(FlaskForm):
    full_name = StringField('ФИО', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired(), NumberRange(min=0, message='Возраст не может быть отрицательным')])
    gender = SelectField('Пол', choices=[('Мужской','Мужской'), ('Женский','Женский')], validators=[DataRequired()])
    complaint = StringField('Жалобы', validators=[DataRequired()])
    submit = SubmitField('Зарегистрировать')

    def validate_full_name(self, field):
        if len(field.data.split()) < 3:
            raise ValidationError('Введите не менее трёх слов ФИО')

class AppointmentForm(FlaskForm):
    patient_name = StringField('ФИО пациента', validators=[DataRequired()])
    doctor = SelectField('Врач', choices=[
        ('Иванов А.А.','Иванов А.А.'),
        ('Петров Б.Б.','Петров Б.Б.'),
        ('Сидоров В.В.','Сидоров В.В.')
    ], validators=[DataRequired()])
    date = DateField('Дата приёма', format='%Y-%m-%d', validators=[DataRequired()])
    time = TimeField('Время приёма', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Записаться')
