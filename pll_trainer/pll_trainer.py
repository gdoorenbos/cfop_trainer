import random
import Tkinter as tk
from PIL import Image, ImageTk

NUM_PLLS = 21

random_pll_nums = random.sample(range(1, NUM_PLLS+1), NUM_PLLS)

for i in range(NUM_PLLS):
    imageFile = 'images/pll' + '%02d' % random_pll_nums[i] + '.GIF'
    # print(imageFile)

    root = tk.Tk()
    root.title('PLL ' + str(i+1))

    # pick an image file you have .bmp  .jpg  .gif.  .png
    # load the file and covert it to a Tkinter image object
    image1 = ImageTk.PhotoImage(Image.open(imageFile).resize((250,250)))

    # make the root window the size of the image
    root.geometry("%dx%d+%d+%d" % (image1.width(), image1.height(), 500, 300))

    # root has no image argument, so use a label as a panel
    panel1 = tk.Label(root, image=image1)
    panel1.pack(side='top', fill='both', expand='yes')

    # put a button on the image panel to test it
    # button2 = tk.Button(panel1, text='button2')
    # button2.pack(side='top')

    # save the panel's image from 'garbage collection'
    panel1.image = image1

    # start the event loop
    root.mainloop()
