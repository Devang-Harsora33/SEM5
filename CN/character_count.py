f1 = []
n = int(input("Enter the size of the array:"))
for i in range(n):
    a = input("Enter the data at position " + str(i) + ": ")
    f1.append(a)
f1.insert(0, str(n+1))
result = ' '.join(f1)
print(result)
