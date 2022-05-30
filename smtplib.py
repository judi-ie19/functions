# from http import server
# import smtplib

# sender_email='owuorakinyijudith@gmail.com'
# rec_email='handelowino@gmail.com'
# password=input("enter your password: ")
# message="Hey i've missed you"

# server=smtplib.SMTP("smtp.gmail.com",587)
# server.starttls()
# server.login(sender_email,password)
# print("Login success")
# # server.sendmail(sender_email,rec_email,message)


import smtplib,ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "owuorakinyijudith@gmail.com.com"
receiver_email = "handelowino@gmail.com"
password = input("Type your password and press enter:")
message = """
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

