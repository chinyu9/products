import os # operating sys

def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'Product, Price' in line:
                continue  # next round
            name, price = line.strip(). split(',')
            products.append([name, price])
    return products
          
# let the user to enter
def user_input(products):
    while True:
        name = input('enter the name of product: ')
        if name == "q":
            break
        price = input('enter the price of product: ')
        price = int(price)
        products.append([name, price]) # p = [name, price], # products.append(p)
    print(products)
    return products

# print the entire purchase record
def print_products(products):
    for p in products:
        print(p[0], 'cost', p[1]) 

# write the file
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('Product, Price\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n') #string


def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # ensure the existence of the file
        print('yeahh! the file is found')
        products = read_file(filename)
    else:
        print('the file can not be found')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()

#refactor reestructurar
