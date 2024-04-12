mKey = [11,0,1,2,3,4,5,6,7,8,9,10]
months = [31,28,31,30,31,30,31,31,30,31,30,31]

def monthsToDays(nomip):
    total = 0
    prevMonth = 5 #code for the current month is the number of the prev month
    for i in range(nomip):
        total += months[prevMonth]
        prevMonth = mKey[prevMonth]
    return total

he = monthsToDays(21) + 9 #9 days past the 10th
we = monthsToDays((12*3)+6) - 11 - 3

print(he)
print(we)
print(he/we)
x = he
k = we

while x/k < 0.5:
    x += 1
    k += 1

print(x-he)
