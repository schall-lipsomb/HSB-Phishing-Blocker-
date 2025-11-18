import smtplib
from email.message import EmailMessage


def send_email(host='127.0.0.1', port=1025, msg=None):
    with smtplib.SMTP(host, port) as s:
        s.send_message(msg)
        print('Sent message:', msg['Subject'])


def make_benign():
    msg = EmailMessage()
    msg['From'] = 'Alice <alice@example.com>'
    msg['To'] = 'bob@example.local'
    msg['Subject'] = 'Weekly report'
    msg.set_content('Hi Bob,\n\nPlease find the weekly report attached.\n\nThanks,\nAlice')
    return msg


def make_phish():
    msg = EmailMessage()
    msg['From'] = 'Support <support@paypal.example.com>'
    msg['To'] = 'victim@example.local'
    msg['Subject'] = 'URGENT: Verify your account now'
    html = '''
    <html><body>
      <p>Please <a href="http://malicious.example.com/login">click here</a> to verify your account.</p>
      <p>Also visit <a href="http://another.bad/link">www.paypal.com</a> for more info.</p>
      <p>Regards,<br/>Support Team</p>
    </body></html>
    '''
    msg.set_content('Please verify your account by visiting the link: http://malicious.example.com/login')
    msg.add_alternative(html, subtype='html')
    return msg


if __name__ == '__main__':
    benign = make_benign()
    phish = make_phish()
    send_email(msg=benign)
    send_email(msg=phish)
