from pyglet.graphics import Group
from pyglet.gl import glEnable, glDisable, GL_SCISSOR_TEST, glScissor

class ScissorGroup(Group):
    def __init__(self, x, y, width, height, order=0):
        super().__init__(order=order)
        self.x = x*2
        self.y = y*2    
        self.width = width * 2
        self.height = height * 2

    def set_state(self):
        glEnable(GL_SCISSOR_TEST)
        glScissor(self.x, self.y, self.width, self.height)

    def unset_state(self):
        glDisable(GL_SCISSOR_TEST)