W = 800
H = 600
RED = 200, 0, 0

ball = Rect((W/2, H/2), (30, 30))


def draw():
    screen.draw.filled_rect(ball, RED)

def on_key_down():
    import sys
    sys.exit()