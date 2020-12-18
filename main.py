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
        robot.drive(2.9, 450) 
        robot.frontMotor.run(-750)
        robot.turn(0, 300) 
        robot.drive(3.0, 350)
        wait(12000)
        robot.stop()
        robot.frontMotor.stop()
        robot.turn(0, 400)
        # -------------- End of Wheel Thing ---------------------
        robot.frontMotor.run(750)
        robot.drive(5, -550)  #back away from treadmill
        robot.frontMotor.stop()

    #=================== ROWING MACHINE ===================
    if True:
        robot.turn(-90, 350)
        robot.drive(11.5, -350) #going up towards rowing machine
        robot.turn(-185, 350)
        #robot.rearMotor.run_time(350, 3000) #raising forklift
        robot.drive(1.7, -300) #At weigh thing
        robot.rearMotor.run_time(-750, 1500)#lowering forklift
        robot.drive(5, 300)
        wait(500)
    #================= WEIGHT MACHINE =====================
    if True:
        robot.rearMotor.run_time(750, 5750, Stop.COAST, False) # raise all the way up
        wait(2000)
        robot.turn(-85, 250) 
        robot.drive(18.4, -505) # at weight machine
        robot.gyroSet(-90)
        wait(500)
        robot.drive(4.5, 400)
        robot.turn(-105, 200)
        robot.rearMotor.run(-750) # lowering forklift
        wait(5000)
        robot.rearMotor.stop()
        robot.drive(5, 300)
        robot.turn(-155, 550)
        #robot.rearMotor.stop()

        #------------------- Line Stuff -----------------------
    if True:
        robot.drive2Line(300, 0, 0, False)  # driving away from weight machine to line 
        robot.lineFollow4Time(300, 3, True, False)
    
        #================== SLIDE =====================
    if True:
        robot.lineFollow2Line(200, True, False)
        robot.gyroSet(-180)
        robot.drive(13, 500)
        robot.rearMotor.run_time(750, 3100, Stop.COAST, False) # raising forklift
        robot.turn(-220, 75)
        wait(5000)




def bench():
    robot.drive(36, 500, 10, 10)
    robot.drive(15, -550)

def erikTest():
    # ================= STEP COUNTER ============================
    if True:
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
        robot.lineFollow2Line(300, False)
        print("Gyro Angle = ", robot.gyroSensor.angle())
        robot.turn(40, 300)
        # ------------ Checkpoint at Wheel Thing -------------
        robot.drive(3, 450) 
        robot.frontMotor.run(-800)
        robot.turn(2, 300) 
        robot.drive(2.8, 350)
        wait(12000)
        robot.stop()
        robot.frontMotor.stop()
        robot.turn(0, 400)
        # -------------- End of Wheel Thing ---------------------
        robot.frontMotor.run(750)
        #robot.drive(5, -550)  
        robot.turn(0, 300)  
        robot.drive2Line(-400, 0, 0, False) 
        robot.frontMotor.stop()
        robot.drive(-1, 200)
    #=================== ROWING MACHINE ===================
    if True:
        #robot.gyroSet()
        robot.turn(-90, 350)
        robot.drive(11.0, -350)
        robot.turn(-185, 350)
        robot.drive(1.2, -300) #At weigh thing
        robot.rearMotor.run_time(-750, 1200)#lowering forklift
        robot.drive(5.2, 300)
        wait(200)
    #================= WEIGHT MACHINE =====================
    if True:
        robot.rearMotor.run_time(750, 5750, Stop.COAST, False) # raise all the way up
        wait(2000)
        robot.turn(-87, 250) 
        robot.drive(20, -500) # at wieght machine
        robot.gyroSet(-90)
        wait(500)
        robot.drive(5.5, 400) # at wieght machine
        robot.turn(-105, 200)
        robot.rearMotor.run(-750) # lowering forklift
        wait(5000)
        robot.rearMotor.stop()

        # ================== DRIVE TO THE LINE AND LINE FOLLOW ==================
        robot.drive(3, 300)
        robot.turn(-160, 550)
        #robot.rearMotor.stop()
        robot.drive2Line(400, 6, 0, False)
        robot.turn(-170, 300)
        robot.lineFollow4Time(300, 1.7, True, False)
        wait(3000)
        robot.lineFollow2Line(300, True, False)
        robot.turn(-210, 400)
        robot.drive(20, 400)
        robot.stop(Stop.HOLD)



print("Gyro Angle = ", robot.gyroSensor.angle())
clock = StopWatch()
#robot.wait4Button()
#bench()
#robot.wait4Button()
dancingqueen()
#erikTest()


print ("Time = ", clock.time())
print("Gyro Angle = ", robot.gyroSensor.angle())

#robot.rearMotor.run_time(350, 15000)
#robot.lineFollow4Time(450, 5, False)


