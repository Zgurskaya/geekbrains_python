fraza = input("Введите строку, разделяя каждое слово пробелом: ")
fraza = list(fraza.split(" "))
ind = 1
for fraza in fraza:
    print(ind, fraza[:10])
    ind += 1
