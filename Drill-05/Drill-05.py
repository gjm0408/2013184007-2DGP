from pico2d import *
import math

open_canvas()


character = load_image('character.png')


def move_00():
    pass

def move_01():
    x , y = 203 , 535
    clear_canvas_now()
    character.draw_now(x,y)


def move_02():
    x , y = 203, 535
    while x <132 or y <243:
        clear_canvas_now()
        character.draw_now(x,y)
        x += 1
        y += 1
        delay(0.01)



def move_03():
    pass

def move_04():
    pass

def move_05():
    pass

def move_06():
    pass

def move_07():
    pass

def move_08():
    pass

def move_09():
    pass

def move_10():
    pass

while True:
    move_00()
    move_01()
    move_02()
    move_03()
    move_04()
    move_05()
    move_06()
    move_07()
    move_08()
    move_09()
    move_10()



close_canvas()
