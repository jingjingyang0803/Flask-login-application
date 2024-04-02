from sendgrid.helpers.mail import Mail

from src import app, sg_client


def send_email(subject, to, template):
    msg = Mail(
        from_email=app.config["MAIL_DEFAULT_SENDER"],
        to_emails=[to],
        subject=subject,
        html_content=template
    )
    sg_client.send(msg)
