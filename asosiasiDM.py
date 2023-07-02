class Transaction:
    def __init__(self, transaction_id, products):
        self.transaction_id = transaction_id
        self.products = products

    def get_products(self):
        return self.products


class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name


# Data transaksi
transaction1 = Transaction(1, ["Apple", "Banana", "Orange"])
transaction2 = Transaction(2, ["Banana", "Mango"])
transaction3 = Transaction(3, ["Apple", "Grapes"])
transaction4 = Transaction(4, ["Apple", "Banana", "Mango"])
transaction5 = Transaction(5, ["Orange", "Grapes"])

# Data produk
product1 = Product(1, "Apple")
product2 = Product(2, "Banana")
product3 = Product(3, "Orange")
product4 = Product(4, "Mango")
product5 = Product(5, "Grapes")

# Membuat daftar transaksi
transactions = [transaction1, transaction2, transaction3, transaction4, transaction5]

# Membuat daftar produk
products = [product1, product2, product3, product4, product5]

# Membuat dictionary untuk menyimpan asosiasi antara produk
associations = {}

# Melakukan perulangan untuk setiap transaksi
for transaction in transactions:
    products_list = transaction.get_products()

    # Membuat asosiasi antara setiap pasangan produk dalam transaksi
    for i in range(len(products_list)):
        for j in range(i + 1, len(products_list)):
            product1 = products_list[i]
            product2 = products_list[j]

            # Memperbarui asosiasi
            if product1 in associations:
                associations[product1].add(product2)
            else:
                associations[product1] = {product2}

            if product2 in associations:
                associations[product2].add(product1)
            else:
                associations[product2] = {product1}

# Menampilkan asosiasi antara produk
for product, associated_products in associations.items():
    print(f"Associated products for {product.name}:")
    for associated_product in associated_products:
        print(associated_product.name)
    print()
