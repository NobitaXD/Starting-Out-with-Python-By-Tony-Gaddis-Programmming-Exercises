# Muhammad Saim
# https://github.com/NobitaXD

sales_tax = 0.7

iteam1 = int(input("Enter iteam 1 Price: "))
iteam2 = int(input("Enter iteam 2 Price: "))
iteam3 = int(input("Enter iteam 3 Price: "))
iteam4 = int(input("Enter iteam 4 Price: "))
iteam5 = int(input("Enter iteam 5 Price: "))

subtotal = iteam1+iteam2+iteam3+iteam4+iteam5
tax_total = subtotal * sales_tax

total = subtotal + tax_total

print("Subtotal : ", subtotal)
print("Total With Taxes Added : ", total)
