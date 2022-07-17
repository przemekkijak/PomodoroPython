from time import sleep
import os
from datetime import timedelta
import winsound

def startCounter(time, currentPhaseName):
    os.system("cls")
    input("Press enter to start " + currentPhaseName)
    for i in range(time, 0, -1):
        os.system("cls")
        print(currentPhaseName)
        minutesAndSeconds = timedelta(seconds = i)
        print('Time left: ', minutesAndSeconds)
        sleep(1)
    winsound.Beep(500, 800)
    

def main():
    currentShortBreaks = 0

    pomodoroTime = int(input("Podaj czas pracy (minuty): "))
    shortBreakTime = int(input("Podaj czas krotkiej przerwy (minuty): ")) 
    longBreakTime = int(input("Podaj czas dlugiej przerwy (minuty): "))
    maxShortBreaks = int(input("Podaj ilosc krotkich przerw: "))
    
    while True:
        startCounter(pomodoroTime, "Work time")
        if currentShortBreaks >= maxShortBreaks:
            currentShortBreaks = 0
            startCounter(longBreakTime, "Long break")
        else:
            currentShortBreaks += 1
            startCounter(shortBreakTime, "Short break")


if __name__ == "__main__":
    main()
