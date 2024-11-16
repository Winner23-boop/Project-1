from tkinter import *

class smartPlug():

    def __init__(self, cRate):
        self.switchedOn = "F"
        self.consumptionRate = cRate

    def getType(self):
        return "P"

    def toggleSwitch(self):
        if self.switchedOn == "F":
            self.switchedOn = "T"
        else:
            self.switchedOn = "F"

    def getSwitchState(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def changeConsumptionRate(self,cRate):
        try:
            cRate = int(cRate)
            self.consumptionRate = cRate
        except ValueError:
            print("You need to input an integer.")

    def __str__(self):
        if self.switchedOn == "F":
            output = "Plug: Off, "
        else:
            output = "Plug: On, "
        output += f"Consumption: {self.consumptionRate}"
        return output

class smartAirFryer():

    def __init__(self):
        self.switchedOn = "F"
        self.cookingModes = ["Healthy", "Defrost", "Crispy"]
        self.currentMode = self.cookingModes[0]

    def getType(self):
        return "AF"

    def toggleSwitch(self):
        if self.switchedOn == "F":
            self.switchedOn = "T"
        else:
            self.switchedOn = "F"

    def getSwitchState(self):
        return self.switchedOn

    def getCurrentMode(self):
        return self.currentMode

    def switchCookingMode(self, cookingModeInput):
        if cookingModeInput in self.cookingModes:
            self.currentMode = cookingModeInput
        else:
            print("The desired cooking mode is not an option. Pick from Healthy, Defrost or Crispy.")

    def __str__(self):
        if self.switchedOn == "F":
            output = "Air Fryer: Off "
        else:
            output = "Air Fryer: On "
        output += f"Mode: {self.currentMode}."
        return output

class smartHome():

    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices

    def getSpecificDevice(self, index):
        return self.devices[index]

    def removeDevice(self, index):
        del self.devices[index]

    def addDevice(self, deviceInput):
        self.devices.append(deviceInput)

    def toggleSwitch(self, index):
        (self.devices[index]).toggleSwitch()

    def toggleAll(self):
        for i in range(len(self.devices)):
            if self.devices[i].getSwitchState() == "F":
                (self.devices[i]).toggleSwitch()
            else:
                pass
    
    def toggleAllOff(self):
        for i in range(len(self.devices)):
            if self.devices[i].getSwitchState() == "T":
                (self.devices[i]).toggleSwitch()
            else:
                pass
            
    def listLength(self):
        return len(self.devices)
    
    def printDevices(self):
        for i in range(len(self.devices)):
            print(self.devices[i])
        return("")


def testSmartPlug():
    plug = smartPlug(45)
    plug.toggleSwitch()
    print(plug.getSwitchState())
    print(plug.getConsumptionRate())
    print(plug)

def testSmartAirFryer():
    airfryer = smartAirFryer()
    print(airfryer.getSwitchState())
    airfryer.toggleSwitch()
    print(airfryer.getSwitchState())
    print(airfryer.getCurrentMode())
    airfryer.switchCookingMode("Not Crispy")
    print(airfryer.getCurrentMode())
    airfryer.switchCookingMode("Crispy")
    print(airfryer.getCurrentMode())
    print(airfryer)

def testSmartHome():
    smarthome = smartHome()
    smartplug1 = smartPlug(45)
    smartplug2 = smartPlug(45)
    customDevice = smartAirFryer()
    smartplug1.toggleSwitch()
    smartplug1.changeConsumptionRate(150)
    smartplug2.changeConsumptionRate(25)
    customDevice.switchCookingMode("Defrost")
    smarthome.addDevice(smartplug1)
    smarthome.addDevice(smartplug2)
    smarthome.addDevice(customDevice)
    print(smarthome.printDevices())
    smarthome.toggleAll()
    print(smarthome.printDevices())
    smarthome.removeDevice(1)
    print(smarthome.printDevices())