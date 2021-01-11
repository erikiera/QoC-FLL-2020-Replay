#!/usr/bin/env pybricks-micropython
from Robot import *

robot=Robot()

def dancingqueen():
    #=============== START (in base) =================

    #============ STEP COUNTER =======================
    if True:
        robot.drive(26, 550)            # Drive out of base (fast)
        robot.moveSteering(1, 40)       # Push Step Counter very slowly
        wait (10500)
        robot.stop()                    # Done with Step counter
        robot.turn(-10, 550, .5)
        robot.drive(4, -400)
        robot.turn(30, 550)
        robot.drive2Line(300, 4, 3)
        robot.turn2Line(150, True)
        robot.lineFollow4Time(250, 3, False)
    #============ TREADMILL =============================
    if True:
        robot.lineFollow2Line(200, False)
        print("Gyro Angle = ", robot.gyroSensor.angle())
        robot.gyroSet(0)
        robot.turn(2, 550)
        # ------------ Checkpoint at Wheel Thing -------------
        robot.frontMotor.run(750)
        robot.drive(6.3, 450)
        wait(8000)
        robot.stop()
        robot.frontMotor.stop()
        robot.frontMotor.run(-750)
        # -------------- End of Wheel Thing ---------------------
        robot.turn(0, 550, .5)
        robot.drive2Line(-400, 1, 1.5, False) #back away from treadmill
        robot.frontMotor.stop()

    #=================== ROWING MACHINE ===================
    if True:
        robot.turn(-90, 350)
        robot.drive(13.5, -350) #going towards rowing machine
        robot.turn(-190, 350)
        #robot.rearMotor.run_time(350, 3000) #raising forklift
        robot.drive(3.2, -300) #At weigh thing
        robot.rearMotor.run_time(-750, 1500)#lowering forklift
        robot.drive(4.5, 300)
        wait(500)
    #================= WEIGHT MACHINE =====================
    if True:
        robot.rearMotor.run_time(750, 5750, Stop.COAST, False) # raise all the way up
        wait(2000)
        robot.turn(-78, 250) 
        robot.drive(12.4, -505) # at weight machine #18.4
        robot.turn(-90, 550)
        robot.drive(5.5, -550)
        robot.gyroSet(-90)
        wait(500)
        robot.drive(4.8, 400)
        robot.turn(-110, 200, 0.8)
        robot.rearMotor.run(-750) # lowering forklift
        wait(5000)
        robot.rearMotor.stop()
        robot.rearMotor.run_time(750, 1500, Stop.COAST, False)
        robot.drive(4.5, 300)
        robot.turn(-150, 550)
        #robot.rearMotor.stop()

    #------------------- Line Stuff -----------------------
    if True:
        robot.drive2Line(300, 0, 0, False)  # driving away from weight machine to line 
        robot.lineFollow4Time(300, 1.5, True, False)
        robot.lineFollow2Line(300, True, False)
        robot.rearMotor.run_time(-750, 1600, Stop.COAST, False)
        robot.drive(3, 300)
    
    #================== SLIDE =====================
    if True:
        robot.lineFollow2Line(300, True, False)
        robot.gyroSet(-180)
        robot.drive(12.8, 500)
        robot.rearMotor.run_time(750, 2900, Stop.COAST, False) # raising forklift
        robot.turn(-220, 100)

    #=============== COLOR BOXES ===================
    if True:
        robot.turn(-200, 500, 1)
        robot.drive2Line(300, 3, 3.5)
        robot.rearMotor.run_time(-750, 3200, Stop.COAST, False) # lowering forklift for basketball 
        robot.turn2Line(150, True)

    #============= BASKETBALL ================
    if True:
        robot.lineFollow2Line(350, False, True) # at color blocks
        robot.gyroSet(-270)
        robot.drive(3, 300) #hits color boxes
        robot.drive(5, -350)
        robot.turn(-350, 350)
        robot.drive(8.3, -350)
        robot.turn(-403, 400, 1.5) # under hoop
        robot.rearMotor.run_time(750, 5000) # raising hoop
        robot.turn(-375, 400)
        robot.drive(30, -550)


def bench():
    robot.drive(36, 500, 10, 10)
    robot.drive(15, -550)


print("Gyro Angle = ", robot.gyroSensor.angle())
#robot.gyroCheck()
clock = StopWatch()
#robot.wait4Button()
#bench()
#robot.wait4Button()
dancingqueen()


print ("Time = ", clock.time())
print("Gyro Angle = ", robot.gyroSensor.angle())



# Coach's Notes:
# SHORT-TERM:
# X Look into straightening out exit from Treadmill (changes distance to Rowing Machine)
# X Work on tire puller for Rowing Machine (maybe hitting mission model)
# X Look into changing turn/approach to Weight Machine (turn harder, farther away)
# X Make sure lift attachment can do all 4 challenges.
# MEDIUM-TERM:
# X Clean up approach to Bocchia Red/Blue
# X Start approach to Basketball
# - Build ball dropper for Basketball
# X Basketball lifting
# X Exit after basketball
# - Adjust Bench detachment for reliability
# LONG-TERM:
# - Speed adjustments
# - Straw man for last run
# - Execute last run
# - Discuss taking Slide child back to base
# - 