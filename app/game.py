from app.window import window, pyglet

@window.event
def on_draw():
    window.clear()

def run():
    pyglet.app.run()
