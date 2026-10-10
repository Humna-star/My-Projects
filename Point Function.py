class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

p1 = point(27885666756, 367564578787988756454)
print(p1)