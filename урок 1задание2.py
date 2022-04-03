list1 = list(range(1, 1001))
list2 = []
amount1 = 0
amount2 = 0
for i in list1:
    if i % 2 != 0:
        list2.append(i**3)
for number in list2:
    zero_sum = 0
    a = number
    while a != 0:
        zero_sum += a % 10
        a = a // 10
    if zero_sum % 7 == 0:
        amount1 += number
    number += 17
    zero_sum = 0
    a = number
    while a != 0:
        zero_sum += a % 10
        a = a // 10
    if zero_sum % 7 == 0:
        amount2 += number
print(amount1)
print(amount2)
