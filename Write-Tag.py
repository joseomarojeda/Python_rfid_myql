import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('Ingresa Texto:')
        print("Coloca tu tag cerca del lector")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()
Footer
