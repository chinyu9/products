#　read the file
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'Product, Price' in line:
			continue
		name, price = line.strip(). split(',')
		products.append([name, price])
print(products)

# let the user to enter
while True:
	name = input('enter the name of product: ') 
	if name == 'q':
		break
	price = input('enter the price of product: ')
	price = int(price)
	products.append([name, price]) # p = [name, price], # products.append(p)
print(products)

# print the entire purchase record
for p in products:
	print(p[0], 'cost', p[1]) 

# write the file
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product, Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #string
