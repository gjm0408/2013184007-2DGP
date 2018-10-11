import game_framework
from pico2d import *

name = "TitleState"
image = None


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del(image)


import main_state

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_State(main_state)


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()






import title_state

def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        game_framework.change_state(title_state)
        delay(0.01)
        logo_time += 0.01


def pause():
    pass


def resume():
    pass






