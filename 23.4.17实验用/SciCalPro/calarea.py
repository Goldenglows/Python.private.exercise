import settings

def caltriangle(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area


def calrectangle(a,b):
    area=a*b
    return area

def calcircle(r):
    area=r*r*settings.pi
    return area