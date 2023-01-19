import pyautogui as py
import keyboard
images = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png',
          '18.png', '19.png', '20.png', '21.png', '22.png', '23.png', '24.png', '25.png', '26.png', '27.png', '28.png', '29.png', '30.png', '31.png', '32.png', '33.png', '34.png', '35.png',
          '36.png', '37.png', '38.png', '39.png', '40.png']
continueButton = 'continueButton.png'
positions = []
imagesToAdded = {

}
buttons = 4
def AddAllImagesToDict():
    iter = 0
    imagesToAdded.clear()
    for image in images:
        if(iter < buttons):
            imagesToAdded[image] = False
            iter += 1
def CheckAllDictValuesForFalse():
    for value in imagesToAdded.values():
        if(value == False):
            return True
def ClickAllPositions():
    for position in positions:
        py.moveTo(position)
        py.click()    
        py.sleep(0.025)
    next = py.locateOnScreen(continueButton, confidence=0.9)
    py.moveTo(next)
    py.click()
    positions.clear()
    AddAllImagesToDict()
def FindImages():
    iter = 0
    while(CheckAllDictValuesForFalse()):
        #print(imagesToAdded)
        for image in images:
            if(iter < buttons):
                if(imagesToAdded[image] != True):
                    target = py.locateOnScreen(image, confidence=0.99)
                    if(target != None):
                        x,y = py.center(target)
                        positions.append((x,y))
                        imagesToAdded[image] = True
                        iter += 1
    if(all(value == True for value in imagesToAdded.values())):
        #print(positions)
        ClickAllPositions()
        
        
while(True):
    start = py.locateOnScreen('startButton.png')
    if(start != None or keyboard.is_pressed("f")):
        py.moveTo(start)
        py.sleep(0.005)
        py.click()
        break

while(True):
    if(keyboard.is_pressed("q")):
        break
    AddAllImagesToDict()
    py.sleep(0.01)
    FindImages()
    buttons += 1

    
