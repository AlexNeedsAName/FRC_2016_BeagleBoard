

def screenPixelsToDegrees(x,y,degrees,resolution):
    xAlpha = float(x)/float(resolution[0])
    yAlpha = float(y)/float(resolution[1])
    return(lerp(xAlpha, -degrees[0], degrees[0]), lerp(yAlpha, -degrees[1], degrees[1]))


def lerp(alpha, lower, upper):
    return (upper - lower) * alpha + lower
