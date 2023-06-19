class Cafe:
    def __init__(self, menu):
        self.menu = menu
        self.order_list = []
        self.order_count = 0

    def order(self, coffee, size, dessert, payment):
        if coffee not in self.menu[0]:
            print('Item not on menu!')
        elif size not in self.menu[1]:
            print('Size not available!')
        elif dessert not in self.menu[2]:
            print('Item not on menu!!')
        elif payment not in ['Cash', 'Card']:
            print('Not a valid method')
        else:
            price = self.menu[0].get(coffee) * self.menu[1].get(size) +\
                    self.menu[2].get(dessert)
            self.order_count += 1
            if dessert == 'None':
                self.order_list.append(f"Order №{self.order_count}: "
                                       f"{coffee} {size} without dessert. "
                                       f"Cost: {price} r, paid by {payment.lower()}")
            else:
                self.order_list.append(f"Order №{self.order_count}: "
                                       f"{coffee} {size} with {dessert}. "
                                       f"Cost: {price} r, paid by {payment.lower()}")

    def custom_order(self):
        custom_order_parameters = []
        for_print = ['coffee type:', 'size:',
                     'dessert (None if not interested):']
        tmp = 0
        for i in self.menu:
            print('Choose', for_print[tmp])
            tmp += 1
            print(*i, sep=', ')
            custom_order_parameters.append(input())
        print('Choose payment method: Cash or Card: ')
        custom_order_parameters.append(input())
        self.order(*custom_order_parameters)
        print('Order successful.')

    def print_list(self):
        print('\nList of orders: ')
        for i in self.order_list:
            print(i)


coffee_menu = {'Cappuccino':70, 'Americano':70, 'Latte':75}
size_list = {'0.2':0.85, '0.3':0.9, '0.4':1, '0.5':1.15}
dessert_menu = {'None':0, 'Strawberry Donut':85, 'Chocolate Donut':85, 'Chocolate Cupcake':80, 'Vanilla Cupcake':80}


full_menu = [coffee_menu, size_list, dessert_menu]
coffee_shop = Cafe(full_menu)

coffee_shop.order('Latte', '0.3', 'None', 'Card')
coffee_shop.order('Americano', '0.4', 'Chocolate Donut', 'Cash')
coffee_shop.custom_order()
coffee_shop.print_list()
