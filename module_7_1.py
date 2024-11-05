class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        a = (self.name, self.weight, self.category)

        return str(a)


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.prod_list = 0
        self.file = 0

    def get_products(self):
        self.file = open(self.__file_name, 'r')
        self.prod_list = self.file.read()
        self.file.close()
        return self.prod_list

    def add(self, *products):
        list_pord = self.get_products()
        for prod in products:
            if list_pord.find(prod.name) != -1:
                self.file = open(self.__file_name, 'a')
                self.file.write(str(f'This produkt\n'))
                self.file.close()
            else:
                self.file = open(self.__file_name, 'a')
                self.file.write(str(f'{prod} \n'))
                self.file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
s1.add(p1, p2, p3)

print(s1.get_products())

