#Calculate CGST and SGST for a product and print the total price to pay {CGST=9%, SGST=11%}

price = float(input("Enter the product price:"))
CGST = 9/100
SGST = 11/100
Amount_for_cgst = price*CGST
Amount_for_sgst = price*SGST
Total = price + Amount_for_cgst + Amount_for_sgst
print("price to pay for CGST: ",Amount_for_cgst)
print("price to pay for SGST: ",Amount_for_sgst)
print("Total price of Tax: ",Total)
