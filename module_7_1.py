# Домашнее задание по теме "Режимы открытия файлов"
# Задача "Учёт товаров"

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products_list.txt'

    def get_products(self):
        file = open(self.__file_name, 'r+')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        list = open(self.__file_name, 'a')
        products_list = self.get_products()
        for product in products:
            if product.name in products_list:
                print(f'Продукт {product.name} есть в ассортименте магазина')
            else:
                list.write(str(product) + '\n')
        list.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('peach', 3.6, 'fruit')
p3 = Product('Tomato', 5.7, 'Vegetables')
p4 = Product('Cherry', 3.8, 'Berry')

print(p2)

s1.add(p3, p1, p2, p4)

print(p4)
