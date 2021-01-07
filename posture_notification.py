"""
Script to remind user of the system to maintain correct posture while working on the laptop.
Produces a popup window that reminds user to sit straight every few minutes. Also reminds 
the user to take a break every one hour or so.

Author: Milind Kumar V 
"""
from tkinter import *
import time
from sys import exit

def reminder(message, notification_duration = 5000):
	"""
	Function to produce a notification about sitting up straight. Notification lasts for 5 seconds.
	Much of the basic code is obtained from 

	https://stackoverflow.com/questions/36982391/how-to-display-a-system-notification-in-python

	Parameters:

	message (string): message to be printed on the popup
	notificatoin_duraton (int): duration in ms for which the notification must last. Defaults to
		5000ms = 5s.

	Returns:

	Outptuts:
		A popup box with text given by the message parameter that lasts for the period 
		notification_duration.
	"""
	popupRoot = Tk()
	popupRoot.after(notification_duration, popupRoot.destroy)
	popupButton = Button(popupRoot, text = message, font = ("Arial", 60), fg = "black", bg = "white", command = popupRoot.destroy)
	popupButton.pack()
	popupRoot.geometry('800x300+700+500')
	popupRoot.mainloop()





#### Constant definition

min_to_sec = 60
sec_to_milisec = 1e3


#### Setting parameters

posture_notification_interval = 5*min_to_sec									# Interval between successive notifications asking you to sit up straight, specified in s
posture_notification_duration = int(5*sec_to_milisec)							# Duration that a particular sit up straight notification lasts, specifiec in ms
break_notification_interval = 60*min_to_sec										# Interval between successive notifications asking you to get up and walk around, specified in s
break_notification_duration = int(break_notification_interval*sec_to_milisec)	# Duration that a particular take a break notification lasts, equal to the break notification interval as it needs to be acknowledged manually to go away
count = 0																		# Count to determine if a notification to take a break must be provided

while (True):
	reminder("Sit up straight! \nShoulders back! \nElbows by your side!", notification_duration = posture_notification_duration)
	time.sleep(posture_notification_interval)
	count = count + 1
	if (count == break_notification_interval/posture_notification_interval):
		count = 0
		reminder("Take a break! \n Stretch! \n Walk around!", notification_duration = break_notification_duration)
