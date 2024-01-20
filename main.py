import pgzrun

WIDTH = 640
HEIGHT = 480

target1 = Actor('target_red1')
target1.x = WIDTH / 2
target1.y = HEIGHT / 2

duck_target_brown = Actor('duck_target_brown')
duck_target_brown.x = 200
duck_target_brown.y = 300

duck_yellow = Actor('duck_yellow')
duck_yellow.x = 200
duck_yellow.y = 200


rifle = Actor('rifle')
rifle.y = HEIGHT


cursor = Actor('crosshair_white_large')
def on_mouse_move(pos):
    rifle.left = pos[0]
    cursor.pos = pos

def on_mouse_down():
    if cursor.colliderect(target1):
        target1.left = WIDTH


def update():
    target1.x -= 1
    duck_target_brown.x += 1
    duck_yellow.x += 1

    if target1.right < 0:
        target1.left = WIDTH
    if duck_target_brown.right > WIDTH:
        duck_target_brown.left = 0
    if duck_yellow.right > WIDTH:
        duck_yellow.right = 0

def draw():
    screen.clear()
    target1.draw()
    duck_target_brown.draw()
    duck_yellow.draw()
    rifle.draw()
    cursor.draw()





pgzrun.go()