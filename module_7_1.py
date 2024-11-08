from pprint import pprint
class Product:
    def __init__(self, name, weight , category):
        self.name = name
        self.weight  = weight
        self.category = category

    def __str__(self):
            str_product = f'{self.name}, {self.weight}, {self.category}'
            return str_product


class Shop:
    __file_name = 'products.txt'
    file = open(__file_name, 'w')
    file.write(f'Potato, 50.5, Vegetables\n'
                'Spaghetti, 3.4, Groceries\n'
                'Potato, 5.5, Vegetables')
    file.close()




    def get_products(self):
            file = open(self.__file_name, 'r')
            prod_str = file.read()
            file.close()
            return prod_str


    def add(self, *products):

            for i in products:
                if self.get_products().find(f'{i.name},{i.weight}, {i.category}') ==+1:
                    file = open(self.__file_name, 'a')
                    file.write(f'{i}\n')
                    file.close()
            else:
                print(f'Продукт {i.name}, {i.weight}, {i.category} уже есть в магазине')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
print(p1)
print(p2)
print(p3)

print(p2)

s1.add(p1)
s1.add(p2)
s1.add(p3)

print(s1.get_products())