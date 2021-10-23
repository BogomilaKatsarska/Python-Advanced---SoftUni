max_items_basket = 5
minimum_money = 100


def shopping_list(budgeted_money, **kwargs):
    if budgeted_money < minimum_money:
        return "You do not have enough budget."

    products_basket = []

    for product, values in kwargs.items():
        P, Q = [float(x) for x in values]
        total_p = P * Q

        if total_p <= budgeted_money:
            products_basket.append(f"You bought {product} for {total_p:.2f} leva.")
            budgeted_money -= total_p

        if len(products_basket) == max_items_basket:
            return "\n".join(products_basket)

    return "\n".join(products_basket)