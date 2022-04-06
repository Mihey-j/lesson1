duration = int(input('Введите количество секунд: '))
if duration < 60:
    print(duration, "сек")
elif 60 <= duration <= 3600:
    m = duration // 60
    s = duration % 60
    print(m, 'мин', s, 'сек')
elif 3600 <= duration <= 86400:
    h = duration // 3600
    s_1 = duration % 3600
    m = s_1 // 60
    s = duration % 60
    print(h, 'час', m, 'мин', s, 'сек')
