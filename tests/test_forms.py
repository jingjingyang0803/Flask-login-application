import unittest

from base_test import BaseTestCase

from src.accounts.forms import LoginForm, RegisterForm


class TestRegisterForm(BaseTestCase):
    def test_validate_success_register_form(self):
        # Ensure correct data validates.
        form = RegisterForm(email="new@tuni.fi",
                            password="Hello1234?", confirm="Hello1234?")
        self.assertTrue(form.validate())

    def test_validate_invalid_password_format(self):
        # Ensure incorrect data does not validate.
        form = RegisterForm(email="new@test.com",
                            password="example", confirm="")
        self.assertFalse(form.validate())

    def test_validate_email_already_registered(self):
        # Ensure user can't register when a duplicate email is used
        form = RegisterForm(
            email="unconfirmeduser@gmail.com", password="unconfirmeduser", confirm="unconfirmeduser"
        )
        self.assertFalse(form.validate())


class TestLoginForm(BaseTestCase):
    def test_validate_success_login_form(self):
        # Ensure correct data validates.
        form = LoginForm(email="unconfirmeduser@gmail.com",
                         password="unconfirmeduser")
        self.assertTrue(form.validate())

    def test_validate_invalid_email_format(self):
        # Ensure invalid email format throws error.
        form = LoginForm(email="unknown", password="example")
        self.assertFalse(form.validate())


if __name__ == "__main__":
    unittest.main()
