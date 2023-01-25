import pyautogui as py
import keyboard

images = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png',
          '18.png', '19.png', '20.png', '21.png', '22.png', '23.png', '24.png', '25.png', '26.png', '27.png', '28.png', '29.png', '30.png', '31.png', '32.png', '33.png', '34.png', '35.png',
          '36.png', '37.png', '38.png', '39.png', '40.png']
continueButton = './images/continueButton.png'
positions = []
imagesToAdded = {

}
IMAGES_PATH = "./images/"
buttons = 4
def add_all_images_to_dict():
    _iter = 0
    imagesToAdded.clear()
    for image in images:
        if(_iter < buttons):
            imagesToAdded[IMAGES_PATH + image] = False
            _iter += 1
def check_all_dict_values_for_false():
    for value in imagesToAdded.values():
        if(value == False):
            return True
def click_all_positions():
    for position in positions:
        py.moveTo(position)
        py.click()    
        py.sleep(0.025)
    val = py.locateOnScreen(continueButton, confidence=0.9)
    py.moveTo(val)
    py.click()
    positions.clear()
    add_all_images_to_dict()
def find_images():
    _iter = 0
    while(check_all_dict_values_for_false()):
        #print(imagesToAdded)
        for image in images:
            if(_iter < buttons):
                if(imagesToAdded[IMAGES_PATH + image] != True):
                    target = py.locateOnScreen(IMAGES_PATH + image, confidence=0.99)
                    if(target != None):
                        x,y = py.center(target)
                        positions.append((x,y))
                        imagesToAdded[IMAGES_PATH + image] = True
                        _iter += 1
    if(all(value == True for value in imagesToAdded.values())):
        #print(positions)
        click_all_positions()
        
text = py.confirm(text="Welcome to the Chimpanzee Test AI Program. To start, go to humanbenchmark.com and click on the chimpanzee test, then press OK. to cancel, press cancel. The program can be stopped at any time by holding 'Q' on your keyboard. Enjoy!")
if(text == "OK"):
    while(True):
        start = py.locateOnScreen('./images/startButton.png')
        if(start != None or keyboard.is_pressed("f")):
            py.moveTo(start)
            py.sleep(0.005)
            py.click()
            break

    while(True):
        if(keyboard.is_pressed("q")):
            break
        add_all_images_to_dict()
        py.sleep(0.01)
        find_images()
        buttons += 1
else:
    exit()

    
