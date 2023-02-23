import turtle

import pandas as pd

from scoreboard import Scoreboard
from get_coor import Get_coor


scoreboard=Scoreboard()
screen=turtle.Screen()
canvas = screen.getcanvas()
window = canvas.create_window((100, 100), width=200, height=100)
screen.title("US States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.tracer(0)


# def get_mouce_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouce_click_coor)

turtle.penup()

get_coor=Get_coor()
gameIsOn= True
while gameIsOn:
    correct=scoreboard.score
    userInput=screen.textinput(title=f"{correct}/50 States Correct",prompt="What's another States?",)
    coor=(0,0)
    if userInput.title()=='Exit':
        break
    if get_coor.have_available(userInput):
        scoreboard.addScore()
        coor=get_coor.get_location(userInput)
        turtle.goto(coor)
        turtle.write(userInput)
        turtle.goto((0, 0))
        screen.update()

    if scoreboard.score==50:
        gameIsOn=False


#states to learn.csv
dic={
    "Unvisted City": get_coor.all_city_list
}
df=pd.DataFrame(dic)
df.to_csv("learn.csv")












