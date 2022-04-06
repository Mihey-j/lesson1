list_price1 = [57.8, 46.51, 97, 14.81, 29.64, 79, 20, 54.91, 10.08, 19.22, 15.40]
list_price2 = []
for price in list_price1:
    r = int(price)
    kk = round((price - r) * 100)
    list_price2.append(f"{r} руб {kk:02d} коп")
print(', '.join(list_price2))
id1 = id(list_price1)
list_price1.sort()
print(list_price1)
print(id(list_price1) == id1)
list_price3 = sorted(list_price1, reverse=True)
print(sorted(list_price3[:5]))