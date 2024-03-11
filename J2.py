pepperAmount = int(input(''))
SHU = 0
PepperSHU = 0

for i in range(pepperAmount) :
    pepper = input('')
    if pepper == 'Poblano':
        PepperSHU = 1500
    if pepper == 'Mirasol':
        PepperSHU = 6000
    if pepper == 'Serrano':
        PepperSHU = 15500
    if pepper == 'Cayenne':
        PepperSHU = 40000
    if pepper == 'Thai':
        PepperSHU = 75000
    if pepper == 'Habanero':
        PepperSHU = 125000

    SHU = SHU + PepperSHU

print(SHU)
