'''
Documentation, License etc.

@package motorControl
'''

#import RPi.GPIO as GPIO
import time as t

class stepper(object):
  
  #params
  ##boardMode --type on pin numbering, true means board, else BCM
  ##pin1.4 -- pins for the stepper
  def __init__(self, boardMode=None, pin1=None ,pin2=None, pin3=None, pin4=None):
    
    #set to correct mode
    if boardMode:
      print("Board mode")
      #GPIO.setmode(GPIO.BOARD)
    else:
      print("BCM mode")
      #GPIO.setmode(GPIO.BCM)
      
    #remove warnings
    #GPIO.setwarnings(False)
    
    self.pins = [pin1,pin2,pin3,pin4]
    
var = stepper()