f1 = []
n = int(input("Enter the size of the array:"))
Y = input("Enter the starting character: ")
Z = input("Enter the ending character: ")
for i in range(n):
    a = input("Enter the data at position " + str(i) + ": ")
    f1.append(a)
processed_list = []
for i in f1:
    i = i.replace(Y, f"${Y}").replace(Z, f"${Z}")
    processed_list.append(i)

processed_list.append(Z)
processed_list.insert(0,Y)
result = ' '.join(processed_list)

print(processed_list)
print(result)
