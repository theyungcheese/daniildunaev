class technic:
    clas = "Проводная"
    warranty.period = "2 года"
    brand = "Lenovo"
    model = "GS123"
    color = "Black"
    def set(self, clas, color):
        self.clas = clas
        self.color= color
class TV(technic):
    def technic_method(self, model, color):
        self.model = model
        self.color = color
class notebook(technic):
    def technic_note(self, product, color):
        self.product = product
        self.color = color
class monitor(technic):
    def technic_monitor(self, size, color):
        self.size = size
        self.color = color
class printer(technic):
    def technic_printer(self, company, color):
        self.company = company
        self.color = color
class mikrovolnovka(technic):
    def technic_method(self, temp):
        self.temp = temp

class employee:
    def employee(self, position, color):
        self.position = position
        self.color = color

class employee:
    position = "employee"
    salary = 123456
    def eployee(self, position, salary):
        self.position = position
        self.salary = salary
class kassir(employee):
    position = "Кассир"
class manager(employee):
    position = "Менеджер"
Manager = [
    {'name': 'Nikita', 'position': "assistant"},
    {'name': 'Andrey', 'position': "manager"},
    {'name': 'Daniil', 'position': "Head master"}
]
Customer = [
    {'name': 'Stepan'},
    {'name': 'Konstantin'},
    {'name': 'Lebron'}
]
Televisor = [
    {'model': 'LG', 'price': 122354, 'quality': 42},
    {'model': 'Samsung', 'price': 42564, 'quality': 13},
    {'model': 'HP', 'price': 123548, 'quality': 22},
]

items = list()
people = list()
customer = list()


# Добавить лист с телевизорами
def create_tele_list(app_items):
    global items
    items = app_items


def create_item(model, price, quantity):
    global items
    items.append({'model': model, 'price': price, 'quality': quantity})


# Найти телевизор модели module
def read_item(model):
    global items
    myitems = list(filter(lambda x: x['model'] == model, items))
    if myitems:
        return myitems[0]
    else:
        print("no")


# Вывести список телевизоров
def read_items():
    global items
    return [item for item in items]

def read_names():
    global items
    return [item for item in items[0]]


# Добавим список менеджеров
def create_Manager_list(app_items):
    global people
    people = app_items

# Добавим список покупателей
def create_Customer_list(app_items):
    global customer
    customer = app_items


# Вывести список покупателей
def customer_list():
    global customer
    return [item for item in customer]


# Вывести список покупателей
def meneger_list():
    global people
    return [item for item in people]


# Функция, которая будет убирать телефизор, который купили
def buy_televisor(model):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['model'] == model, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]

def choice_name(choice):
    new_model = input("Введите модель телевизора: ")
    Oleg.find(new_model)
    if read_item(new_model):
        ans = input("Собираетесь ли вы его приобретать? (Да/Нет): ")
        if ans == "Да":
            Oleg.buy("dexp")
            print("Хорошего пользования ")

class cust_buy:

    def __init__(self, name):
        self.name = name

    # Найти необходимый телевизор
    def find(self, model):
        self.model = model
        if read_item(model):
            print("Он в наличии")
            return True
        else:
            print("Выберите другой")

    # купить телевизор
    def buy(self, model):
        self.model = model
        if read_item(model):
            buy_televisor(model)
            print("Он работает")
        else:
            print("К сожалению, данная модель не доступна(")



create_tele_list(Televisor)
create_Manager_list(Manager)
create_Customer_list(Customer)
# create_item("samsung", 15000, 15)
print(read_names())


name = input("Введте имя пользователя: ")
Oleg = cust_buy(name)
choice = int(input("Вы можете выбрать конкретную модель телевизора, "
               "который хотите купить, либо посмотреть список всех телевизоров(1/2): "))
if choice == 1:
    choice_name(choice)
else:
    read_names()
choice = int(input("Вы можете выбрать конкретную модель телевизора, "
               "который хотите купить, либо посмотреть список всех телевизоров(1/2): "))
if choice == 1:
    choice_name(choice)
else:
    read_names

