'''
Documentation, License etc.

@package motorControl
'''

#import RPi.GPIO as GPIO
import time as t

class stepper(object):
  
  #params
  ##boardMode --type on pin numbering, true means board, else BCM
  ##pin1-4 --pins for the stepper
  ##clockwise --sets movement to be clockwise, conterclock wise if false
  def __init__(self, boardMode=None, pin1=None ,pin2=None, pin3=None, pin4=None, clockwise=None):
    
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
    self.clockwise = clockwise
    
var = stepper(1,1,2,3,4,1)