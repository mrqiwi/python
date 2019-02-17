#!/usr/bin/python3

import smtplib, getpass
 

def send_email(host, subject, to_addr, from_addr, text):

    body = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (from_addr, to_addr, subject, text)
 	
    password = getpass.getpass()

    server = smtplib.SMTP_SSL(host)
    server.login('mrqiwi@ya.ru',password)
    server.sendmail(from_addr, to_addr, body)    
    server.quit() 
 
if __name__ == "__main__":

    host = 'smtp.yandex.ru'
    subject = 'check connection'
    to_addr = '7ssa7@inbox.ru'
    from_addr = 'mrqiwi@ya.ru'
    text = 'hi, my friend'
    
    send_email(host, subject, to_addr, from_addr, text)
