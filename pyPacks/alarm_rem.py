import time as t
from playsound import playsound
import pyttsx3
ob=pyttsx3.init()
class alarm_rem:
	def __init__(self,tm):
		self.tm=tm
	def alarm_time(self):
		if "set alarm" in self.tm:
			ti=self.tm.replace('.','')  				#handle dots as they are unwanted
			r=ti.replace(':','')  					#handle colons as they get missed 
			print (r.upper())					#print everything in uppercase for easier comparison		
			while ((t.strftime(" %I%M").replace(' 0','') or t.strftime("%p")) not in r.upper()): #%I prints a 0 for time<10		
				print (t.strftime(" %I%M").replace(' 0',''))
				t.sleep(1)
			print("time out")							
			playsound('believer.mp3')
		'''else:
			while ((t.strftime("%B") not in self.tm) or (t.strftime("%d") not in self.tm)):
				t.sleep(1)
			print("date's here!")
			ob.say("there is a reminder")
			ob.say("it is " + self.tm.replace("reminder","") )
			ob.runAndWait()
'''
	

