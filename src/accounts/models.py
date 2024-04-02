from datetime import datetime, timedelta, timezone

from flask_login import UserMixin

from src import bcrypt, db

import pytz

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    failed_login_attempts = db.Column(db.Integer, default=0)
    last_failed_login = db.Column(db.DateTime)

    def __init__(
        self, email, password, is_admin=False, is_confirmed=False, confirmed_on=None
    ):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.created_on = datetime.now()
        self.is_admin = is_admin
        self.is_confirmed = is_confirmed
        self.confirmed_on = confirmed_on

    def __repr__(self):
        return f"<email {self.email}>"

class OTP(UserMixin, db.Model):
    __tablename__ = 'otps'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    otp_code = db.Column(db.String(6), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow().replace(tzinfo=pytz.utc))
    expires_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, otp_code, lifespan_in_minutes=15):
        self.email = email
        self.otp_code = otp_code
        self.expires_at = datetime.utcnow().replace(tzinfo=pytz.utc) + timedelta(minutes=lifespan_in_minutes)

    def is_expired(self):
        return datetime.now(timezone.utc).replace(tzinfo=None) > self.expires_at

    def __repr__(self):
        return f"<OTP for {self.email}>"
