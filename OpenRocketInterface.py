#!/usr/bin/python
import jpype
from config import JAR_PATH as classpath
from config import JVM as jvm
try:
   fh = open(classpath)
except IOError, ex:
   print "Caught the IOError:\n    ", ex
   print "Verify the path to openrocket.jar in config.py"
   quit()
try:
   fh = open(jvm)
except IOError, ex:
   print "Caught the IOError:\n    ", ex
   print "Verify the path to the jvm in config.py"
   quit()

class OpenRocketInterface(object):
    def __init__(self):
        jpype.startJVM(jvm, "-Djava.class.path=%s" % classpath)
        SwingStartup = jpype.JClass('net.sf.openrocket.startup.SwingStartup') 
        SwingStartup.initializeLogging()

#        package = jpype.JPackage('net').sf.openrocket.startup
#        OpenRocketAPI = package.OpenRocketAPI
        openRocketAPIClass = 'net.sf.openrocket.startup.OpenRocketAPI'
        try:
            OpenRocketAPI = jpype.JClass(openRocketAPIClass)
        except jpype.JavaException, ex:
            if ex.message() == "Class " + openRocketAPIClass + " not found":
                print "Caught the runtime exception:\n     ", ex.message()
                print "Ensure that you are using a version of OpenRocket with this class"
            else:
                print "Caught the runtime exception:\n     ", ex.message()
            quit()
        self.apiInstance = OpenRocketAPI()
    def GetTimeStep(self):
        return self.apiInstance.GetTimeStep()
    def cleanup(self):
        jpype.shutdownJVM()
    def LoadRocket(self, rocketname, index=0):
	print rocketname
        self.apiInstance.LoadRocket(jpype.JString(rocketname))#, int(index))
    def StartSimulation(self):
        self.apiInstance.StartSimulation()
    def GetVelocity(self):
	x = self.apiInstance.GetVelocityX()
	y = self.apiInstance.GetVelocityY()
	z = self.apiInstance.GetVelocityZ()
        return (x,y,z)
    def RunSimulation(self):
        self.apiInstance.RunSimulation()
    def IsSimulationLoopRunning(self):
        return self.apiInstance.IsSimulationLoopRunning()
    def IsSimulationStagesRunning(self):
        return self.apiInstance.IsSimulationStagesRunning()
    def SimulationStep(self, timestep=None):
        if timestep != None:
            return self.apiInstance.SimulationStep(timestep)
        return self.apiInstance.SimulationStep()
    def StagesStep(self):
        return self.apiInstance.StagesStep()

    def getDeploymentVelocity(self):
    	return self.apiInstance.getDeploymentVelocity()