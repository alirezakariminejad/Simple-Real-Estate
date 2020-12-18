from base import BaseClass


class Sell(BaseClass):
    def __init__(self, price_per_meter, discountable, convertable, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f"price: {self.price_per_meter} \t discount: {self.discountable} \t convert: {self.convertable}")


class Rent(BaseClass):
    def __init__(self, initial_price, monthly_price, discountable, convertable, *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.discountable = discountable
        self.convertable = convertable
        super().__init__(*args, **kwargs)
