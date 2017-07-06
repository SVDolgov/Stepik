'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных
классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого
класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются.
Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в
качестве роста используется натуральное число, но при подсчёте среднего
требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера
класса (для классов с первого по одиннадцатый). Если про какой-то класс нет
информации, необходимо вывести напротив него прочерк.
'''
kdict = {(i + 1): [0, 0] for i in range(11)}
with open("3_7_5.tsv") as ifile:
    for line in ifile:
        klass, name, height = line.split('\t')
        klass = int(klass)
        kdict[klass][0] += int(height)
        kdict[klass][1] += 1
for klass, value in kdict.items():
    if kdict[klass][0] == 0:
        print(klass, '-')
    else:
        print(klass, kdict[klass][0] / kdict[klass][1])

# EOF