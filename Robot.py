#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import copysign, sin

class LightSensor(ColorSensor):
    def light():
        return sum(self.rgb())

    def white()    

class Robot():
    def __init__(self):
        self.frontMotor=Motor(Port.D)
        self.rearMotor=Motor(Port.A)
        self.leftMotor=Motor(Port.C)
        self.rightMotor=Motor(Port.B)
        self.leftSensor=ColorSensor(Port.S2)
        self.rightSensor=ColorSensor(Port.S3)
        self.gyroSensor=GyroSensor(Port.S1)

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
        rotation= distance*2*3.14*6.28
        self.rightMotor.reset_angle(0)

        if distance < 0 :
            distance = abs(distance)
            speed = -speed

        #  Loop
        while abs(self.rightMotor.angle()) < abs(rotation)  :
            # Do the gyro steering stuff
            currentDegrees=self.gyroSensor.angle()
            errorGyro=currentDegrees-startDegrees
            print(self.gyroSensor.angle())
            # Do the ramp speed stuff   
            rampSpeed=sin(abs(self.rightMotor.angle()) / rotation * 3.14)
            self.moveSteering(errorGyro*kSteering, rampSpeed * speed + copysign(20, speed))


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
        pass

    def lineFollow4Time(self, speed, time, rightSide=True):
        pass

    def turn2Line(self, speed, time=5):
        pass
    
    def drive2Line(self, speed, distanceBefore, distanceAfter):
        # Startup
        self.drive(distanceBefore, speed)
        
        # Loop
        while self.rightSensor.reflection() < 90:
            self.moveSteering(0, 70)

        # Exit
        self.drive(distanceAfter, speed)

    
    def stop(self, brake=Stop.BRAKE):
        # 3 options: Stop.BRAKE, Stop.COAST, Stop.HOLD
        self.rightMotor.stop(brake)
        self.leftMotor.stop(brake)

    


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.