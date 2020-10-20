#!/usr/bin/env pybricks-micropython
from Robot import *

robot=Robot()

#=============== START (in base) =================
if False:
    robot.drive(35, 500)            # Drive out of base (fast)
    robot.moveSteering(0, 20)       # Push Step Counter very slowly
    wait (20000)
    robot.stop()                    # Done with Step counter
    robot.drive(8, -400)
    robot.turn(30, 300)
    robot.drive2Line(300, 5, 2)
    robot.turn2Line(250)
    robot.lineFollow2Line(200)
# ========== Checkpoint at Wheel Thing =================
#robot.lineFollow2Line(500)
#robot.frontMotor.run(-550)
#robot.drive(4, 300)
#wait(10000)

robot.lineFollow4Time(300, 3000)
