products = []
while True:
	name = input('enter the name of product: ') 
	if name == 'q':
		break
	price = input('enter the price of product: ')
	products.append([name, price]) # p = [name, price], # products.append(p)
print(products)


for p in products:
	print(p[0], 'cost', p[1]) 
