'''
Курс Программирование на Python — 3 Функции. Словари. Интерпретатор. Файлы. Модули.

Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей в списке известных слов, после передаётся d строк с одним словарным словом на строку, затем — количество l строк текста, после чего — l строк текста.

Программа выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы
'''
wcount = int(input())
wset = set()
for i in range(wcount):
    wset.add(input().lower())
lcount = int(input())
llist = list()
ewords = set()
for i in range(lcount):
    llist = input().split()
    for word in llist:
        if word.lower() not in wset:
            ewords.add(word)
for word in ewords:
    print(word)

# EOF