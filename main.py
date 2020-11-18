#!/usr/bin/env pybricks-micropython
from Robot import *

robot=Robot()

def dancingqueen():
    #=============== START (in base) =================

    #============ STEP COUNTER =======================
    if False:
        robot.drive(26, 550)            # Drive out of base (fast)
        robot.moveSteering(1, 40)       # Push Step Counter very slowly
        wait (10500)
        robot.stop()                    # Done with Step counter
        robot.drive(4, -400)
        robot.turn(40, 300)
        robot.drive2Line(300, 3, 2)
        robot.turn2Line(150, True)
    #============ TREADMILL =============================
    if True:
        robot.lineFollow4Time(250, 3, False)
        robot.lineFollow2Line(200, False)
        robot.turn(15, 200)
    # ------------ Checkpoint at Wheel Thing -------------
        robot.frontMotor.run(-550)
        robot.drive(4.5, 250)
        robot.turn(5, 200)
        wait(1000)
        robot.turn(-5, 300, 8)
        wait(16000)
        robot.stop()
        robot.frontMotor.stop()
    # -------------- End of Wheel Thing ---------------------
        robot.frontMotor.run(550)
        robot.drive(15, -250)
        robot.frontMotor.stop()
        robot.turn(-25, 200)
        robot.drive2Line(350, 0, 0)
        robot.turn(-5, 350)
        robot.lineFollow2Line(350, False)
        robot.gyroSet()
        robot.turn(-90, 350)
        robot.drive(8.5, -350)
        robot.turn(-180, 350)




    # ========== ROWING MACHINE ========================
    if False:





        robot.drive(23.5, -450)
        robot.turn(93, 300)
        robot.drive(20, 550) #goes under bar
        robot.turn(157, 300)
        robot.drive(20, 400)
        robot.drive(3, -300)
        robot.turn(-30, 400) #dance


def bench():
    robot.drive(36, 375, 10, 10)
    robot.drive(15, -550)

#robot.wait4Button()
#bench()
robot.wait4Button()
dancingqueen()


