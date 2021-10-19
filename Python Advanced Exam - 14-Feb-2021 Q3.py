def stock_availability(product_list: list, command, *args):
    if command == "delivery":
        for el in args:
            product_list.append(el)
    elif command == "sell":
        if args == ():
            if product_list:
                del product_list[0]
        elif str(args[0]).isdigit():
            if int(args[0]) < len(product_list):
                for _ in range(int(args[0])):
                    del product_list[0]
            else:
                product_list.clear()
        else:
            for el in args:
                while el in product_list:
                    product_list.remove(el)

    return product_list

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))