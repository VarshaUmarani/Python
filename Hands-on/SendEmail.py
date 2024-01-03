import smtplib
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.multipart import MIMEMultipart

# App Password - wazg xwtc ffsh bfbc

def send_mail(send_from, send_to, subject, message,
              server="smtp.gmail.com", port=587, username='', password='',
              use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    part = MIMEBase('application', "octet-stream")
    msg.attach(part)

    smtp = smtplib.SMTP(server,port)
    if use_tls:
        smtp.starttls()
        
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

send_mail("varshaumarani2002@gmail.com",["varuumarani6688@gmail.com"],"Test Mail","Good Evening Ashu...!!!",username='varshaumarani2002@gmail.com',password='wazg xwtc ffsh bfbc')