class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

bottomLeft = Point(0,0)
topRight = Point(9,9)

def countShips(corner1=bottomLeft, corner2=topRight):
    if not hasShips(corner1, corner2):
        return 0
    if corner1.x==corner2.x and corner1.y==corner2.y:
        return 1

    midX = (corner1.x + corner2.x)//2
    midY = (corner1.y + corner2.y)//2

    if corner1.x == corner2.x:
        return countShips(corner1, Point(midX,midY)) + countShips(Point(midX,midY+1),corner2)

    if corner1.y == corner2.y:
        return countShips(corner1, Point(midX,midY)) + countShips(Point(midX+1,midY),corner2)

    count = 0
    count += countShips(corner1, Point(midX,midY))
    count += countShips(Point(corner1.x,midY+1), Point(midX,corner2.y))
    count += countShips(Point(midX+1,corner1.y), Point(corner2.x,midY))
    count += countShips(Point(midX+1,midY+1), corner2)

    return count


def hasShips(corner1, corner2):
    ships = [(1,5),(2,7),(5,1),(3,1),(2,1),(8,4),(9,0),(0,9),(6,6),(5,5),(0,0)]
    for i in range(corner1.x, corner2.x+1):
        for j in range(corner1.y, corner2.y+1):
            if (i,j) in ships:
                return True
    return False


print(countShips())
