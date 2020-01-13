import RPi.GPIO as GPIO
import time
import json

# default dot and dash times (seconds)
DOTTIME = 0.0375
DASHTIME = 0.1125

# setup GPIO and make GPIO 23 output
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=23
GPIO.setup(buzzer, GPIO.OUT)

def playDotSound():
	"""
	Plays the dot sound according to specified time
	"""
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(DOTTIME)
	GPIO.output(buzzer, GPIO.LOW)
	
def playDashSound():
	"""
	Plays the dash sound accord to specified time
	"""
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(DASHTIME)
	GPIO.output(buzzer, GPIO.LOW)

def waitDot():
	"""
	Waits the specified dot sound time
	"""
	time.sleep(DOTTIME)

def waitDash():
	"""
	Waits the specified dash sound time
	"""
	time.sleep(DASHTIME)

def decodeMorse(file):
	"""
	Decodes the morse json file (eg codes.json)
	"""
	with open(file, 'r') as f:
		morseDict = json.load(f)
	return morseDict

def playMorseLetter(letter):
	"""
	Plays the morse code of a letter
	"""
	codes = list(letter)
	for code in codes:
		if code == '.':
			playDotSound()
		elif code == '_':
			playDashSound()
		waitDash()

def playMorseWord(word):
	"""
	Plays the morse code of a word
	"""
	for letter in word:
		playMorseLetter(letter)
		print(letter + " ")
	waitDash()
	waitDash()
	waitDot()

def transcodeWord(word, morseDict):
	"""
	Converts a alphabetic letter to morse code string value
	"""
	morseList = []
	for letter in word:
		morseLetter = morseDict.get(letter.lower())
		morseList.append(morseLetter)
	return morseList

def playMorseSentence(sentence):
	"""
	Plays an alphabetic sentence in morse code
	"""
	alphabetWords = sentence.split()
	morseDict = decodeMorse('codes.json')
	for word in alphabetWords:
		morseWord = transcodeWord(word, morseDict)	
		playMorseWord(morseWord)

if __name__ == '__main__':
	sentence = str(input("Please type your sentence to be converted to morse code: "))
	print(sentence)
	playMorseSentence(sentence)
	GPIO.cleanup()	

