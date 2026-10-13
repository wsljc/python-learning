price = float(input("请输入商品价格："))
quantity = int(input("请输入商品数量："))
discount = int(input("请输入商品折扣（75就是七五折）"))
total = price * quantity*0.01*discount
print(f"最后的价格是{total:.2f}")