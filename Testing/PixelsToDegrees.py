

def screenPixelsToDegrees(x,y,degrees,resolution):
    xAlpha = x/resolution[0]
    yAlpha = y/resolution[1]
    return(lerp(xAlpha, -degrees[0], degrees[0]), lerp(yAlpha, -degrees[1], degrees[1]))


def lerp(alpha, min, max):
    return ((max[0] - min[0]) * alpha + min[0],(max[1] - min[1]) * alpha + min[1])
