#!/usr/bin/env pybricks-micropython
from Robot import *

robot=Robot()

#=============== START (in base) =================
if True:
    robot.drive(26, 550)            # Drive out of base (fast)
    robot.moveSteering(3, 50)       # Push Step Counter very slowly
    wait (9000)
    robot.stop()                    # Done with Step counter
    robot.drive(4, -400)
    robot.turn(30, 300)
    robot.drive2Line(300, 4.3, 0.15)
    wait(2000)
    robot.turn2Line(150, True)
    wait(2000)
    robot.lineFollow4Time(350, 2000, False)
    robot.lineFollow2Line(200)
    wait(2000)
# ========== Checkpoint at Wheel Thing =================
if False:
    robot.lineFollow2Line(500)
    robot.frontMotor.run(-550)
    robot.drive(15, 300)
    wait(20000)


# Erik's Testing
if False:
    robot.drive2Line(150, 1, 2)
    wait(3000)
    robot.turn2Line(100)
    wait(3000)
    robot.lineFollow2Line(300)

#robot.lineFollow4Time(350, 7000, False)
#robot.drive(20, 200)