#get the lane stuff
laneSize = int(input())
lane1 = input().replace(' ', '')
lane2 = input().replace(' ', '')

#set variables
tape = 0
direction = 1

#the logic
for i in range(laneSize):
    if lane1[i] == '1': #add 3 to tape if triangle is wet (lane 1)
        tape = tape+3
        if lane1[i-1] == '1' and i>0: #takes away 2 tape if there is a wet triangle next to a wet triangle (lane 1)
            tape = tape-2

    direction = direction*-1 #change direction
    if lane2[i] == '1': #add 3 to tape if triangle is wet (lane 2)
        tape = tape+3
        if lane2[i-1] == '1' and i>0: #takes away 2 tape if there is a wet triangle next to a wet triangle (lane 2)
            tape = tape-2
        if direction == -1 and lane1[i] == '1': #checks if above triangle is facing up and wet
            tape = tape-2

print(tape)
