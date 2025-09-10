class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add(self, item):
        self.cart.append(item.lower())
        print(f"{item} is added to cart")

    def remove(self, item):
        if item.lower() in self.cart:
            self.cart.remove(item.lower())
            print(f"{item} is removed from cart")
        else:
            print(f"{item} is not present in cart")

    def search(self, item):
        if item.lower() in self.cart:
            print(f"{item} is present in cart")
        else:
            print(f"{item} is not present in cart")

    def display(self):
        if self.cart:
            print(f"Items in cart are: {self.cart}")
        else:
            print("Cart is empty")

    def total(self):
        print(f"Total number of items in cart: {len(self.cart)}")

    def clear(self):
        self.cart.clear()
        print("Cart has been cleared")

    def sort_items(self):
        self.cart.sort()
        print(f"The sorted cart is: {self.cart}")



def main():
    cart = ShoppingCart()
    cond = True
    
    while cond:
        print("-----------------------------------------------------------------")
        print(" 1. Add\n 2. Remove\n 3. Search\n 4. Display\n 5. Total\n 6. Clear\n 7. Sort\n 8. Exit")
        print("-----------------------------------------------------------------")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number (1-8).")
            continue

        match choice:
            case 1:
                s = input("Enter the product to add: ")
                cart.add(s)
            case 2:
                s = input("Enter the product to remove: ")
                cart.remove(s)
            case 3:
                s = input("Enter the product to search: ")
                cart.search(s)
            case 4:
                cart.display()
            case 5:
                cart.total()
            case 6:
                cart.clear()
            case 7:
                cart.sort_items()
            case 8:
                cond = False
                print("Thank you for using the cart system. Goodbye!")
            case _:
                print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
