#ПРИМЕРЫ
def get_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Julia', 'Chernova')
print(musician)
def greet_user(userDepartment,userProf,userGroup):
    print(f" {userDepartment.title()}")
    print(f" {userProf.title()}")
    print(f" {userGroup.title()}")

#Упражнение№1
def make_shirt(size,message):
    print("size: " + size)
    print("message: " + message)

make_shirt('large','Hello World!')
make_shirt(size = 'large',message = 'Hello World!')

#Упражнение№2
def make_shirt(size = 'large',font = 'I love Python'):
    print("size: " + size)
    print("font: " + font)

make_shirt()
make_shirt(size = 'middle')
make_shirt(size = 'small',font = 'Hello World')

#Упражнение№3
def greet_user():
    print("ФСПО 'Отделение Связь и телекоммуникации'")
    print("Специальность: Прикладная информатика")
    print("Группа: ДКЕО-41")
greet_user()

