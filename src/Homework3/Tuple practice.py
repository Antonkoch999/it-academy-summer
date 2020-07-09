"""
1. Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
2. Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
3. Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
4. Создайте кортеж из одного элемента, чтобы при итерировании
   по этому элементы последовательно выводились значения 1, 2, 3.
   Убедитесь что len() исходного кортежа возвращает 1.
"""


lst = ['a', 'b', 'c']
tpl_lst = tuple(lst)
print('Task 1:', tpl_lst)

tpl = ('a', 'b', 'c')
lst_tpl = list(tpl)
print('Task 2:', lst_tpl)

a, b, c = 'a', 2, 'python'
print('Task 3:', a, b, c)

tpl_one_el = ([1, 2, 3], )
print('Task 4:', 'len tuple = ', len(tpl_one_el))
for i in tpl_one_el:
    for j in i:
        print(j)
