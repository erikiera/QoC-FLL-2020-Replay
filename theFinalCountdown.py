#!/usr/bin/env pybricks-micropython
from Robot import *
robot=Robot ()

def thefinalcountdown():
    #=============== START (in base) =======================
    #robot.gyroSet(0)
    #=============== PULL-UP BAR ==========================
    if True:
        robot.drive2Line(550, 5, 0)                 #drive towards first line
        robot.turn(10, 450)
        robot.lineFollow4Time(200, 3, False, True)
        robot.lineFollow2Line(350, False, True)     #line follow to the line near pull-up bar
        robot.turn(75, 450)                         #turn
        robot.drive2Line(450, 0, 0)                 #drive through pull-up bar
        robot.lineFollow2Line(350, False, True)
        robot.drive(15, 550)                        #drive forward and dump blocks
        #robot.turn(75, 450)
        robot.frontMotor.run_time(250, 1000)
    #=============== DANCE =======================
    if True:
        robot.drive(7, -450)                        #back up
        robot.turn(140, 450)                        #turn towards dance
        robot.drive(13, 550)                        #drive towards dance
        dancetime = StopWatch()
        while dancetime.time() < 10000:             #dance
            robot.turn(180, 350)
            robot.turn(80, 350)

robot.wait4Button
thefinalcountdown()
