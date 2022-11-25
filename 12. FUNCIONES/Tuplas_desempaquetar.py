#Devolucion de tuplas para desempaquetar

stock_precios = [('Zapato',100),('Camisa', 30),('Pantalon', 70)]

for item in stock_precios:
  print(item)

for stock, precio in stock_precios:
  print(stock)

for stock, precio in stock_precios:
  print(precio)