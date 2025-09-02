import tkinter as tk
from tkinter import filedialog, simpledialog
import cv2
from PIL import Image, ImageTk
import numpy as np

img ='0'
saveim='1'
def openfile():
    global img
    img = cv2.imread(filedialog.askopenfilename())
    show(img,"original")


def grayscale():
    global img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show(gray,"grayscale")

def point():
    global img

    kernel =np.float32([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])
    show(cv2.filter2D(img, -1, kernel),"point")





def horizontalline():
    global img

    kernel =np.float32([
        [-1, -1, -1],
        [2,  2, 2],
        [-1, -1, -1]
    ])

    show(cv2.filter2D(img, -1, kernel),"horizontalline")



def verticalline():
    global img

    kernel =np.float32([
        [-1, 2, -1],
        [-1,  2, -1],
        [-1, 2, -1]
    ])


    show(  cv2.filter2D(img, -1, kernel),"verticalline")






def plus45line():
    global img

    kernel =np.float32([
        [-1, -1, 2],
        [-1,  2, -1],
        [2, -1, -1]
    ])


    show(cv2.filter2D(img, -1, kernel),"plus45line")






def negative45line():
    global img
    kernel =np.float32([
        [2, -1, -1],
        [-1,  2, -1],
        [-1, -1, 2]
    ])


    show(cv2.filter2D(img, -1, kernel),"negative45line")




def edgedetectionvertical():
    global img
    kernel =np.float32([
        [-1, -2, -1],
        [0,  0, 0],
        [1, 2, 1]
    ])


    show(cv2.filter2D(img, -1, kernel),"edgedetectionvertical")

def edgedetectionhorizontal():
    global img
    kernel =np.float32([
        [-1, 0, 1],
        [-2,  0, 2],
        [-1, 0, 1]
    ])


    show(cv2.filter2D(img, -1, kernel),"edgedetectionhorizontal")



def edgedetectionnegative45():
    global img
    kernel =np.float32([
        [0, 1, 2],
        [-1,  0, 1],
        [-2, -1, 0]
    ])


    show(cv2.filter2D(img, -1, kernel),"edgedetectionnegative45")



def edgedetectionplus45():
    global img
    kernel =np.float32([
        [-2, -1, 0],
        [-1,  0, 1],
        [0, 1, 2]
    ])


    show(cv2.filter2D(img, -1, kernel),"edgedetectionplus45")


def log():
    global img
    kernel = np.float32([
        [0, 0, -1, 0, 0],
        [0, -1, -2, -1, 0],
        [-1, -2, 16, -2, -1],
        [0, -1, -2, -1, 0],
        [0, 0, -1, 0, 0]
    ])


    show(cv2.filter2D(img, -1, kernel),"log")

def laplacian():
    global img
    kernel = np.float32([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1,0]
    ])

    show(cv2.filter2D(img, -1, kernel),"laplacian")


def threshold():
    global img
    input = simpledialog.askstring("Input", "The value of the threshold:")
    if input:
        _, threshold = cv2.threshold(img, int(input), 255, cv2.THRESH_BINARY)

    show(threshold,"threshold")



def saveimg():
    global saveim, nameimg
    if isinstance(saveim, np.ndarray):
        filename = nameimg + ".jpg"
        cv2.imwrite(filename, saveim)
        print(f" successfully as {filename}.")

    else:
        print("error. It's a", type(saveim))




def customfilter():
    global img

    root = tk.Tk()
    root.withdraw()


    dimensions = simpledialog.askstring("Input", "Enter matrix dimensions (ex: 3x3):")
    values = simpledialog.askstring("Input", "Enter matrix values, separated by commas(ex: -1,-1,-1,-1,8,-1,-1,-1,-1):")


    root.destroy()

    if dimensions and values:

        rows, cols = map(int, dimensions.split('x'))
        matrix_list = list(map(float, values.split(',')))


        if len(matrix_list) == rows * cols:
            matrix = np.float32(matrix_list).reshape(rows, cols)
            filtered_image = cv2.filter2D(img, -1, matrix)
            show(filtered_image, "Filtered Image")
        else:
            print("Error: Matrix size and values do not match.")
    else:
        print("Error: Missing input.")





    show(filtered_image,"customfilter")

def show(image,name):
    global imgnew,saveim,nameimg ,canvas
    saveim=image
    nameimg=name
    cv2.imshow("hi",image)
    cv2.waitKey(1)




def mainwindow():
    global canvas
    welcomewindow.destroy()
    window = tk.Tk()
    window.geometry('1000x100')



    buttons = [
        {"text": "Open Image", "command": openfile},
        {"text": "Convert to Grayscale", "command": grayscale},
        {"text": "Point Detection", "command": point},
        {"text": "Horizontal Line", "command": horizontalline},
        {"text": "Vertical Line", "command": verticalline},
        {"text": "+45 Line", "command": plus45line},
        {"text": "-45 Line", "command": negative45line},
        {"text": "edge detection vertical", "command": edgedetectionvertical},
        {"text": "edge detection horizontal", "command": edgedetectionhorizontal},
        {"text": "edge detection -45", "command": edgedetectionnegative45},
        {"text": "edge detection +45", "command": edgedetectionplus45},
        {"text": "custom filter", "command": customfilter},
        {"text": "log", "command": log},
        {"text": "laplacian", "command": laplacian},
        {"text": "threshold", "command": threshold},
        {"text": "saveimg", "command": saveimg},

    ]

    top = buttons[:8]
    bottom = buttons[8:16]

    topf = tk.Frame(window, bg='#607274')
    topf.pack(side='top', fill='x')

    bottomf = tk.Frame(window, bg='#607274')
    bottomf.pack(side='bottom', fill='x')


    for button in top:
        B = tk.Button(topf, text=button["text"], command=button["command"], borderwidth=8, relief="raised", padx=5, pady=2, bg='#FAEED1', fg='#607274')
        B.pack(side='left', padx=10, pady=5)


    for button in bottom:
        B = tk.Button(bottomf, text=button["text"], command=button["command"], borderwidth=8, relief="raised", padx=5, pady=2, bg='#FAEED1', fg='#607274')
        B.pack(side='left', padx=10, pady=5)

    window.mainloop()






welcomewindow = tk.Tk()
welcomewindow.geometry('1100x300')

welcomewindow.configure(bg='#607274')

test1="|Point Detection|Horizontal Line|Vertical Line|+45 Line|-45 Line|edge detection vertical|edge detection horizontal|"
test2="|edge detection -45|edge detection +45|custom filter|laplacian of gaussian|laplacian|threshold|Convert to Grayscal|"
welcomelabel = tk.Label(welcomewindow,text="Digital Image Processing that Apply all segmentation filters",font=('Helvetica', 16),bg='#607274',fg='#FAEED1')
welcomelabel.pack(pady=20)
welcomelabel1 = tk.Label(welcomewindow,text=test1,font=('Helvetica', 16),bg='#607274',fg='#FAEED1')
welcomelabel1.pack(pady=20)
welcomelabel2 = tk.Label(welcomewindow,text=test2,font=('Helvetica', 16),bg='#607274',fg='#FAEED1')
welcomelabel2.pack(pady=20)
startbutton = tk.Button(welcomewindow, text="Start",command=mainwindow,borderwidth=8, relief="raised", padx=30, pady=10, bg='#FAEED1', fg='#607274',font=('Helvetica', 15))
startbutton.pack(pady=20)


welcomewindow.mainloop()













































