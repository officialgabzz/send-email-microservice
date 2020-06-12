import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail




if __name__ == "__main__":
    message = Mail(
    from_email='garubamalik@gmail.com',
    to_emails='mgaruba@memmcol.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)