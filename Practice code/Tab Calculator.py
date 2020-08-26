class Tab:

    menu= {
        'shawarma':70,
        'pepsi':20,
        'garlic':35,
        'falafel':60,
        'burger':100,
        'kudo': 75
    }

    def __init__(self):
        self.total=0
        self.items=[]

    def add(self,item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, tax, service):
        tax =(tax/100)*self.total
        service=(service/100)*self.total
        total=self.total + tax + service

        for item in self.items:
            print(f'{item} Rs{self.menu[item]}')
        
        print(f'{"total"} rs{total:.2f}')