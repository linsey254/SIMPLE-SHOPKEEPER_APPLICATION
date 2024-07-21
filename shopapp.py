# Shopkeeper Application

class Shopkeeper:
    def __init__(self):
        self.items = {}

    def add_item(self, product_number, buying_price, selling_price):
        self.items[product_number] = {"buying_price": buying_price, "selling_price": selling_price, "profit": selling_price - buying_price}

    def display_items(self):
        print("Product Number\tBuying Price\tSelling Price\tProfit")
        for product_number, item in self.items.items():
            print(f"{product_number}\t\t{item['buying_price']}\t\t{item['selling_price']}\t\t{item['profit']}")

    def calculate_total_profit(self):
        total_profit = sum(item["profit"] for item in self.items.values())
        print(f"Total Profit: {total_profit}")

def main():
    shopkeeper = Shopkeeper()

    while True:
        print("1. Add Item")
        print("2. Display Items")
        print("3. Calculate Total Profit")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            product_number = input("Enter product number: ")
            buying_price = float(input("Enter buying price: "))
            selling_price = float(input("Enter selling price: "))
            shopkeeper.add_item(product_number, buying_price, selling_price)
        elif choice == "2":
            shopkeeper.display_items()
        elif choice == "3":
            shopkeeper.calculate_total_profit()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()