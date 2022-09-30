```python
# Простой словарь
fio={'firstName':'nina','secondName':'Alexandrovna','lastName':'chekalina'}
```


```python
# Доступ к значению
print("Полное имя/фамилия: " + fio['firstName'] + fio['lastName'])
```

    Полное имя/фамилия: ninachekalina
    


```python
# Перебор всех пар ключ-значение
fio={'firstName':'nina','secondName':'Alexandrovna','lastName':'chekalina','date':'2022-09-10','period':14}
for name,s in fio.items():
 print(name + ':' + str(s) )
```

    firstName:nina
    secondName:Alexandrovna
    lastName:chekalina
    date:2022-09-10
    period:14
    


```python
# преобразую представление в список, списокявляется последовательностью кортежей (ключ, значение) - то, что получает dict для создания словаря
list(fio.items())
```




    [('firstName', 'nina'),
     ('secondName', 'Alexandrovna'),
     ('lastName', 'chekalina'),
     ('date', '2022-09-10'),
     ('period', 14),
     ('occupation', 'programming')]




```python
# функция sorted возвращает новый отсортированный список 
for name in sorted(fio.items()):
    print(name)
```

    ('date', '2022-09-10')
    ('firstName', 'nina')
    ('lastName', 'chekalina')
    ('occupation', 'programming')
    ('period', 14)
    ('secondName', 'Alexandrovna')
    


```python
# противоположный порядок вывода
for name in sorted(fio.keys(),
                   reverse=True):
     print(name)
   
  
 
```

    secondName
    period
    occupation
    lastName
    firstName
    date
    


```python
for name in sorted(fio.items(),
                   reverse=True):
     print(name)
```

    ('secondName', 'Alexandrovna')
    ('period', 14)
    ('occupation', 'programming')
    ('lastName', 'chekalina')
    ('firstName', 'nina')
    ('date', '2022-09-10')
    


```python
# Перебираем все ключи
fio={'firstName':'nina','secondName':'Alexandrovna','lastName':'chekalina','date':'2022-09-10','period':14}
for name in fio.keys():
 print(name + '')
```

    firstName
    secondName
    lastName
    date
    period
    


```python
# Перебор всех значений
# Результат вызова .values также является представлением. Он отражает
# # # текущее состояние значений, находящихся в словаре
for number in fio.values():
 print(str(number) + ' ' + 'статус:по совместительству')
```

    nina статус:по совместительству
    Alexandrovna статус:по совместительству
    chekalina статус:по совместительству
    2022-09-10 статус:по совместительству
    14 статус:по совместительству
    


```python
# Для вставки значений в словарь используют индексные операции:
fio['occupation'] = 'programming'
```


```python
# поиск индексной операцией:
fio['occupation']
```




    'programming'




```python
# Метод .get словаря получает значение, соответствующее ключу
staff = fio.get('Должность', 'преподаватель')
staff
 
```




    'преподаватель'




```python
# операции подсчета
import collections
count = collections.Counter(['Чернова', 'Семенов', 'Ветров', 'Чернова'])
count

```




    Counter({'Чернова': 2, 'Семенов': 1, 'Ветров': 1})




```python
# только Чернова
count['Чернова']

```



