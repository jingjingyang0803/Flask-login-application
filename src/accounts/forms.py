from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from src.accounts.models import User

import re

class TUNIEmail:
    """Ensure email belongs to the TUNI domain."""
    def __init__(self, message=None):
        if not message:
            message = "Email must be a TUNI email address (@tuni.fi)."
        self.message = message

    def __call__(self, form, field):
        if not field.data.endswith('@tuni.fi'):
            raise ValidationError(self.message)

class OtpLoginForm(FlaskForm):
    email = EmailField("Tuni Email", validators=[DataRequired(), Email(), TUNIEmail()])
    password = StringField("6-digits verification code", validators=[Length(max=6)])

class PasswordStrength:
    def __init__(self, message=None):
        if not message:
            message = 'Password must include at least one lowercase letter, one uppercase letter, one digit, and one special character.'
        self.message = message

    def __call__(self, form, field):
        password = field.data
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).+$', password):
            raise ValidationError(self.message)

class LoginForm(FlaskForm):
    email = EmailField("Tuni Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    email = EmailField(
        "Tuni Email", validators=[DataRequired(), Email(message=None), Length(min=6, max=40), TUNIEmail()]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25),
            PasswordStrength()]
    )
    confirm = PasswordField(
        "Repeat password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True

class ResetForm(FlaskForm):
    email = EmailField(
        "Tuni Email", validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25),
            PasswordStrength()]
    )
    confirm = PasswordField(
        "Repeat password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )

    def validate(self):
        initial_validation = super(ResetForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append("Email is not registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True

class ForgotPasswordForm(FlaskForm):
    email = EmailField("Tuni Email", validators=[DataRequired(), Email()])