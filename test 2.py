class Product:
    def __init__(self, type = None, price = None, qty = None) -> None:
        if type is not None:
            self.type = type
        else:
            self.type = input("Enter type: ")

        if price is not None:
            self.price = price
        else:
            self.price = int(input("Enter price: "))

        if qty is not None:
            self.qty = qty
        else:
            self.qty = int(input("Enter Quantity: "))

    def isEmpty(self):
        return True if self.qty == 0 else False
    
    def stocked(self, qty):
        self.qty += qty
        return self.cash(qty)

    def sold(self, qty):
        if self.has(qty):
            self.qty += -qty
            return self.cash(qty)
        return 0

    def has(self, qty):
        return True if qty <= self.qty else False

    def cash(self, qty):
        return qty * self.price
    
    def toString(self):
        if not self.isEmpty():
            output = f"{self.type} level: {self.qty} at price {self.price:.2f}"
        else:
            output = f"{self.type} level: {self.qty}"

        print(output)

class CashRegister:
    def __init__(self, cash = 0) -> None:
        self.cash = cash
    
    def gain(self, cash):
        self.cash += cash

    def pay(self, cash):
        self.cash += -cash

    def isEmpty(self):
        return True if self.cash == 0 else False
    
    def has(self, cash):
        return True if cash <= self.cash else False

    def toString(self):
        if not self.isEmpty():
            output = f"Cash level: {self.cash}"
        else:
            output = "Cash register is empty"

        print(output)


class Shop:
    def __init__(self) -> None:
        self.product = Product("Pepsi", 20, 10)
        self.cashRegister = CashRegister()
    
    def sell(self):
        qty = int(input("Please enter the quantity to sell: "))
        if self.product.has(qty):
            self.cashRegister.gain(self.product.sold(qty))
        else:
            print("Not enough stock")

    def restock(self):
        qty = int(input("Please enter the quantity to restock: "))
        if self.cashRegister.has(self.product.cash(qty)):
            self.cashRegister.pay(self.product.stocked(qty))
        else:
            print("Not enough funds")

    def view(self):
        self.product.toString()
        self.cashRegister.toString()

    def help(self):
        print("\nMenu Options\ns = sell\nr = restock\nv = view\nx = exit\n")
    
    def menu(self):
        cmd = ''
        while cmd != 'x':
            self.help()
            cmd = input()
            match cmd:
                case 's':
                    self.sell()
                case 'r':
                    self.restock()
                case 'v':
                    self.view()
                case 'x':
                    break
                case _:
                    self.help()

if __name__ == "__main__":
    s = Shop()
    s.menu()