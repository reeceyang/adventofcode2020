nums = [0,1,4,13,15,12,16]

last_turn = {}
turn = 1
for i in nums:
    last_turn[i] = turn
    turn += 1

while turn <= 30000000: #this is slow but it works, just have to wait a little bit
    print("turn", turn, "checking", nums[-1])
    if nums[-1] in last_turn and last_turn[nums[-1]] != turn - 1:
        #print("spoken before")
        nums.append(turn - 1 - last_turn[nums[-1]])
        last_turn[nums[-2]] = turn - 1
    else:
        #print("new")
        last_turn[nums[-1]] = turn - 1
        nums.append(0)
    #print("added", nums[-1])
    turn += 1

print(nums[-1])
