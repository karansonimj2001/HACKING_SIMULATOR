#the basics i know ......
from time import sleep
import random
import array
maxlen=10
a="1","2","3","4","5","6","7","8","9","0"
b='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z'
c='A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
cmbind=a+b+c
a1=random.choice(a)
b1=random.choice(b)
c1=random.choice(c)
d=a1+b1+c1
for x in range(maxlen - 2):
	d=d+random.choice(cmbind)
	d1=array.array('u',d)
	random.shuffle(d1)
	password=""
	for x in d1:
		password=password+x

print(" █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█ \n █░░║║║╠─║─║─║║║║║╠─░░█ \n █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█ \n █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")

while True:
	x=input("ENTER THE PASSWORD : ")
	if x=="karansonimj":

		print('''|/    /\   |)	/\    |\ | 
 |\   /--\  |\ /--\   | \|''')

		hack=input("hello karan ,what do you want to do right now : ")

 #code for profile hack simulator.....
 
		if hack=="profile hack":
			input("all right karan which profile you want to hack : ")
			print("============================================================")
			sleep(1)
			for i in range(10):
				print(" analysing profile data############25% ")
			sleep(1)
			print("============================================================")
			sleep(1)
			for i in range(10):
				print(" analysing profile data############50% ")
			sleep(2)
			print("============================================================")
			sleep(1)
			for i in range(10):
				print(" analysing profile data############75% ")
			sleep(2)
			print("============================================================")
			sleep(1)
			for i in range(10):
				print(" analysing profile data############100% ")
			sleep(2)
			print("============================================================")
			sleep(1)
			for i in range(10):
				print("password crash**********************************************")
			sleep(2)
			print("============================================================")

			print("the pasword is : "+password)
			print("============================================================")
	
	
			#code for insta hack simulator....
	
		elif hack=="instagram hack":
			input("all right karan here we go, enter the insta id  : ")
			print("============================================================")
			sleep(2)
			for i in range(10):
				print(" analysing instagram name###############################25% ")
			print("============================================================")
			sleep(1)
			for i in range(10):
				print(" analysing instagram name###############################50% "*10)
			print("============================================================")
			sleep(2)
			for i in range(10):
	
				print(" analysing instagram name###############################75% ")
			print("============================================================")
			sleep(1)
			for i in range(10):
				print(" analysing instagram name###############################100%")
			print("============================================================")
			sleep(2)
			for i in range(10):
				print("password crash**********************************************")
			print("============================================================")
			sleep(2)
			print("the password is : "+password)
	
	#code for facebook hack simulator.....
	
		elif hack=="facebook hack":
			input("ohk karan , just enter the facebook id code : ")
			sleep(2)
			for i in range(10):
				print(" analysing profile  data25%")
			print("============================================================")
			sleep(1)
			for i in range(10):
				print(" analysing profile data50% ")
			print("============================================================")
			sleep(1)
			for i in range(10):
				print(" analysing profile data75% ")
			print("============================================================")
			sleep(1)
			for i in range(10):
				print(" analysing profile data100% ")
			print("============================================================")
			sleep(2)
			for i in range(5):
				print("cracking the password...........")
			print("============================================================")
			sleep(2)
			for i in range(10):
				print("password crash**********************************************")
			print("============================================================")
			sleep(1)
			print("the 5 min password is : "+password)
	else:
		print("the password is incorrect///// try again")