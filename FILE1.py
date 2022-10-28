from tkinter import *		
import tkinter.font
from gpiozero import LED as led1 
from gpiozero import LED as led2
from gpiozero import LED as led3
import RPi.GPIO	as GPIO					   

GPIO.setmode(GPIO.BOARD)	   

redLED = led1(17)						
yellowLED = led2(27)					
greenLED = led3(22)					    

win = Tk()							    
win.title("Led Toggler")				 
winFont = tkinter.font.Font(family = 'Arial' , size = 20, weight = "bold")
									    
def redLEDToggle():						
	if redLED.is_lit:					
		redLED.off()					
		redLEDButton["text"] = "Turn Red LED on"
												
	else:
		yellowLED.off()					
		greenLED.off()					
		redLED.on()						
		redLEDButton["text"] = "Turn Red LED off"


def yellowLEDToggle():
	if yellowLED.is_lit:
		yellowLED.off()
		yellowLEDButton["text"] = "Turn yellow LED on"
	else:
		redLED.off()
		greenLED.off()
		yellowLED.on()
		yellowLEDButton["text"] = "Turn blue LED off"


def greenLEDToggle():
	if greenLED.is_lit:
		greenLED.off()
		greenLEDButton["text"] = "Turn Green LED on"
	else:
		redLED.off()
		yellowLED.off()
		greenLED.on()
		greenLEDButton["text"] = "Turn Green LED off"

def close():							
	redLED.off()						
	yellowLED.off()						
	greenLED.off()						
	win.destroy()						

redLEDButton = Radiobutton(win, text = 'Turn Red LED on', font  = winFont, command = redLEDToggle, bg = 'red', height = 1, width = 24).pack()
										

										

yellowLEDButton = Radiobutton(win, text = 'Turn yellow LED on', font  = winFont, command = yellowLEDToggle, bg = 'yellow', height = 1, width = 24).pack()

greenLEDButton = Radiobutton(win, text = 'Turn Green LED on', font  = winFont, command = greenLEDToggle, bg = 'green', height = 1, width = 24).pack() 


exitButton = Radiobutton(win, text = 'Exit', font  = winFont, command = close, width = 24).pack()  


win.protocol("WM_DELETE_WINDOW", close)	
win.mainloop()							


