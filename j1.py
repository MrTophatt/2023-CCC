delivered = int(input(''))
collisions = int(input(''))

points = (delivered*50) - (collisions*10)

if delivered > collisions:
    points = points + 500

print(points)
