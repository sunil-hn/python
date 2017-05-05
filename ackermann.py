def ackermann(m, n):
    if (m == 0):
        return (n + 1)
    elif ((m > 0) & (n ==0)):
        num = ackermann(m-1, 1)
        return num
    elif ((m > 0) & (n > 0)):
        num = ackermann(m-1, ackermann(m, n-1))
        return num


print ("Enter m")
m = input()
print("Enter n")
n = input()
result = ackermann(int(m), int(n))
print("Result:", int(result))
