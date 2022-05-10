
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    
    if blueShirtHeights[0] > redShirtHeights[0]:
        # this means the tallest is the blue shirt, and all the blue shirts should be greater and therefore at the back
        for i in range(len(blueShirtHeights)):
            if blueShirtHeights[i] <= redShirtHeights[i]:
                return False
            else:
                continue
    elif blueShirtHeights[0] < redShirtHeights[0]:
        # this means the tallest is the red shirt, and all the red shirts should be greater and therefore at the back
        for i in range(len(blueShirtHeights)):
            if blueShirtHeights[i] >= redShirtHeights[i]:
                return False
            else:
                continue
    else:
        return False
    return True


def classPhotos2(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    firstRow = "RED" if redShirtHeights[0] > blueShirtHeights[0] else "BLUE"
    for i in range(len(blueShirtHeights)):
        red = redShirtHeights[i]
        blue = blueShirtHeights[i]
        
        if firstRow == "RED":
            if blue >= red:
                return False
        else:
            if red >= blue:
                return False
    return True
            

if __name__ == "__main__":
    redShirtHeights = [6, 9, 2, 4, 5]
    blueShirtHeights = [5, 8, 1, 3, 4]
