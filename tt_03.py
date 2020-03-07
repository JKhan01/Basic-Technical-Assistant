from tkinter import *
from tkinter import messagebox
from PIL import Image
import PIL.ImageTk
import speech_recognition as sr
import pyttsx3
import time
from pyPacks.alarm_rem import alarm_rem		#self-made for alarm
from pyPacks.ytube import ytube				#self-made for youtube
from pyPacks.g_search import g_search		#self-made for google_search
from pyPacks.fhan import fhan				#self-made for basic file handling
import multiprocessing as mp
obj=pyttsx3.init()
obj.setProperty('rate',175)
obj.setProperty('volume',0.5)
def spk():
	r=sr.Recognizer()
	m=sr.Microphone()
	
	cmd_list={"alarm and rem":["set alarm","set reminder"],
	"youtube":["play","play trailer of","play highlights of","play match highlights of","play teaser of"],
	"google search":["who is the","which is the","tell me the","search","read","provide","provide update on","update me with","find me","tell me about","update about","show me","update me ","what is"],
	"file_handling":["open","create"]}#command dataset^^^^^^^
	
	try:
		with m as source:
			print ("..speak..")
			obj.say("go ahead ")
			obj.runAndWait()
			#obj.stop()
			#time.sleep(5)
			print ("speak")
			r.energy_threshold = 1000
			tlk = r.listen(source)	#record speech
		#time.sleep(1)
		#time.sleep(2)
		st = r.recognize_google(tlk)
		print (st)
		c=0
		lb_01 = Label(top, text=st, font=(("Ubuntu Condensed"),18) )
		lb_01.place(x=383, y=200, height=50, width=650)
		for i in cmd_list:    							#iterate through dictionary keys
			for j in cmd_list[i]:
				if j in st:    						#check for keywords within the string
					print (i + " command recognized")
					obj.say(i + "command recognized")
					obj.runAndWait()
					obj.stop()
					c=1
					if (i=="alarm and rem"):
						if (j=="set alarm"):
							print("ALARM SET!!")
							obj.say("alarm set")
							obj.runAndWait()			
							k=alarm_rem(st)
							k.alarm_time()
							lb_04=Label(top, text="ALARM", font=(("Ubuntu Condensed"),18) )
							lb_04.place(x=683-175, y=100, height=50, width=500)
							#p1=mp.Process(target=k.alarm_time)
							#p2=mp.Process(target=spk)
							#p1.start()
							#p2.start()
							#break
						else:
							lst.append(st.replace("set"," "))
							lb_02=Label(top, text=st.replace("set"," "), font=(("Ubuntu Condensed"),18))
							lb_02.place(x=683-175, y=100, height=50, width=500)
							#break

					elif (i=="google search"):
						print("searching...")
						obj.say("okay, searching")
						obj.runAndWait()
						k_01=g_search(st)
						k_01.g_url()
						#break
					elif (i=="youtube"):
						print("youtube streaming")
						obj.say("there we go")
						obj.runAndWait()
						k_02=ytube(st)
						k_02.srch_to_url()
						#break
					elif (i=="file_handling"):
						print("file handling ")
						obj.say("ok working upon")
						obj.runAndWait()
						k_03=fhan(st)
						k_03.f_handle()
						#break
					else:
						obj.say("try  again!!")
						obj.runAndWait()
						#break
					
				#else:
				#	obj.say("command didn't match")
				#	obj.runAndWait()
		if c==0:
			obj.say("command not recognised")
			obj.runAndWait()
		
	except sr.UnknownValueError:
		obj.say("sorry,couldn't understand")
		obj.runAndWait()
	except sr.RequestError:
		obj.say("sorry,connection failed")
		obj.runAndWait()
	
	#print (st)
def rm():
	count=0
	for j in lst:
		if ((time.strftime("%M") in lst) and (time.strftime("%d") in lst)):
			obj.say("reminder for today")
			obj.say(j)
			count+=1
	if count==0:			
		obj.say("no reminders for today")
		obj.runAndWait()
lst=['reminder list']	
top = Tk()
top.configure(bg="cyan4")
top.geometry("1366x768")
C = Canvas(top, bg="black", height=480, width=852)
filename = PIL.ImageTk.PhotoImage(Image.open("/home/jkhan01/Downloads/trial_wallpaper.jpg"))
background_label = Label(top, image=filename)
background_label.place(x=257, y=144, height=480, width=852)
lb_main=Label(top, text="BASIC TECHNICAL ASSISTANT WITH INTELLIGENCE", font=(("Ubuntu Condensed"),30))
lb_main.place(x=0,y=20, height=40, width=1300)
lb_main["bg"]="cyan4"
lb_03 = Label(top, text="Press the blue button to speak!", font=(("Ubuntu Condensed"),18))
lb_03["bg"]="cyan4"
lb_03.place(x=520 ,y=650 , height=50, width=350)
bt_img01 = PIL.ImageTk.PhotoImage(Image.open("/home/jkhan01/Downloads/final_1-2.jpg"))
bt_01 = Button(top, image=bt_img01, command= spk)
bt_01["bg"] = "cyan4"
bt_01["border"] = "0"
bt_01.place(x=580,y=450, height=160, width=160)
bt_02 = Button(top, text="check reminders for today", command= rm)
bt_02["bg"] = "royal blue"
bt_02["border"] = "0"
bt_02.place(x=510,y=100, height=50, width=250)
#C.pack()
#bt_01.pack()
top.mainloop()

