
def computepay(a, b) :
    if a > 40 :
        ans = 40 * b
        ans = ans + (a-40) * b * 1.5
    else :
        ans = a * b
    
    return ans
    
print(computepay(45,10))