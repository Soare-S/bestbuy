import products
import store
import promotions


def main():
    """Set up initial stock of inventory, run the app using the start(best_buy) function,
    and handle potential error exceptions."""
    try:
        mac = products.Product("MacBook Air M2", price=1450, quantity=100)
        bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        pixel = products.Product("Google Pixel 7", price=500, quantity=250)
        windows = products.NonStockedProduct("Windows License", price=125)
        shipping = products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
        intel = products.LimitedProduct("Chip", price=1000, quantity=50, maximum=2)

        # Create promotion catalog
        second_half_price = promotions.SecondHalfPrice("Second Half price!")
        third_one_free = promotions.ThirdOneFree("Third One Free!")
        thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

        # Add promotions to products
        mac.set_promotion(second_half_price)
        bose.set_promotion(third_one_free)
        pixel.set_promotion(thirty_percent)

        best_buy = store.Store([mac, bose, pixel, windows, shipping])

        # Magic methods implemented
        mac.price = -100  # Should give error
        print(mac)  # Should print `MacBook Air M2, Price: $1450 Quantity:100`
        print(mac > bose)  # Should print True
        print(mac in best_buy)  # Should print True
        print(intel in best_buy)  # Should print False

        start(best_buy)
    except TypeError:
        print("Missing on of attributes: 'name', 'price' or 'quantity'")
    except NameError:
        print("Enter a positive number(digits) for price and/or quantity.")


def start(store_obj):
    """Run the main interactive loop of the store app, displaying the menu and
        responding to user choices.
    Args:
        store_obj (Store): The Store object representing the store."""
    while True:
        print("\nMenu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit\n")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            all_products = store_obj.get_all_products()
            index = 1
            for product in all_products:
                print(f"{index}. {product}")
                index += 1
        elif choice == "2":
            total_products = store_obj.get_total_quantity()
            print(f"Total of {total_products} items in store")
        elif choice == "3":
            shopping_items = []
            all_products = store_obj.get_all_products()
            index = 1
            for product in all_products:
                print(f"{index}. {product}")
                index += 1
            print("\nWhen you want to finish order, just press Enter.")
            ordered_limited_product = False
            while True:
                product = input("Which product # do you want?")
                if product == "":
                    break
                try:
                    product_index = int(product)
                    if product_index <= len(all_products):
                        quantity = int(input("What amount do you want? "))
                        product = all_products[product_index - 1]
                        if isinstance(product, products.LimitedProduct) and quantity > 1:
                            print("You can only order one unit of a limited products per order.")
                        elif isinstance(product, products.LimitedProduct) and ordered_limited_product:
                            print("You already have added this product!")
                        else:
                            shopping_items.append((product, quantity))
                            print("Product added to the list!")
                            if isinstance(product, products.LimitedProduct):
                                ordered_limited_product = True
                except TypeError:
                    pass
                except ValueError:
                    print("Enter a valid amount!")
            total_price = store_obj.order(shopping_items)
            print(f"\nTotal amount to pay is: {total_price}.")

        elif choice == "4":
            print("Thank you for visiting our shop!\nBye")
            break
        else:
            pass


if __name__ == "__main__":
    main()
