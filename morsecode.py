import RPi.GPIO as GPIO
import time
import json

DOTTIME = 0.0375
DASHTIME = 0.1125

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=23
GPIO.setup(buzzer, GPIO.OUT)

def playDotSound():
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(DOTTIME)
	GPIO.output(buzzer, GPIO.LOW)
	
def playDashSound():
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(DASHTIME)
	GPIO.output(buzzer, GPIO.LOW)

def waitDot():
	time.sleep(DOTTIME)

def waitDash():
	time.sleep(DASHTIME)

def decodeMorse(file):
	with open(file, 'r') as f:
		morseDict = json.load(f)
	return morseDict

def playMorseLetter(letter):
	codes = list(letter)
	for code in codes:
		if code == '.':
			playDotSound()
		elif code == '_':
			playDashSound()
		waitDash()

def playMorseWord(word):
	for letter in word:
		playMorseLetter(letter)
		print(letter + " ")
	waitDash()
	waitDash()
	waitDot()

def transcodeWord(word, morseDict):
	morseList = []
	for letter in word:
		morseLetter = morseDict.get(letter.lower())
		morseList.append(morseLetter)
	return morseList

def playMorseSentence(sentence):
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

