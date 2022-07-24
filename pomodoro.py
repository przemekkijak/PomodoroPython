from time import sleep
import os
from datetime import timedelta
from win10toast_persist import ToastNotifier
import keyboard

def displayNotification(title, messageContent):
    ToastNotifier().show_toast(title, messageContent)


def startCounter(time, currentPhaseName):
    os.system("cls")
    input("Press enter to start " + currentPhaseName)
    for i in range(time, 0, -1):
        os.system("cls")
        print(currentPhaseName)
        minutesAndSeconds = timedelta(seconds = i)
        print('Time left: ', minutesAndSeconds, '(Press CTRL+F5 to skip current phase)')
        sleep(1)
        if keyboard.is_pressed('CTRL') and keyboard.is_pressed('F5'):
            break
    
def main():
    currentShortBreaks = 0

    pomodoroTime = int(input("Podaj czas pracy (minuty): ")) * 60
    shortBreakTime = int(input("Podaj czas krotkiej przerwy (minuty): ")) * 60 
    longBreakTime = int(input("Podaj czas dlugiej przerwy (minuty): ")) * 60
    maxShortBreaks = int(input("Podaj ilosc krotkich przerw: ")) * 60
    
    while True:
        startCounter(pomodoroTime, "Work time")
        displayNotification("Work time is over!", "Take a break and refill your glass of water :)")
        if currentShortBreaks >= maxShortBreaks:
            currentShortBreaks = 0
            startCounter(longBreakTime, "Long break")
            displayNotification("Long break is over!", "Close your eyes for a mintue and let them rest before work")
        else:
            currentShortBreaks += 1
            startCounter(shortBreakTime, "Short break")
            displayNotification("Short break is over!", "Let your eyes rest before work, take a look through window")



if __name__ == "__main__":
    main()
