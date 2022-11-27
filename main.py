import os,keyboard

def clearScreen() :
    if os.name == 'nt' :
        os.system("cls")
    else :
        os.system("clear")

class table :
    def __init__(self) :
        self.number = int(input("Enter the number till which you want to display the tables: "))
        self.current = 1;
        self.exit = False

    def printTable(self) :
        for i in range(1,self.number+1) :
            for j in range(1,11):
                print("{} x {} = {}".format(i,j,i*j))

    def printTable1(self) :
        clearScreen()

        for j in range(1,11):
            print("{} x {} = {}".format(self.current,j,self.current*j))

        print()
        if self.current != 1 :
            print("Press Left arrow to go to previous table")
        if self.current != self.number :
            print("Press Right arrow to go to next table")
        print("Press Escape key to quit")

    def leftPress(self) :
        if(self.current > 1) :
            self.current -= 1
            self.printTable1()

    def rightPress(self) :
        if(self.current < self.number) :
            self.current += 1
            self.printTable1()

    def quit(self) :
        self.exit = True

    def mainLoop(self) :
        keyboard.on_press_key("left arrow",lambda _ : self.leftPress())
        keyboard.on_press_key("right arrow",lambda _ : self.rightPress())
        keyboard.on_press_key("esc",lambda _ : self.quit())
        self.printTable1()
        while (not self.exit) :
            continue

clearScreen()
t = table()

t.mainLoop()
