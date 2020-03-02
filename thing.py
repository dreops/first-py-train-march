binary = []
def countBits(n):
    countvar = 0
    for n in range(n,-1):
        x = n % 2
        if x == 0:
            binary = [0]
        else:
        binary = [1]
    countvar = countvar + binary[i]
    return countBits    
          