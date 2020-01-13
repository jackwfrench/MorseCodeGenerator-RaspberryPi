# MorseCodeGenerator-RaspberryPi
A morse code text to sound generator for a raspberry pi connected piezo buzzer.

## Motivation 
Got really bored doing software projects and thought it would be 
interesting to dive into some simple hardware projects, especially 
ones that include technological history.

## GPIO and Hardware configuration
Connect GPIO pin 23 (pin 16) to the positive terminal of a piezo buzzer and ground (pin 6, 9, 14 ... etc) to negative terminal of the buzzer.

## Running the generator 
To run the morse code generator simply
```
cd MorseCodeGenerator-RaspberryPi
sudo python3 morsecode.py
```
Enter alphabetic text then press enter.

## License 
This project is licensed under the MIT License - Read more at [LICENSE.md](./LICENSE.md)

