
def getScreenParams(topLeft,topRight,bottomLeft,bottomRight,resolution):
    return(topLeft,topRight,bottomLeft,bottomRight,resolution)


def screenPixelsToDegrees(x,y,params):
    tl = params[0]
    tr = params[1]
    bl = params[2]
    br = params[3]
    res = params[4]
    xAlpha = float(x)/res[0]
    yAlpha = float(y)/res[1]
    return lerp(lerp(bl,br,xAlpha),lerp(tl,tr,xAlpha),yAlpha)


def lerp(min,max,alpha):
    return ((max[0] - min[0]) * alpha + min[0],(max[1] - min[1]) * alpha + min[1])
