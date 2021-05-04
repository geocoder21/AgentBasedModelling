"""A model to create 10 agents which move around their environment,
altering its values as they go"""

# IMPORTS
import tkinter
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animate
import random
import requests
import bs4

import agentframework
import Environment


# MODEL PARAMETERS
num_sheep = 10
num_wolves = 2
iterations = 50
sheep = []
wolves = []
neighbourhood = 20


# FUNCTIONS

def update(frame_number):
    fig.clear()
    global carry_on
    sheep_left = len(sheep)

# move agents at random and get them to 'eat' environment and share stores
    for j in range(iterations):
        for i in range(sheep_left):
            random.shuffle(sheep)
            sheep[i].move()
            sheep[i].eat()
            sheep[i].share_with_neighbours(neighbourhood)

            
# move wolves at random and get them to 'eat' the agents
# update number of remaining sheep as sheep_left
        for i in range(num_wolves):
            random.shuffle(wolves)
            wolves[i].move()
            sheep_left = wolves[i].eat_sheep()
            # print(sheep_left)             # Test that sheep_left reduces
        
# plot and animate the results
# sheep coloured in white, wolves in red
    plt.ylim(0, 99)                        # y dimension limit
    plt.xlim(0, 99)                        # x dimension limit
    plt.imshow(current_environment)        # environment plot
    for i in range(sheep_left):            # agents scatter plot
        plt.scatter(sheep[i].x, sheep[i].y, color='white')
    for i in range(num_wolves):
        plt.scatter(wolves[i].x, wolves[i].y, color='red')

# run function
def run():
    create_agents()
    animation = animate.FuncAnimation(fig, update, interval=1, repeat=False, 
                                      frames=iterations)
    canvas.draw()


# create agents function
def create_agents():
    global sheep_slider
    global wolf_slider
    global num_sheep
    global num_wolves
    
    # get agent parameters from sliders
    num_sheep = sheep_slider.get()
    num_wolves = wolf_slider.get()
    
    # download y and x data from web
    # extract for use in positioning agents
    mydata = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = mydata.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    mydata_y = soup.find_all(attrs={"class": "y"})
    mydata_x = soup.find_all(attrs={"class": "x"})
    # print(mydata_y)                               # Test download of y
    # print(mydata_x)                               # Test download of x

    # Create sheep within environment, using y and x classes
    for i in range(num_sheep):
        y = int(mydata_y[i].text)
        x = int(mydata_x[i].text)
        sheep.append(agentframework.Sheep(current_environment, sheep, y, x))
        # print(y, x)                               # Test print sheep coordinates
        # print()
    
    # create wolves within environment, using y and x classes
    for i in range(num_wolves):
        y = int(mydata_y[num_sheep+i].text)
        x = int(mydata_x[num_sheep+i].text)
        wolves.append(agentframework.Wolves(sheep, y, x))
        # print(y, x)                               # Test print wolf coordinates
        


# ****************************************************************************
# MAIN PROGRAMME
# ***************************************************************************

# set up backend correctly before fig is created
matplotlib.use('TkAgg')


# create an environment for the agents
# NB update filename to use a different csv dataset
current_environment = Environment.create_environment('in.txt')

carry_on = True


# GUI code
root = tkinter.Tk()
root.wm_title("ABM Model")

# create a new figure
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
# ax.set_autoscale_on(False)

# make a canvas
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# add a menu bar to run the model
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


# add sheep slider to change number of sheep at start
sheep_slider = tkinter.Scale(root, from_ = 1, to = 20, orient=tkinter.HORIZONTAL, 
                             label="Sheep")
sheep_slider.pack(padx=5, pady=5)

# add wolf slider to change number of wolves at start
wolf_slider = tkinter.Scale(root, from_ = 1, to = 10, orient=tkinter.HORIZONTAL,
                            label="Wolves")
wolf_slider.pack(padx=5, pady=5)


# print descriptive text for user
# print("Sheep are white, wolves are red")
# print()


# application mainloop
tkinter.mainloop()  # Wait for interactions.


# doctest
# test by typing 'python model_final.py -v' in command prompt
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Write out the environment created as a file
# NB will overwrite file with same name in same directory
# update filename to prevent this
Environment.write_environment(current_environment, 'dataout.txt')
