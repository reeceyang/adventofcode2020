line = input()
numbers = []
sum = []
current = 0
num = 32321523
ans1 = 0
ans2 = 0
done = False

while line != "":
    if not done:
        thenum = int(line)
        numbers.append(thenum)
        current += thenum
        sum.append(current)
        for i in range(0, len(sum) - 2):
            if current - sum[i] == num:
                done = True
                index1 = i + 1
                index2 = len(sum)
                break
    line = input()

newlist = sorted(numbers[index1:index2])
print(newlist)
smallest = newlist[0]
largest = newlist[len(newlist) - 1]
print(smallest + largest)
