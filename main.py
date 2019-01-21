import numpy as np
import rumgeom
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def showPlane(p : rumgeom.Plane):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(-10, 10, 0.25)
    Y = np.arange(-10, 10, 0.25)
    X, Y = np.meshgrid(X, Y)
    zs = np.array([p.getZCoord(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    surf = ax.plot_surface(X, Y, Z,
                       linewidth=0, antialiased=False, alpha=0.3)

    #Linje
    l = rumgeom.Line.createNew(0,1,5,1,1,-0.5)
    X = np.linspace(-10, 10, 100)
    Y = [l.getXPoint(x).y for x in X]
    Z = [l.getXPoint(x).z for x in X]
    ax.plot(X,Y,Z, label='Linje')

    #Skæringspunkt
    p = rumgeom.intersect(l,p)
    ax.scatter(p.x, p.y, p.z+1, c='r')
    ax.scatter(p.x, p.y, p.z-1, c='r')
    ax.scatter(p.x, p.y, p.z, c='g')

    plt.show()




'''
l = Line.createNew(-10,-10,-10,1,2,3)
p = Plane.createNew(1,4,67,1,2,2,-1,2,1)
pip = intersect(l, p)
print("Intersect siger at {} ligger i planen.".format(pip))
print(distancePointPlane(pip, p))
print(p.isInPlane(pip))
'''
print(rumgeom.Plane.createNew.__doc__)
p1 = rumgeom.Point(2,3,-1)
v1 = rumgeom.Vector.fromPoint(p1)
v1 = rumgeom.Vector.connect(3,2,1,5,3,-1)
print(v1.length())

v2 = rumgeom.Vector.fromPoint(rumgeom.Point(4,1,1))
print(rumgeom.dot(v1,v2))

p = rumgeom.Plane.createNew(0,0,0,1,0,0,1,1,0.5)
showPlane(p)
