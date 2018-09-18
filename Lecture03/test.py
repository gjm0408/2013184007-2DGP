from pico2d import *
import math




open_canvas()

grass = load_image('grass.png')

character = load_image('character.png')


x =0

y =0

x2 = 750

y2 = 540

x3 = 20
y3 = 90

while (True):

    
    if(x < 750):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x = x + 2
            delay(0.01)
            

    elif(x == 750 and y < 450):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y+90)
            y = y + 2
            delay(0.01)

    elif(x2 > 20):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x2, y2)
            x2 = x2 - 2
            delay(0.01)

    elif(x2 == 20 and y2>90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x2, y2)
            y2 = y2 - 2
            delay(0.01)
            
    
    elif(x3 < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x3, 90)
            x3 = x3 + 2
            delay(0.01)

    elif(1):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x3+400*math.sin(math.radians(C)),(y3*3)-200*math.cos(math.radians(C)))
        x3 = x3 + 2
        y3 = y3 + 2
        delay(0.01)
            

    


   


        
close_canvas()
