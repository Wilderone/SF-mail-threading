import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def email_send(reciever, subject, message):

    message = Mail(
        from_email='test.testovich.2021@list.ru',
        to_emails=f'{{reciever}}',
        subject=f'{{subject}}',
        html_content=f'{{message}}')

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.body)
    except Exception as e:
        print(e)
