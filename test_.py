list = []
n = 5
sum = 0
def countBits(n):
    x = bin(n)
    list = x
    for i in range(2,len(list)):
        sum = sum + list[i]
        countBits = sum
    return countBits

print(countBits(n))

    