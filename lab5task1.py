import math
class point:
    "represents a point"

p1=point()
p2=point()

def distance_between(a,b):
    dx=p1.x-p2.x
    dy=p1.y-p2.y
    dist=math.sqrt(dx**2+dy**2)
    print(dist)

p1.x=4
p2.x=5
p1.y=3
p2.y=4

distance_between(p1,p2)