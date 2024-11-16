from backend import *
def setUpHome():
    home = smartHome()
    while home.listLength() < 5:
        deviceChoice = input("Would you like to add a plug or a custom device? (Input: plug or custom): ")
        if deviceChoice == ("plug"):
            try:
                cRate = int(input("What consumption rate will the plug have?: "))
                plug = smartPlug(cRate)
                home.addDevice(plug)
            except ValueError:
                print("You need to input an integer")
        elif deviceChoice == ("custom"):
            smartDevice = smartAirFryer()
            home.addDevice(smartDevice)
        else:
            print("Input either plug or custom.")
    system = smartHomeSystem(home)
    system.run()
class smartHomeSystem():
    def __init__(self, home):
        self.home = home

        self.win = Tk()
        self.win.title("Smart Home")
        self.calculateWindowSize()

        self.mainframe = Frame(self.win)
        self.mainframe.grid(
            column=0,
            row=0,
        )

        self.rowLabels = []

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def toggleAllDevices(self):
        self.home.toggleAll()
        for i in range(self.home.listLength()):
            device = self.rowLabels[i]
            device.config(text = str(self.home.getSpecificDevice(i)))

    def toggleAllDevicesOff(self):
        self.home.toggleAllOff()
        for i in range(self.home.listLength()):
            device = self.rowLabels[i]
            device.config(text = str(self.home.getSpecificDevice(i)))

    def toggleButton(self, index):
        device = self.rowLabels[index]
        self.home.toggleSwitch(index)
        device.config(text = str(self.home.getSpecificDevice(index)))

    def calculateWindowSize(self):
        windowWidth = "600x"
        windowHeight = 40 * self.home.listLength()
        windowSize = windowWidth + str(windowHeight + 100)
        self.win.geometry(windowSize)

    def refreshWindow(self):

        self.win.destroy()
        self.win = Tk()
        self.win.title("Smart Home")
        self.calculateWindowSize()

        self.mainframe = Frame(self.win)
        self.mainframe.grid(
            column=0,
            row=0,
        )

        self.rowLabels = []

    def deleteRow(self, index):
        self.home.removeDevice(index)
        self.refreshWindow()
        self.createWidgets()

    def customizeDevice(self, entry, device, index):
        inputtedChoice = entry.get()
        if device.getType() == "AF":
            device.switchCookingMode(inputtedChoice)
        elif device.getType() == "P":
            device.changeConsumptionRate(inputtedChoice)
        self.rowLabels[index].config(text = str(self.home.getSpecificDevice(index)))
    def createWindow(self, title, windowType, index):
        newWindow = Toplevel(self.win)
        newWindow.title(title)
        newWindow.geometry("400x200")
        if windowType == "edit":
            editedDevice = self.home.getSpecificDevice(index)
            if editedDevice.getType() == "AF":
                Label(
                    newWindow,
                    text="You are editing an air fryer. Please input from Healthy, Defrost or Crispy.").pack()
                customOptionEntry = Entry(
                    newWindow,
                    width=20,
                )
                customOptionEntry.pack()
                entryButton = Button(
                    newWindow,
                    text="Enter",
                    command=lambda entry=customOptionEntry: self.customizeDevice(customOptionEntry, editedDevice, index),
                )
                entryButton.pack()
            elif editedDevice.getType() == "P":
                Label(newWindow,
                      text="You are editing a plug. Please input the new Consumption Rate.").pack()
                customOptionEntry = Entry(
                    newWindow,
                    width=20,
                )
                customOptionEntry.pack()
                entryButton = Button(
                    newWindow,
                    text="Enter",
                    command=lambda entry=customOptionEntry: self.customizeDevice(customOptionEntry, editedDevice, index),
                )
                entryButton.pack()

        else:
            topLabel = Label(
                newWindow,
                text="This is the adding window.",
                )
            topLabel.pack()
            choiceButton1 = Button(
                newWindow,
                text="Press to add a Plug.",
                command=lambda deviceInput="P": self.addDevice("P")
                )
            choiceButton1.pack()
            choiceButton2 = Button(
                newWindow,
                text="Press to add an Air Fryer.",
                command=lambda deviceInput="AF": self.addDevice("AF")
            )
            choiceButton2.pack()

    def addPlug(self, entry):
        cRate = entry.get()
        try:
            cRate = int(cRate)
            newPlug = smartPlug(cRate)
            newPlug = smartPlug(cRate)
            self.home.addDevice(newPlug)
            self.refreshWindow()
            self.createWidgets()
        except ValueError:
            print("You need to input an integer")

    def addAirFryer(self, entry):
        airFryerChoice = entry.get()
        newAF = smartAirFryer()
        if airFryerChoice in newAF.cookingModes:
            newAF.switchCookingMode(airFryerChoice)
            self.home.addDevice(newAF)
            self.refreshWindow()
            self.createWidgets()
        else:
            print("You have to choose from either Healthy, Defrost or Crispy.")

    def addDevice(self, deviceInput):
        addingWindow = Toplevel(self.win)
        addingWindow.title("Configuration Window")
        if deviceInput == "P":
            addingWindow.geometry("400x200")
            topLabel = Label(
                addingWindow,
                text="Configure the plug you want to add.",
            )
            topLabel.pack()
            customEntry = Entry(
                addingWindow,
                width=20
            )
            customEntry.pack()
            entryButton = Button(
                addingWindow,
                text="Enter",
                command=lambda entry=customEntry: self.addPlug(entry)
            )
            entryButton.pack()
        elif deviceInput == "AF":
            addingWindow.geometry("500x200")
            topLabel = Label(
                addingWindow,
                text="Please input a choice from Healthy, Defrost or Crispy before adding the air fryer.",
            )
            topLabel.pack()
            customEntry = Entry(
                addingWindow,
                width=20
            )
            customEntry.pack()
            entryButton = Button(
                addingWindow,
                text="Enter",
                command=lambda entry=customEntry: self.addAirFryer(entry)
            )
            entryButton.pack()


    def createWidgets(self):

        for i in range(self.home.listLength()):
            deviceMessage = Label(
                self.mainframe,
                text=str(self.home.getSpecificDevice(i))
                )
            deviceMessage.grid(column=0, row= 1 + i)
            self.rowLabels.append(deviceMessage)

            toggleButton = Button(
                self.mainframe,
                text="Toggle",
                command = lambda index=i: self.toggleButton(index),

            )
            toggleButton.grid(column=1, row= 1 + i)

            editButton = Button(
                self.mainframe,
                text="Edit",
                command = lambda index=i: self.createWindow("Edit Window", "edit", index)
            )
            editButton.grid(column=2, row= 1 + i)

            deleteButton = Button(
                self.mainframe,
                text="Delete",
                command= lambda index = i: self.deleteRow(index),
            )
            deleteButton.grid(column=3, row= 1 + i)

        turnAllButton = Button(
            self.mainframe,
            text="Turn all the devices on.",
            command= lambda: self.toggleAllDevices(),
        )
        turnAllButton.grid(
            row=0,
            column=0,
            pady=10,
        )

        turnAllOffButton = Button(
            self.mainframe,
            text="Turn all the devices off.",
            command= lambda: self.toggleAllDevicesOff(),
        )
        turnAllOffButton.grid(
            row=0,
            column=1,
            pady=10,
        )

        addButton = Button(
            self.mainframe,
            text="Add",
            command=lambda index=len(self.home.getDevices()): self.createWindow("Adding Window", "add", index)
        )
        addButton.grid(column=0, row=self.home.listLength() + 1)


#def testSystem():
#     home = smartHome()
#     plug1 = smartPlug(45)
#     plug2 = smartPlug(150)
#     custom1 = smartAirFryer()
#     custom2 = smartAirFryer()
#     custom3 = smartAirFryer()
#     plug1.toggleSwitch()
#     home.addDevice(plug1)
#     home.addDevice(plug2)
#     home.addDevice(custom1)
#     home.addDevice(custom2)
#     home.addDevice(custom3)
#
#     print(home.getDevices())
#
#     system = smartHomeSystem(home)
#     system.run()


#testSystem()
setUpHome()

