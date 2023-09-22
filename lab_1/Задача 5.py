products = {
    "торт": ["со сливочным кремом", 150, 10],
    "маффин": ["пышный", 20, 100],
    "пирожное": ["заварное", 30, 30],
    "пирог": ["яблочный", 100, 5]
}
purchased_items = []
while True:
    print("\nМеню кондитерской\n1. Описание товаров\n2. Цена товаров\n"
          "3. Кол-во товаров\n4. Вся информация\n5. Покупка\n6. Выйти")
    choice = input()
    if choice == "1":
        for product, information in products.items():
            print(f"{product} {information[0]}")
    elif choice == "2":
        for product, information in products.items():
            print(f"{product} стоит {information[1]} рублей")
    elif choice == "3":
        for product, information in products.items():
            print(f"Продукции {product} есть {information[2]} единиц")
    elif choice == "4":
        for product, information in products.items():
            print(f"Продукции {product} {information[0]} за "
                  f"{information[1]} рублей есть {information[2]} единиц")
    elif choice == "5":
        total_price = 0
        while True:
            print("Введите название продукции (или 'n' для завершения покупки):")
            product_name = input()
            product_name = product_name.lower()
            if product_name == 'n':
                break
            if product_name in products:
                print(f"Введите количество {product_name}:")
                try:
                    quantity = int(input())
                    if quantity <= products[product_name][2]:
                        total_price += (products[product_name][1]) * quantity
                        products[product_name][2] -= quantity
                        purchased_items.append((product_name, quantity, products[product_name][1]))
                    else:
                        print(
                            f"Извините, не хватает {product_name}. Доступное количество: {products[product_name][2]}.")
                except ValueError:
                    print("Пожалуйста, введите корректное количество.")
            else:
                print("Продукция с таким названием не найдена в меню.")

        print("\nЧек:")
        for item, quantity, cost in purchased_items:
            print(f"{item}: {quantity} шт. по {cost} р.")

        print(f"Сумма вашей покупки: {total_price} рублей\n")
        print("Остатки продукции в меню:")
        for product, information in products.items():
            print(f"{product} осталось {information[2]} штук")
    elif choice == "6":
        break
    else:
        print("Введите подходящую цифру")
