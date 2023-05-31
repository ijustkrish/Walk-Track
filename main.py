import tkinter as tk
from tkinter import messagebox

class ShoeShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Walk Track")
        self.root.geometry("600x400")
        
        self.inventory = {}
        self.sales = []

        self.inventory_frame = tk.LabelFrame(self.root, text="Inventory")
        self.inventory_frame.pack(pady=10)

        self.product_label = tk.Label(self.inventory_frame, text="Product Name:")
        self.product_label.grid(row=0, column=0, padx=5, pady=5)
        self.product_entry = tk.Entry(self.inventory_frame)
        self.product_entry.grid(row=0, column=1, padx=5, pady=5)

        self.quantity_label = tk.Label(self.inventory_frame, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(self.inventory_frame)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.inventory_frame, text="Add to Inventory", command=self.add_to_inventory)
        self.add_button.grid(row=2, columnspan=2, padx=5, pady=5)

        self.sales_frame = tk.LabelFrame(self.root, text="Sales")
        self.sales_frame.pack(pady=10)

        self.customer_label = tk.Label(self.sales_frame, text="Customer Name:")
        self.customer_label.grid(row=0, column=0, padx=5, pady=5)
        self.customer_entry = tk.Entry(self.sales_frame)
        self.customer_entry.grid(row=0, column=1, padx=5, pady=5)

        self.sale_product_label = tk.Label(self.sales_frame, text="Product Name:")
        self.sale_product_label.grid(row=1, column=0, padx=5, pady=5)
        self.sale_product_entry = tk.Entry(self.sales_frame)
        self.sale_product_entry.grid(row=1, column=1, padx=5, pady=5)

        self.sale_quantity_label = tk.Label(self.sales_frame, text="Quantity:")
        self.sale_quantity_label.grid(row=2, column=0, padx=5, pady=5)
        self.sale_quantity_entry = tk.Entry(self.sales_frame)
        self.sale_quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        self.sale_price_label = tk.Label(self.sales_frame, text="Sale Price:")
        self.sale_price_label.grid(row=3, column=0, padx=5, pady=5)
        self.sale_price_entry = tk.Entry(self.sales_frame)
        self.sale_price_entry.grid(row=3, column=1, padx=5, pady=5)

        self.sell_button = tk.Button(self.sales_frame, text="Sell Product", command=self.sell_product)
        self.sell_button.grid(row=4, columnspan=2, padx=5, pady=5)

        self.reports_frame = tk.LabelFrame(self.root, text="Reports")
        self.reports_frame.pack(pady=10)

        self.inventory_button = tk.Button(self.reports_frame, text="View Inventory", command=self.view_inventory)
        self.inventory_button.grid(row=0, column=0, padx=5, pady=5)

        self.sales_button = tk.Button(self.reports_frame, text="View Sales", command=self.view_sales)
        self.sales_button.grid(row=0, column=1, padx=5, pady=5)

    def add_to_inventory(self):
        product = self.product_entry.get()
        quantity = self.quantity_entry.get()

        if product and quantity:
            if product in self.inventory:
                self.inventory[product] += int(quantity)
            else:
                self.inventory[product] = int(quantity)
            
            messagebox.showinfo("Inventory", f"{quantity} {product}(s) added to inventory.")
        else:
            messagebox.showerror("Error", "Please enter both product name and quantity.")

        self.product_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def sell_product(self):
        customer = self.customer_entry.get()
        product = self.sale_product_entry.get()
        quantity = self.sale_quantity_entry.get()
        price = self.sale_price_entry.get()

        if customer and product and quantity and price:
            if product in self.inventory and self.inventory[product] >= int(quantity):
                self.inventory[product] -= int(quantity)
                self.sales.append({
                    "customer": customer,
                    "product": product,
                    "quantity": int(quantity),
                    "price": float(price)
                })
                messagebox.showinfo("Sales", f"{quantity} {product}(s) sold to {customer} at {price} per unit.")
            else:
                messagebox.showerror("Error", "Product not available in inventory or insufficient quantity.")
        else:
            messagebox.showerror("Error", "Please enter customer name, product name, quantity, and sale price.")

        self.customer_entry.delete(0, tk.END)
        self.sale_product_entry.delete(0, tk.END)
        self.sale_quantity_entry.delete(0, tk.END)
        self.sale_price_entry.delete(0, tk.END)

    def view_inventory(self):
        inventory_str = "Current Inventory:\n"
        for product, quantity in self.inventory.items():
            inventory_str += f"{product}: {quantity}\n"
        
        messagebox.showinfo("Inventory", inventory_str)

    def view_sales(self):
        sales_str = "Sales Report:\n"
        for sale in self.sales:
            customer = sale["customer"]
            product = sale["product"]
            quantity = sale["quantity"]
            price = sale["price"]
            sales_str += f"Customer: {customer}\nProduct: {product}\nQuantity: {quantity}\nPrice: {price}\n\n"
        
        messagebox.showinfo("Sales", sales_str)

root = tk.Tk()
shoe_shop_app = ShoeShopApp(root)

root.mainloop()