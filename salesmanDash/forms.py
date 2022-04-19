from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField,StringField
from wtforms.validators import DataRequired, EqualTo


class login(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class regForm(FlaskForm):

    businessName = StringField("Business name", validators=[DataRequired()])
    botName = StringField("Chatbot name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField()

