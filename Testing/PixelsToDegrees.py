

def screenPixelsToDegrees(x,y,params):
    res = params[1]
    degs = params[0]
    x = x - res[0]/2
    y = y - res[1]/2
    x = x/res[0]
    y = y/res[1]
    return(x * degs[0], y * degs[1])

