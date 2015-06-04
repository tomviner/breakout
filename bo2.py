from collections import namedtuple


W = 800
H = 600
RED = 200, 0, 0

ball = Rect((W/2, H/2), (30, 30))
Direction = namedtuple('Direction', 'x y')
ball_dir = Direction(1, 1)

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, RED)

def on_key_down():
    import sys
    sys.exit()


def move(ball):
    """returns a new ball at a new position
    """
    global ball_dir
    ball.move_ip(ball_dir)
    if ball.x > W or ball.x <= 0:
        ball_dir = Direction(-1 * ball_dir.x, ball_dir.y)

    if ball.y > H or ball.y <= 0:
        ball_dir = Direction(ball_dir.x, ball_dir.y * -1)


def update():
    move(ball)