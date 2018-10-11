import game_framework
from pico2d import *
#import main_state

name = "PauseState"
image = None

def enter():
    global image
    image = load_image('pause.png')
    size = (50,50)
def exit():
    global image
    del(image)

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()






def draw():
    clear_canvas()
    image.draw(800/2, 600/2)
    update_canvas()

def pause():
    pass

def resume():
    pass