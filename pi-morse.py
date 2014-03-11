# pi-morse.py -- Generates/displays ITU-Standard morse code, given ASCII text.
#                Uses GPIO pin 17 on the Rasberry Pi Model B.
# MIT License -- Copyright (c) Philip Conrad 2013, all rights reserved.

import time, sys
import RPi.GPIO as GPIO


morseITUStandard = {
"a" : ['.', '-'], #dot dash
"b" : ['-', '.', '.', '.'], #dash dot dot dot
"c" : ['-', '.', '-', '.'], #dash dot dash dot
"d" : ['-', '.', '.'], #dash dot dot
"e" : ['.'], #dot
"f" : ['.', '.', '-', '.'], #dot dot dash dot
"g" : ['-', '-', '.'], #dash dash dot
"h" : ['.', '.', '.', '.'], #dot dot dot dot
"i" : ['.', '.'], #dot dot
"j" : ['.', '-', '-', '-'], #dot dash dash dash
"k" : ['-', '.', '-'], #dash dot dash
"l" : ['.', '-', '.', '.'], #dot dash dot dot
"m" : ['-', '-'], #dash dash
"n" : ['-', '.'], #dash dot
"o" : ['-', '-', '-'], #dash dash dash
"p" : ['.', '-', '-', '.'], #dot dash dash dot
"q" : ['-', '-', '.', '-'], #dash dash dot dash
"r" : ['.', '-', '.'], #dot dash dot
"s" : ['.', '.', '.'], #dot dot dot
"t" : ['-'], #dash
"u" : ['.', '.', '-'], #dot dot dash
"v" : ['.', '.', '.', '-'], #dot dot dot dash
"w" : ['.', '-', '-'], #dot dash dash
"x" : ['-', '.', '.', '-'], #dash dot dot dash
"y" : ['-', '.', '-', '-'], #dash dot dash dash
"z" : ['-', '-', '.', '.'], #dash dash dot dot

"1" : ['.', '-', '-', '-', '-'], #dot dash dash dash dash
"2" : ['.', '.', '-', '-', '-'], #dot dot dash dash dash
"3" : ['.', '.', '.', '-', '-'], #dot dot dot dash dash
"4" : ['.', '.', '.', '.', '-'], #dot dot dot dot dash
"5" : ['.', '.', '.', '.', '.'], #dot dot dot dot dot
"6" : ['-', '.', '.', '.', '.'], #dash dot dot dot dot
"7" : ['-', '-', '.', '.', '.'], #dash dash dot dot dot
"8" : ['-', '-', '-', '.', '.'], #dash dash dash dot dot
"9" : ['-', '-', '-', '-', '.'], #dash dash dash dash dot
"0" : ['-', '-', '-', '-', '-'], #dash dash dash dash dash

" " : [' '] #inter-word gap == 7 dots length
}


def toMorse(inString):
    out = []
    sourceText = inString.lower()
    sourceText = list(sourceText) #explode string into list of characters
    prevChar = " "

    for c in sourceText:
        if c in morseITUStandard.keys():
            if prevChar != " ":
                out += [' '] #inter-letter gap == 3 dots length
            out += morseITUStandard[c]
            prevChar = c
    return out

    

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)

    try:
        msg = sys.argv[1]

        for x in toMorse(msg):
            if x == '-':      #dash
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.4)
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.2)
            elif x == '.': #dot
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.2)
            elif x == '^': #inter-letter gap
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.1)
            elif x == ' ': #inter-word gap
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.7)
    except IndexError:
        print "USAGE: python pi-morse.py \"message\""
    finally:
        GPIO.cleanup()
