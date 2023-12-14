class puu:
    def __init__(self, number):
        self.vasak = None
        self.parem = None
        self.number = number

    def insert(self, number):
        if self.number is not None:
            if number < self.number:
                if self.vasak is None:
                    self.vasak = puu(number)
                else:
                    self.vasak.insert(number)
            elif number > self.number:
                    if self.parem is None:
                        self.parem = puu(number)
                    else: 
                        self.parem.insert(number)
        else:
            self.number = number

    def in_order_traversal(self, binaarpuu_list):
        if self.vasak:
            self.vasak.in_order_traversal(binaarpuu_list)
        binaarpuu_list.append(self.number)
        if self.parem:
            self.parem.in_order_traversal(binaarpuu_list)

vanem = puu(14)
vanem.insert(6)
vanem.insert(7)
vanem.insert(12)
vanem.insert(1)
vanem.insert(4)
vanem.insert(3)

binaarpuu_list = []

vanem.in_order_traversal(binaarpuu_list)
binaarpuu_list.reverse()

print(binaarpuu_list)
