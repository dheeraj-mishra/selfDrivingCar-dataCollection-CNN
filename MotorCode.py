import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor:
    def __init__(self, EnableA, In1A, In2A, EnableB, In1B, In2B):
        self.EnableA = EnableA
        self.In1A = In1A
        self.In2A = In2A
        self.EnableB = EnableB
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.EnableA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnableB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnableA, 60)
        self.pwmA.start(0)
        self.pwmB = GPIO.PWM(self.EnableB, 100)
        self.pwmB.start(0);

    def move(self, speed=0.5, turn=0, t=0):
        speed *= 100
        turn *= 100
        leftSpeed = speed - turn
        rightSpeed = speed + turn
        if leftSpeed > 100:
            leftSpeed = 100
        elif leftSpeed < -100:
            leftSpeed = -100

        if rightSpeed > 100:
            rightSpeed = 100
        elif rightSpeed < -100:
            rightSpeed = -100

        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))

        if leftSpeed > 0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)

        if rightSpeed > 0:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.HIGH)
        sleep(t)

    def stop(self, t=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        sleep(t)


def main():
    motor.move(0.6, 0, 2)
    motor.stop(2)
    motor.move(-0.6, 0, 2)
    motor.stop(2)


if __name__ == '__main__':
    motor = Motor(5, 6, 26, 23, 24, 25)
    main()
