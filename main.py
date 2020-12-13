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
        robot.drive2Line(300, 3, 3)
        robot.turn2Line(150, True)
        robot.lineFollow4Time(250, 3, False)
    #============ TREADMILL =============================
    
    if True:
        robot.lineFollow2Line(200, False)
        print("Gyro Angle = ", robot.gyroSensor.angle())
        robot.turn(40, 300)
        # ------------ Checkpoint at Wheel Thing -------------
        robot.drive(2.5, 450) 
        robot.frontMotor.run(-750)
        robot.turn(0, 300) 
        robot.drive(3.0, 350)
        wait(12000)
        robot.stop()
        robot.frontMotor.stop()
        robot.turn(0, 400)
        # -------------- End of Wheel Thing ---------------------
        robot.frontMotor.run(750)
        robot.drive(5, -550)  
        robot.frontMotor.stop()
        robot.turn(18, 200)  
        robot.drive2Line(-350, 0, 0) 

    #=================== ROWING MACHINE ===================
    if True:
        robot.lineFollow2Line(350, False)
        robot.gyroSet()
        robot.turn(-90, 350)
        robot.drive(12.5, -350)
        robot.turn(-185, 350)
        #robot.rearMotor.run_time(350, 3000) #raising forklift
        robot.drive(1.2, -300) #At weigh thing
        robot.rearMotor.run_time(-750, 1500)#lowering forklift
        robot.drive(5.4, 300)
        wait(500)
    #================= WEIGHT MACHINE =====================
    if True:
        robot.rearMotor.run_time(750, 5750, Stop.COAST, False) # raise all the way up
        wait(2000)
        robot.turn(-97, 250) 
        robot.drive(12.4, -400) # at wieght machine
        robot.turn(-105,200)
        robot.rearMotor.run(-750) # lowering forklift
        wait(5000)
        robot.rearMotor.stop()
        #robot.rearMotor.run(750) # raising forklift
        robot.drive(1, 300)
        robot.turn(-130, 550)
        #robot.rearMotor.stop()
        wait(1000)

        #======== line stuff -------------------------------------

        robot.drive2Line(300, 0, 1.5, False)  # driving away from wieght machine to line 
        robot.turn2Line(550, False)
       # robot.turn(-180, 350)
       # robot.drive2Line(400, 12, 0)
        robot.lineFollow4Time(300, 3, True, False)
        #wait(2000)
        #robot.lineFollow2Line(200, True, False)
        wait(100000)
        #robot.gyroSet(-180)
       # robot.drive(8, 300) 
       # robot.turn(-215, 300)
        #robot.drive(15, 500) #near children
        #robot.turn(-270, 400)
        #robot.drive(5,300)
        #robot.turn(-225, 400)

    # #### Tested independently - will fail if run with other parts because angles are wrong ######
    # DELETE ONCE THE REGULAR SECTION IS WORKING
    if False:
        robot.drive(8, 300)
        robot.turn(-35, 300)
        robot.drive(17.5, 500)
        robot.drive(-4, 400)
        robot.turn(-90, 400)
        robot.turn(-45, 400)


    # ========== From Competition 1 ========================
    if False:
        robot.drive(23.5, -450)
        robot.turn(93, 300)
        robot.drive(20, 550) #goes under bar
        robot.turn(157, 300)
        robot.drive(20, 400)
        robot.drive(3, -300)
        robot.turn(-30, 400) #dance


def bench():
    robot.drive(36, 500, 10, 10)
    robot.drive(15, -550)

print("Gyro Angle = ", robot.gyroSensor.angle())
clock = StopWatch()
#robot.wait4Button()
#bench()
#robot.wait4Button()
dancingqueen()



print ("Time = ", clock.time())
print("Gyro Angle = ", robot.gyroSensor.angle())

#robot.rearMotor.run_time(350, 15000)
#robot.lineFollow4Time(450, 5, False)

