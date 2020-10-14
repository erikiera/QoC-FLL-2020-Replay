#!/usr/bin/env pybricks-micropython
from Robot import *

robot=Robot()

if False:
    robot.drive(35, 500)
    robot.moveSteering(0, 20)
    wait (20000)
    robot.stop()
    robot.drive(8, -400)
    robot.turn(-90, 300)
    robot.drive(-50, 450)

robot.lineFollow2Line(200)


















#robot.drive(35, 500)
#robot.drive(10, 300)


#robot.drive2Line(200, 2, 0)