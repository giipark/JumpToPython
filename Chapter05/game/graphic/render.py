# from game.sound.echo import echo_test
from ..sound.echo import echo_test  # relative 하게 import 가능

def render_test():
    print("render")
    echo_test()
