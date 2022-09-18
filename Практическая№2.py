group = {
    'dkmo-21': 'Технология разработки',
    'dkms-21': 'Разработка программных модулей',
    'dkmo -22': 'Разработка мобильных приложений',
    'dkmo -22/1': 'Тестирование программного обеспечения'
}
print( group['dkms-21'] )
for key in group.values():
    print( key )

newGroup = 'dkmo -22/2'
newDisciplineValue = 'Разработка баз данных'

if newGroup in group:
    print( 'Ok' )
    
else:
    group[ newGroup ] = newDisciplineValue

print( group )
#Задание№1
states = {
 'Астраханская область': 'RU',
 'Брянская область': 'RUU',
 'Волгоградская область': 'RUUU',
 'Белгородская область': 'RUUUU',
 'Амурская область': 'RUUUUU'
 }
cities = {
 'RUUU': 'Волгоград',
 'RUUUUU': 'Благовещенск',
 'RUU': 'Брянск'
 }

cities['RUUUU'] = 'Белгород'
cities['RU'] = 'Астрахань'


print ( ' - ' * 10)
print ( " B стране RUUUU есть город: ", cities['RUUUU'])
print (" В стране RU есть город: ", cities['RU'])

 
print ( ' - ' * 10 )
print ("Аббревиатура Амурская область : ", states['Амурская область'])
print("Абберевиатура Брянская область: ", states['Брянская область'])


print ('-' * 10 )
print ("В Амурской области есть город: ", cities[states['Амурская область']])
print ("В Брянской области есть город: ", cities[states['Брянская область']])

 
print ('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} имеет аббревиатуру {abbrev}")


print('-' * 10)
for abbrev, city in list(cities.items()):
     print(f"B стране {abbrev} есть город {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
     print(f"B стране {state} используется аббревиатура {abbrev}")
     print(f"И есть город {cities[abbrev]}")




