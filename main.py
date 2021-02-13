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
        robot.turn(-10, 550, .5)
        robot.drive(4, -400)
        robot.turn(35, 550)
        robot.drive2Line(300, 4, 3)
        robot.turn2Line(150, True)
        robot.lineFollow4Time(250, 3, False)
    #===================== TREADMILL =======================
    if False:
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
        robot.drive2Line(-350, 0.5, 2.5, False) #back away from treadmill
        robot.frontMotor.stop()

    #=================== ROWING MACHINE ===================
    if False:
        robot.turn(-90, 350)
        robot.drive(13.5, -350) #going towards rowing machine  *** was (14, -350)
        robot.turn(- 185 , 350)                                   # Was (-190, 350)
        #robot.rearMotor.run_time(350, 3000) #raising forklift
        robot.drive(3.3, -300) #At weigh thing
        robot.rearMotor.run_time(-750, 1500)#lowering forklift
        robot.drive(5, 300)
        wait(500)
    #================= WEIGHT MACHINE =====================
    if False:
        robot.rearMotor.run_time(750, 5750, Stop.COAST, False) # raise all the way up
        wait(2000)
        robot.turn(-85, 250) # Currently -86  Was as low as -78
        robot.drive(11.4, -505) # at weight machine #18.4
        robot.turn(-90, 550)
        robot.drive(7, -550)
        robot.gyroSet(-90)
        wait(500)
        robot.drive(4.8, 400)
        robot.turn(-110, 200, 0.8)
        robot.rearMotor.run(-750) # lowering forklift
        wait(5000)
        robot.rearMotor.stop()
        robot.rearMotor.run_time(750, 1500, Stop.COAST, False)
        robot.drive(4.5, 300)
        robot.turn(-155, 550)
        #robot.rearMotor.stop()

    #------------------- Line Stuff -----------------------
    if False:
        robot.drive2Line(300, 0, 0, False)  # driving away from weight machine to line 
        robot.lineFollow4Time(200, 1.5, True, False)
        robot.lineFollow2Line(200, True, False)
        robot.rearMotor.run_time(-650, 1600, Stop.COAST, False)
        robot.drive(3, 250)
    
    #================== SLIDE =====================
    if False:
        robot.lineFollow2Line(300, True, False)
        robot.gyroSet(-180)
        robot.turn(-183, 400)
        robot.drive(12.9, 500)
        robot.turn(-188, 400)
        robot.rearMotor.run_time(750, 2200, Stop.COAST, False) # raising forklift
        robot.turn(-220, 100)

    #=============== COLOR BOXES ===================
    if False:
        robot.turn(-200, 500, 1)
        robot.drive2Line(300, 3, 3.5)
        robot.rearMotor.run_time(-750, 3200, Stop.COAST, False) # lowering forklift for basketball 
        robot.turn2Line(150, True)

    #============= BASKETBALL ================
    if True:
        robot.lineFollow2Line(350, False, True) # at color blocks
        robot.gyroSet(-270)
        robot.drive(2, 100) #hits color boxes
        robot.drive(6, -350)
        robot.turn(-365, 350)
        wait(2000)
        robot.drive(7.5, -350)
        robot.turn(-415, 400, 0.5) # under hoop
        wait(2000)
        robot.rearMotor.run_time(750, 6000) # raising hoop
        robot.turn(-380, 400)
        robot.drive(30, -550)

def thefinalcountdown():
    #=============== START (in base) =======================
    robot.gyroSet(0)
    #=============== PULL-UP BAR ==========================
    if True:
        robot.drive2Line(550, 5, 0)                 #drive towards first line
        robot.lineFollow4Time(200, 3, False, True)
        robot.lineFollow2Line(350, False, True)     #line follow to the line near pull-up bar
        robot.turn(75, 450)                         #turn
        robot.drive2Line(450, 0, 0)                 #drive through pull-up bar
        robot.lineFollow2Line(350, False, True)
        robot.drive(12, 550)                        #drive forward and dump blocks
        #robot.turn(75, 450)
        robot.frontMotor.run_time(350, 500)
    #=============== DANCE =======================
    if True:
        robot.drive(7, -450)                        #back up
        robot.turn(140, 450)                        #turn towards dance
        robot.drive(13, 550)                        #drive towards dance
        dancetime = StopWatch()
        while dancetime.time() < 10000:             #dance
            robot.turn(180, 350)
            robot.turn(80, 350)


def bench():
    robot.drive(16, 550)
    wait(500)
    robot.moveSteering(0, 550)
    wait(1000)
    robot.drive(15, -550)


#print("Gyro Angle = ", robot.gyroSensor.angle())
#robot.gyroCheck()
#clock = StopWatch()
robot.wait4Button()
dancingqueen()
#robot.wait4Button()
#bench()
#robot.wait4Button()
#thefinalcountdown()

robot.rearMotor.run_time(600, 5500)

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
# - Dumper for cubes
# - Routine and attachment for yellow cube
# - Attachment for pull-up