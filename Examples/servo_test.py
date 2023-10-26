import machine
import time

servo_pin = machine.Pin(5)  # Define the GPIO pin number for the servo motor
# Initialize PWM object with frequency of 50Hz
servo = machine.PWM(servo_pin) 
servo.freq(500)

# Rotate the servo motor continuously in the other direction for 5 seconds
print("setting duty to zero")
servo.duty_u16(0)  # Set the duty cycle to 0 to stop the servo motor
time.sleep(0)  # Wait for the servo to stop
print("setting duty to 32768")
servo.duty_u16(32768)  # Set the duty cycle to 50% to start the servo motor
time.sleep(0)  # Wait for the servo to start
# Stop the servo motor
print("setting duty to 1638")
# servo.duty_u16(1638)  # Set the duty cycle to 0 to stop the servo motor
servo.duty_u16(1638)  # Set the duty cycle to 0 to stop the servo motor

time.sleep(20)  # Wait for the servo to start
servo.duty_u16(0)  # Set the duty cycle to 0 to stop the servo motor
