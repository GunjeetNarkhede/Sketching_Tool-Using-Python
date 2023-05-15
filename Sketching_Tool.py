"""Main purpose of this program is to create a sketch art work from an image.
User should paste the path of image involved in the space provided in dialouge box (without using quotes).
This python program will then take the image and create its sketch and return it instantly.
This python program will save the sketch image in a file named "sketch.png"."""

from tkinter import *
# The tkinter library is imported and used to create the GUI for the program
from PIL import Image
# The PIL library is used for handling image file
import cv2
# The cv2 is used in creation of sketch
import tkinter.font as font

window = Tk()
# we created  object window to use for the program

window.title('  ' * 110 + 'Alpha Coders')
# The title for the dialouge box is specified
Label(window, text="SKETCHING TOOL", bg='#CDFF8F', font=("Bradley Hand ITC", 100)).pack()

# the specification of the dialoge window is now given
window.geometry('500x500')
window.config(bg='#CDFF8F')

# we created a canvas to place our various object
canvas1 = Canvas(window, bg='#CDFF8F',highlightthickness=0, width=700, height=300)
canvas1.pack()

def reset():
    """this function is use to reset the value the entry box """
    var = StringVar(window)
    var.set('')
    entry1.config(textvariable=var)


var = StringVar(window)
var.set('')

paste=Label(text='Paste the image path here (without using quotes)',font=('Algerian bold',20), fg='black', bg='#CDFF8F')
canvas1.create_window(350,100, window=paste)
# the paste is a variable to show the instruction
entry1 = Entry(window, width=100, borderwidth=5, textvariable=var )
canvas1.create_window(350, 130, window=entry1)
# entry1 is an entry box created to take the input from user i.e. the path of image

def imageconverter():
    path = entry1.get()
    # path is the data we get from user
    # the path is still string to use it further we need to convert it in raw string
    for i in range(0,len(path)):
        # for loop is used to change the path
        if path[i]=="\\":
            path=path[0:i]+'/'+path[i+1:]

    image = cv2.imread(path)
    ''' image will read the file
      To convert the image the file under goes a predefined sequence of step to get the final product
      the steps are as below '''
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # converts image to gray scale
    invert = cv2.bitwise_not(grey_img)
    # this invert the gray image formed
    blur = cv2.GaussianBlur(invert, (25, 25), 0)
    # we now blur the inverted gray image
    invertedblur = cv2.bitwise_not(blur)
    # now we invert the inverted gray image
    sketch = cv2.divide(grey_img, invertedblur, scale=220)
    # now the pencil image is finished
    cv2.imwrite("sketch.png", sketch)
    # the image is then saved as a image filed name sketch

    img = Image.open("sketch.png")
    img.show()
    #this will open the image file

myFont= font.Font(family='Helvetica',size='10' ,weight='bold')

button1 = Button(text='Submit', command=imageconverter, height=2,font=myFont, width=10, borderwidth=4, foreground='white', background='#3399ff')
canvas1.create_window(300, 180, window=button1)
# this will crete the submit button which will run the program

button2 = Button(text='Reset', command=reset,font=myFont, height=2, width=10, borderwidth=4, foreground='white', background='#B30000')
canvas1.create_window(400, 180, window=button2)
# the reset button is created, it will reset the program


window.mainloop()