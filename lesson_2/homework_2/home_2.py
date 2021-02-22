a = input("Введите элементы списка  через пробел a=: ").split()
for i in range(0,len(a),2):
    a[i:i+2]=a[i:i+2][::-1]
print(a)