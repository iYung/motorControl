'''
Documentation, License etc.

@package motorControl
'''

#import RPi.GPIO as GPIO
import time as t

class stepper(object):
  
  #pattern required to turn the steppers
  Seq = [[1,0,0,1],
	 [1,0,0,0],
         [1,1,0,0],
         [0,1,0,0],
         [0,1,1,0],
         [0,0,1,0],
         [0,0,1,1],
         [0,0,0,1]] 
  
  #length of the sequence
  StepCount = len(Seq)
  
  #params
  ##boardMode --type on pin numbering, true means board, else BCM
  ##pin1-4 --pins for the stepper
  ##clockwise --sets movement to be clockwise, conterclock wise if false
  ##precise --if true, sets stepper for 8 bit movement. else, 4 bit movement
  def __init__(self, boardMode=None, pin1=None ,pin2=None, pin3=None, pin4=None, clockwise=None, precise=None):

    #set to correct mode
    if boardMode:
      print("Board mode")
      #GPIO.setmode(GPIO.BOARD)
    else:
      print("BCM mode")
      #GPIO.setmode(GPIO.BCM)
      
    #remove warnings
    #GPIO.setwarnings(False)
    
    #set up the pins array
    self.pins = [pin1,pin2,pin3,pin4]
    
    #set pins as output
    for pin in self.pins:
      print("pin setup of " + str(pin))
      #GPIO.setup(pin,GPIO.OUT)
      #GPIO.output(pin, False)
    
    #stores direction
    if clockwise:
      self.direction = 1
    else:
      self.direction = -1
    
    #sets step size with precise
    if precise:
      self.stepSize = 1
    else:
      self.stepSize = 2
    
var = stepper(1,1,2,3,4,1)