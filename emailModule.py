import email
import email.mime.application
import smtplib


def sendMail(body, sender, receiver, password, filename, fileType):
    msg = email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = 'Greetings'
    msg['From'] = sender
    msg['To'] = receiver

    body = email.mime.Text.MIMEText(body + "\n\nPS: I found that amazing file you were searching for years, PFA")
    msg.attach(body)

    fp = open(filename,'rb')
    att = email.mime.application.MIMEApplication(fp.read(), _subtype=fileType)
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)

    s = smtplib.SMTP('smtp.gmail.com')
    s.starttls()
    s.login(sender,password)
    s.sendmail(sender,[receiver], msg.as_string())
    s.quit()

if __name__ == "__main__":
    sendMail(
        "Hello, this is a test email",
        "keryx.messenger@gmail.com",
        "himanshuj.cs14@rvce.edu.in@gmail.com",
        "11211121",
        "README.md",
        "md"
    )