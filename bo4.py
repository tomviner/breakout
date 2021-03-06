from collections import namedtuple
import sys


W = 800
H = 600
RED = 200, 0, 0
BLUE = 0, 0, 200

ball = Rect((W/2, H/2), (30, 30))
Direction = namedtuple('Direction', 'x y')
ball_dir = Direction(5, -5)

bat = Rect((W/2, 0.96 * H), (150, 15))

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, RED)
    screen.draw.filled_rect(bat, RED)

def on_key_down():
    sys.exit()

def on_mouse_move(pos):
    x, y = pos
    bat.center = (x, bat.center[1])

def move(ball):
    """returns a new ball at a new position
    """
    global ball_dir
    ball.move_ip(ball_dir)

    if ball.x > W or ball.x <= 0:
        ball_dir = Direction(-1 * ball_dir.x, ball_dir.y)

    if ball.y <= 0:
        ball_dir = Direction(ball_dir.x, ball_dir.y * -1)

    if ball.colliderect(bat):
        ball_dir = Direction(ball_dir.x, - abs(ball_dir.y))


    if ball.y > H:
        sys.exit()



def update():
    move(ball)
