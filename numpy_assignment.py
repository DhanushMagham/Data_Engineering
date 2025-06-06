# -*- coding: utf-8 -*-
"""numpy assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dkk53bzxd8XW5GG9G7VaKIMBZ2Cq9eCK
"""

import numpy as np

# Retail dataset as numpy array

retail_np_array = np.array([
    [1001, "Laptop", 1, 50000, 50000],
    [1002, "Mouse", 2, 500, 1000],
    [1003, "Keyboard", 1, 1000, 1000],
    [1004, "Monitor", 2, 7000, 14000],
    [1005, "Headphones", 1, 2000, 2000]
], dtype=object)

retail_np_array

# Extracting columns

customer_ids = retail_np_array[:, 0]

products = retail_np_array[:, 1]

quantities = retail_np_array[:, 2].astype(int)

prices = retail_np_array[:, 3].astype(int)

totals = retail_np_array[:, 4].astype(int)

customer_ids

products

quantities

prices

totals

customer_ids1 = retail_np_array[:, 0]
customer_ids1

retail_np_array.shape # returns the shape like rows and coloumns

print("1. Total number of transactions: ",retail_np_array.shape[0])

print("2. Total revenue generated: ",np.sum(totals))

print("3. Average order value: ",np.mean(totals))

print("4. Product with the highest total price: ",products [np.argmax(totals)])

print("5. Product with the lowest total price: ",products [np.argmin(totals)])

print("6. Average price of products: ",np.mean (prices))

print("7. Total quantity sold: ",np.sum (quantities),)

print("8. Most frequently purchased product: ",np.unique(products, return_counts=True)[0][np.argmax(np.unique(products, return_counts=True)[1])])

print("9. Number of unique products : ",len (np.unique (products)),)

print("10. Number of unique customers: ",len(np.unique(customer_ids)))

print("11. List all products sold: ",products.tolist())

print("12. Revenue per product: ",{prod: np.sum(totals[products == prod]) for prod in np.unique(products)},)

print("13. Quantity sold per product : ",{prod: np.sum(quantities[products == prod]) for prod in np.unique(products)})

print("14. Highest price of a product : ",np.max(prices),)

print("15. Lowest price of a product : ",np.min(prices))

print("16. Products sold more than once : ",products[quantities > 1].tolist())

print("17. Customers who bought more than one item : ",customer_ids[quantities > 1])

print("18. Total spent by CustomerID 1002 : ",np.sum(totals[customer_ids == 1002]))

print("19. Products priced above 1000 : ",products[prices > 1000])

print("20. Products with total >= 2000 : ",products[totals >= 2000])

