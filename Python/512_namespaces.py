'''
Реализуйте программу, которая будет эмулировать работу с пространствами имен.
Необходимо реализовать поддержку создания пространств имен и добавление в них
переменных.
В данной задаче у каждого пространства имен есть уникальный текстовый
идентификатор – его имя.
Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем
<namespace> внутри пространства <parent>

add <namespace> <var> – добавить в пространство <namespace> переменную <var>

get <namespace> <var> – получить имя пространства, из которого будет взята
переменная <var> при запросе из пространства <namespace>, или None, если такого
пространства не существует

Sample Input: 
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b

Sample Output: 
global
None
bar
foo
'''

n = int(input())
namespaces = {'global':{'parent':'', 'vars':[]}}

def get(namespace, var):
    if namespace == '':
        return None
    elif namespaces[namespace]['vars'].count(var) > 0:
        return namespace
    else:
        return get(namespaces[namespace]['parent'], var)

for i in range(n):
    action, namespace, var = input().split()
    if action == "create":
        namespaces[namespace] = {'parent':var, 'vars':[]}
    elif action == "add":
        namespaces[namespace]['vars'].append(var)
    elif action == "get":
        print(get(namespace, var))

# EOF