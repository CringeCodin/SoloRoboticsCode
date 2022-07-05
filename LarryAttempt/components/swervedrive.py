import math

from wpilib import ADXRS450_Gyro
import ctre

import constants

class SwerveModule:
    """
    Create a swerve module. __init__ takes drive motor and turn motor (TalonFXs). The drive motor drives the module, and the turn motor turns it using a PID controller.
    """
    #static methods can be called as a class (SwerveModule.method()) or as an object (flmodule.method()) but cannot access attributes
    @staticmethod
    def sensorUnitsToDegrees(su: float) -> float:
        return su * (360/2048)
    
    @staticmethod
    def degreesToSensorUnits(deg: float) -> float:
        return deg * (2048/360)

    @staticmethod
    def closestAngle(a: float, b: float) -> float:
        """
        Find the closest direction to go to get from angle a to angle b. Returns an angle in degrees.
        """
        #modulus is just so the angles are under 360. this is really b - a (difference between angles)
        direc = (b % 360) - (a % 360)
        #if distance is over 180 we can go the other way
        if abs(direc) > 180.0:
            #let's say the direc is 270. we take the inverse of 360 (taking the sign of our angle) 
            #and then add direc onto it to get our new angle
            direc = -(math.copysign(1, direc) * 360.0) + direc
        return direc

    def __init__(self, driveMotor: ctre.TalonFX, turnMotor: ctre.TalonFX):

        self.driveMotor = driveMotor
        self.turnMotor = turnMotor
        self.turnMotor.configSelectedFeedbackSensor(ctre.TalonFXFeedbackDevice.IntegratedSensor, timeoutMs=10)
        self.turnMotorIsInverted = False

    def setDirection(self, angle: float):
        """
        Change the direction the module is facing. Takes angle argument (degrees).
        """
        
        self.turnMotor.setInverted(False)
        
        pos = self.sensorUnitsToDegrees(self.turnMotor.getSelectedSensorPosition())
        optimizedAngle = self.closestAngle(pos, angle)
        
        if optimizedAngle != (angle % 360) - (pos % 360):
            angle = optimizedAngle
            self.turnMotor.setInverted(True) 
        
        self.turnMotor.set(ctre.ControlMode.Position, self.degreesToSensorUnits(angle))


    def setSpeed(self, speed):
        """
        Change the speed of the module. speed argument should be between -1.0 (backward) and 1.0 (forward)
        """
        self.driveMotor.set(ctre.ControlMode.PercentOutput, speed)

class SwerveDrive:
    """
    Swerve drive component. Now we're gaming
    """
    FLModule: SwerveModule
    BLModule: SwerveModule
    FRModule: SwerveModule
    BRModule: SwerveModule
    gyro: ADXRS450_Gyro

    def move(self, leftX, leftY, rightX):
        """
        Move the swerve drive. This doesn't actually move anything, but it 
        """
        ...
    
    def execute(self):
        ...

