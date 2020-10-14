#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import copysign, sin
from pybricks.iodevices import Ev3devSensor
from os import path


class LightSensor(ColorSensor):
    black = 20
    white = 80
    line = 50

    def __init__(self, port, low = 10, high = 120):
        super().__init__(port)
        self.black = low + (high-low)*.2
        self.white = low + (high-low)*.8
        self.line = low + (high-low)*.5

    def light(self):
        return sum(self.rgb())

    def isWhite(self):
        if self.light()>=self.white:
            return True
        else:
            return False

    def isBlack(self):
        if self.light()<=self.black:
            return True
        else:
            return False

    def waitForWhite(self):
        while not self.isWhite():
            pass

    def waitForBlack(self):
        while not self.isBlack():
            pass

    def waitForLine(self):
        self.waitForWhite()
        self.waitForBlack()
    
class Robot():
    def __init__(self):
        self.frontMotor=Motor(Port.D)
        self.rearMotor=Motor(Port.A)
        self.leftMotor=Motor(Port.C)
        self.rightMotor=Motor(Port.B)

        if path.exists('calibrate.py'):
            import calibrate
            self.leftSensor=LightSensor(Port.S3, calibrate.leftLow, calibrate.leftHigh)
            self.rightSensor=LightSensor(Port.S2, calibrate.rightLow, calibrate.rightHigh)

        else: 
            self.leftSensor=LightSensor(Port.S3, 10, 105)
            self.rightSensor=LightSensor(Port.S2, 20, 160)

        self.gyroSensor=GyroSensor(Port.S1)
        self.gyroSensor.reset_angle(0)
        self.testSensor = Ev3devSensor(Port.S3)

    def calibrate(self):
        rightHigh = 40
        rightLow = 70
        leftHigh = 40
        leftLow = 70

        timer = StopWatch()
        self.moveSteering(0, 125)
        while timer.time() < 5000:
            if self.rightSensor.light() > rightHigh:
                rightHigh = self.rightSensor.light()
            if self.rightSensor.light() < rightLow:
                rightLow = self.rightSensor.light()
            if self.leftSensor.light() > leftHigh:
                leftHigh = self.leftSensor.light()
            if self.leftSensor.light() < leftLow:
                leftLow = self.leftSensor.light()
        self.stop()
        # write results to file
        with open('calibrate.py', 'w') as myFile:
            myFile.write('leftLow = ')
            myFile.write(str(leftLow))
            myFile.write('\nrightLow = ', rightLow)
            myFile.write(str(rightLow))
            myFile.write('\nleftHigh = ', leftHigh)
            myFile.write(str(leftHigh))
            myFile.write('\nrightHigh = ', rightHigh)
            myFile.write(str(rightHigh))
        
    def moveSteering(self, steering, speed):
        leftMotorSpeed = speed * min(1, 0.02 * steering + 1)
        rightMotorSpeed = speed * min (1, -0.02 * steering + 1)
        self.leftMotor.run(leftMotorSpeed)
        self.rightMotor.run(rightMotorSpeed)

    def drive(self, distance, speed, time=8):
        # Startup for gyro
        kSteering=5     # Steering coefficient
        startDegrees=self.gyroSensor.angle()
        # Startup for ramp speed
        if distance < 0 :
            distance = abs(distance)
            speed = -speed
        rotation= distance*2*3.14*6.28
        self.rightMotor.reset_angle(0)
        #  Loop
        while abs(self.rightMotor.angle()) < abs(rotation)  :
            # Do the gyro steering stuff
            currentDegrees=self.gyroSensor.angle()
            errorGyro=currentDegrees-startDegrees
            # Do the ramp speed stuff   
            rampSpeed=sin(abs(self.rightMotor.angle()) / rotation * 3.14)
            self.moveSteering(errorGyro*kSteering*copysign(1, speed), rampSpeed * speed + copysign(20, speed))
        # Exit
        self.stop()

    def turn(self, angle, speed, time=5):
        # Startup
        steering = 100
        kTurn=0.01
        offset = 20
        timer = StopWatch()   
        # Loop
        while (abs(self.gyroSensor.angle() - angle) > 2)  & (timer.time() < time * 1000):
            error = self.gyroSensor.angle() - angle
            #if error > 0 : 
            #    steering = 100
            #else:
            #    steering = -100
            self.moveSteering(steering, speed * error * kTurn + copysign(offset,error))
        # Exit
        self.stop()

    def lineFollow2Line(self, speed, rightSide=True, rightStop=True):
        # Loop
        while not self.leftSensor.isWhite():
            error = self.rightSensor.line - self.rightSensor.light()
            correction = error * 0.3
            self.moveSteering(correction, speed)
        self.stop()

    def lineFollow4Time(self, speed, time, rightSide=True):
        pass

    def turn2Line(self, speed, time=5):
        self.moveSteering(100,speed)
        self.rightSensor.waitForLine()
        self.stop()
    
    def drive2Line(self, speed, distanceBefore, distanceAfter):
        # Startup
        self.drive(distanceBefore, speed)

        # Loop
        #while self.rightSensor.rgb() < 90:
        #    self.moveSteering(0, 70)
        # Start Driving
        self.moveSteering(0, 70)
        # execute function wait until we detect a line
        self.rightSensor.waitForLine()
        self.stop()

        # Exit
        self.drive(distanceAfter, speed)

    def stop(self, brake=Stop.BRAKE):
        # 3 options: Stop.BRAKE, Stop.COAST, Stop.HOLD
        self.rightMotor.stop(brake)
        self.leftMotor.stop(brake)








