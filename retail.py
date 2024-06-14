class item:
    all=[]
    def __init__(self,name: str,price: float,quantity):
        assert price>=0 ,f"{price} should be greater than zero!"
        assert quantity>=0,f"{quantity} should be greater than zero!"

        self.name =name
        self.price=price
        self.quantity=quantity

        item.all.append(self)

    @classmethod
    def create_item(cls):  # cls refers to the class itself
        print("\nEnter details")
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))

        # Create an instance of the class using cls
        new_item = cls(name, price, quantity)
        
        flag = input("Do you want to apply specific discount [y/n]: ")
        if flag == 'y':
            discount = float(input("Enter discount percent: "))
            new_item.apply_discount(discount)
        
        return new_item

    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self,discount):
        self.price = self.price * (1 - discount / 100)
    
    def print_bill(self):
        print(f"\nItem: {item.all.index(self) + 1}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Price: {self.calculate_total_price()}\n")
    
    def edit_details(self):
        print("\nenter new details")
        self.name=input("enter item name ")
        self.price=int(input("enter item price "))
        self.quantity=int(input("enter item quantity "))      
  

def display_menu():
    print("\nMenu:")
    print("1. Add Item")
    print("2. Print Bill")
    print("3. Edit Item")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                new_item = item.create_item()
                print(f"Item '{new_item.name}' added.")
            case '2':
                print("Your bill is:")
                for item_instance in item.all:
                    item_instance.print_bill()
            case '3':
                index = int(input("Enter the item number you would like to edit: ")) - 1
                if 0 <= index < len(item.all):
                    item.all[index].edit_details()
                    print("Updated item details:")
                    item.all[index].print_bill()
                else :
                    print("Item not found")
            case '4':
                print("Exiting the program.")
                return
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

