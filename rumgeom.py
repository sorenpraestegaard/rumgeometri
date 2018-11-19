import math

class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def connect(cls, x1,y1,z1, x2,y2,z2):
        '''
        Returns a new vector from two points.
        '''
        return cls(x2-x1, y2-y1, z2-z1)

    @classmethod
    def fromPoint(cls, p: Point):
        '''
        Returns a new vector from a point
        '''
        return cls(p.x, p.y, p.z)

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)




class Line():
    def __init__(self, p0, d):
        self.p0 = p0
        self.d = d

    '''
    Factory methods
    '''
    @classmethod
    def createNew(cls, x0, y0, z0, a, b, c):
        '''
        Creates a new Line from a point and a direction vector
        '''
        p0 = Vector(x0, y0, z0)
        d = Vector(a,b,c)
        return Line(p0, d)

    @classmethod
    def createTwoPoints(cls,x1,y1,z1,x2,y2,z2):
        '''
        Creaates a new Line from two points on the line
        '''
        d = Vector(x2-x1, y2-y1, z2-z1)
        p0 = Vector(x1,y1,z1)
        return Line(p0, d)

    def point(self, t: (float,int) = 0) -> Point:
        '''
        Return a point on the line, from a given parameter
        '''
        if not isinstance(t, (float, int)):
            raise TypeError('Parameter is not a valid number')
        p = Vector.fromPoint(self.p0)
        s = scale(t, self.d)
        return add(p,s)

    def __str__(self):
        return "(x,y,z) = ({}, {}, {}) + t*({}, {}, {})".format(self.p0.x, self.p0.y, self.p0.z, self.d.x, self.d.y, self.d.z)

class Plane():
    '''
    The class describes a plane in spaceself.

    It is created by a point and to direction vectors
    or by three points.

    Attributes
    ----------
    p0 : Vector(x,y,z), where (x,y,z) is a point on the Plane
    d1 : A direction vector for the plane.
    d2 : Another direction vector for the plane. Can not be perpendicular to d1

    Factory methods
    -------
    createNew(x0, y0, z0, a1, b1, c1, a2, b2, c2)
        Returns a plane through (x0,y0,z0) with
        the direction vectors (a1,b1,c1)^T and (a2,b2,c2)^T

    createThreePoints(x1, y1, z1, x2, y2, z2, x3, y3, z3)
        Returns a plane through the three points
        (x1,y1,z1), (x2,y2,z2) and (x3,y3,z3)


    normal()
        Returns a normal vector to the plane.
        The normal will be a unit vector.
    '''

    def __init__(self, p0, d1, d2):
        self.p0 = p0
        self.d1 = d1
        self.d2 = d2

    '''
    Factory methods
    '''
    @classmethod
    def createNew(cls, x0, y0, z0, a1, b1, c1, a2, b2, c2):
        '''
        Creates a new Plane from a point and two direction vectors
        '''
        p0 = Point(x0, y0, z0)
        d1 = Vector(a1,b1,c1)
        d2 = Vector(a2,b2,c2)
        return cls(p0, d1, d2)

    @classmethod
    def createThreePoints(cls, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        '''
        Creaates a new Line from two points on the line
        '''
        d = np.array([x2-x1, y2-y1, z2-z1])
        p0 = np.array([x1,y1,z1])
        return cls(p0, d)

    def normal(self) -> Vector:
        '''
        Returns a normal unit vector to the plane
        by crossing the two direction vectors
        '''
        return normalize(cross(self.d1, self.d2))

    def isInPlane(self, p) -> bool:
        '''
        Returns True if the point is in the plane,
        and False otherwise.
        '''
        #Testing for zero is done with math.isclose, to avoid rounding/floating point errors.
        if math.isclose(math.fabs(dot(self.normal(), Vector.fromPoint(p))),0):
            return True
        else:
            return False

    def point(self, t: (float,int) = 0, s: (float, int) = 0) -> Vector:
        '''
        Returns a point on the plane, from two given parameters
        '''
        p = Vector.fromPoint(self.p0)
        s1 = scale(t, self.d1)
        s2 = scale(s, self.d2)
        return
        return add(add(p,s1), s2)



def scale(s: (float, int), v: Vector) -> Vector:
    '''
    Returns a version of v scaled by s.
    '''
    return Vector(v.x * s, v.y * s, v.z * s)


def normalize(v: Vector) -> Vector:
    '''
    Returns a unit-vector in the direction v
    '''
    if v.length() > 0.000001:
        s = 1/v.length()
        return Vector(v.x * s, v.y * s, v.z * s)
    else:
        return Vector(0,0,0)


def cross(v1: Vector, v2: Vector) -> Vector:
    '''
    Returns the cross product of v1 and v2
    '''
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Vector(x,y,z)

def add(v1: Vector, v2: Vector) -> Vector:
    '''
    Adds the two vectors v1 and v2, and returns their sum
    '''
    return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)


def dot(v1: Vector, v2: Vector) -> float:
    '''
    Returns the inner product (dot-product)
    of v1 and v2
    '''
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z


def angle(v1: Vector, v2: Vector) -> float:
    '''
    Returns the angle in degrees between v1 and v2
    '''
    return math.degrees(math.acos(dot(v1,v2)/(v1.length()*v2.length())))

def distancePointPlane(p: Point, a: Plane) -> float:
    #The distance between the point and the plane is
    # the absolute value of the dot product between
    # the unit normal vector of the plane, and the projection
    # of a vector connecting the point to the plane, onto that unit
    # normal vectors
    return math.fabs(dot(a.normal(), Vector.connect(p.x, p.y, p.z, a.p0.x, a.p0.y, a.p0.z)))

def intersect(l: Line, p: Plane) -> Point:
    '''
    Calculates the intersection between a Line and a Plane.
    Returns None if the two arguments are parallel.
    '''
    if math.isclose(dot(l.d,p.normal()), 0):
        #If the line direction is perpendicular to the plane normal,
        # the line and plane must be parallel.
        return None
    else:
        #There exists a parameter t, which makes
        # p.isInPlane(l.point(t)) == 0
        #Let's find it.
        #Initial guess
        t = 5
        step = 0.1
        done = p.isInPlane(l.point(t))
        c = 0
        while not done:
            d = distancePointPlane(l.point(t), p)
            delta = d - distancePointPlane(l.point(t + step), p)
            if delta > 0:
                #We are going the right way!
                pass
            else:
                #Turn around
                step *= -1
            if math.fabs(delta) > math.fabs(l.d.length()*step):
                step += 0.1*d
            else:
                step += 0.1*d
            t += step
            c += 1
            #print(c,t, step, d)

            done = p.isInPlane(l.point(t)) or d < 0.00001
            if c > 10000:
                done = True
        return l.point(t)

l = Line.createNew(-10,-10,-10,1,2,3)
p = Plane.createNew(1,4,67,0,1,0,0,0,1)
print(p.point(1,3))
v1 = Vector(1,0,0)
v2 = Vector(0,1,0)
print(p.normal())
print(p.isInPlane(Point(0,1,0)))
print(angle(Vector(1,0,0), Vector(1,-1,1)))
pip = intersect(l, p)
print("Intersect siger at {} ligger i planen.".format(pip))
print(distancePointPlane(pip, p))
print(p.isInPlane(pip))
print(p.isInPlane(Vector(1,12,23)))
