# Flask User Authentication With Email Verification

The initial code of this app is sourced from: https://github.com/ashutoshkrris/Flask-User-Authentication-With-Email-Verification

## Getting Started

1. Clone the repository
2. After creating and activating a virtual environment, run the following command to install all the dependencies:

   ```
   $ pip install -r requirements.txt
   ```

3. Create a file named `.env` in the root directory and add the following content there:

   ```
   export SECRET_KEY=your_secret_key
   export DEBUG=True
   export APP_SETTINGS=config.DevelopmentConfig
   export DATABASE_URL=sqlite:///db.sqlite
   export FLASK_APP=src
   export FLASK_DEBUG=1

   export SECURITY_PASSWORD_SALT=salt_value_used_for_hashing_passwords
   export EMAIL_USER=your_gmail_account
   export EMAIL_PASSWORD=your_gmail_app_password
   ```

   Create app passwords for a gmail account:

   https://www.youtube.com/watch?v=nOkpTwPvDTg

   https://support.google.com/mail/answer/185833?hl=en

   In production environments:

   ```
   export SECRET_KEY=your_secret_key
   export DEBUG=False
   export APP_SETTINGS=config.ProductionConfig
   export DATABASE_URL=postgresql://username:password@hostname:port/database_name
   export FLASK_APP=src
   export FLASK_DEBUG=0

   export SECURITY_PASSWORD_SALT=salt_value_to_hash_passwords
   export EMAIL_USER=your_gmail_account
   export EMAIL_PASSWORD=your_gmail_app_password
   ```

   If you use SendGrid SMTP service to enable sending emails, please add the following:

   ```
   export MAIL_SENDER=your_verified_identity_email_in_sendgrid
   export SENDGRID_API_KEY=your_api_key_in_sendgrid
   ```

4. Run the following command to export all the environment variables from the `.env` file:

   ```
   source .env
   ```

5. Run the following commands to set up the database:

   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the following command to run the tests:

   ```
   python3 manage.py test
   ```

7. Run the following command to run the Flask server:

   ```
   python3 manage.py run
   ```

   Once the app is running, go to **http://localhost:5000/register** to register a new user. You will notice that after completing the registration, the app will automatically log you in and redirect you to the main page.

## Create and activate a virtual environment

1. Install the virtual environment package:

   ```
   pip install virtualenv
   ```

2. Navigate to your project directory and create a virtual environment:

   ```
   cd your_project_directory
   virtualenv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```
     venv\\Scripts\\activate
     ```

   - On Unix or MacOS:

     ```
     source venv/bin/activate
     ```

## Features

1. Implemented Flask login/logout functionality to ensure secure user authentication and session management.
2. Used a salt value along with URLSafeTimedSerializer to generate tokens for email verification, password reset, and other sensitive operations, adding an additional layer of security to token generation and validation processes.
3. Utilized bcrypt hashing algorithm to securely hash user passwords before storing them in the database, ensuring that sensitive information remains protected even in the event of a breach.
4. Restricted login access to only "tuni" users, enhancing security by allowing access only to authorized individuals.
5. Implemented expiration times for various links sent through email, such as account activation links (1 hour), password reset links (15 minutes), and one-time login verification codes (15 minutes), enhancing security by limiting the window of vulnerability.
6. Enforced strong password requirements, mandating that user passwords must include at least one lowercase letter, one uppercase letter, one digit, and one special character for a successful registration, thereby enhancing password security and resilience against brute-force attacks.
7. Implemented a login failure notification system, informing account owners of any unauthorized access attempts(5 login failure within one hour), thereby enhancing security by promptly alerting users to potential threats.
8. Optimized user interface for smooth navigation, ensuring a seamless and intuitive experience for all users.
9. Implemented user-friendly messages at each step of the user journey, including notifications and error messages, to provide clear guidance and enhance user satisfaction.
10. Enabled a password reset feature, empowering users to regain access to their accounts securely in case of forgotten passwords.
11. Implemented a password field toggle feature, allowing users to conveniently hide or show their passwords as needed, enhancing usability and accessibility.
12. Implemented custom error pages for HTTP status codes such as 401 (Unauthorized), 404 (Not Found), and 500 (Internal Server Error), providing users with informative and user-friendly error messages in case of unexpected issues, thereby improving user experience and reducing frustration.
