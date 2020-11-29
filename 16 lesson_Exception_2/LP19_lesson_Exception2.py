def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
    except TypeError:
        print("price type error")
        return -1
    except ValueError:        
        print("price Value error")
        return -1

    try:
        discount = float(discount)
    except TypeError:
        print("price type error")
        return -1
    except ValueError:        
        print("price Value error")
        return -1

    try:
        max_discount = int(max_discount)
    except TypeError:
        print("price type error")
        return -1
    except ValueError:        
        print("price Value error")
        return -1

    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

if __name__ == "__main__":
    discounted("aa", 100)