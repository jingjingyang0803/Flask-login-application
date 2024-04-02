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

## Check SQLite database

```sql
# Navigate to the directory where the db.sqlite file is located
cd src

# Run the SQLite command-line interface
sqlite3 db.sqlite

# List all the tables in the database
.tables

# View the actual data in the users table
SELECT * FROM users;

# To delete all records from a table in SQLite
DELETE FROM users;

# To delete a specific row from a table in SQLite
# with a condition that identifies the specific row
# (for example, email = "john.smith@tuni.fi")
DELETE FROM users WHERE condition;

# Exit the SQLite prompt
CTRL + D
```
