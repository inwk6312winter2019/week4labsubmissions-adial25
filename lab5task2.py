import copy
class point:
    "represents a point"

class rectangle:
    """Represents a rectangle.attributes: width, height, corner."""

box = rectangle()
box.width = 100.0
box.height = 200.0
box.corner = point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


center = find_center(box)
print_point(center)


def move_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
    print(rect.width,rect.height)

move_rectangle(box,50,100)

def move_rectangle_new(rect, dwidth, dheight):
    new=copy.deepcopy(rect)
    move_rectangle(new,dwidth,dheight)
    return new

move_rectangle_new(box,50,100)