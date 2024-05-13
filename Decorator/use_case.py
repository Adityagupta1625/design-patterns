from abc import ABC,abstractmethod

class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price


class CarFeature(ABC,Car):
    def __init__(self, car):
        super().__init__(car.get_make(),car.get_model(),car.get_year(),car.get_price())
        self.car = car

    @abstractmethod
    def get_price(self):
        pass

class NavigationDecorator(CarFeature):
    def get_price(self):
        return self.car.get_price() + 500  # Assuming $500 for navigation system


class SunroofDecorator(CarFeature):
    def get_price(self):
        return self.car.get_price() + 1000  # Assuming $1000 for sunroof

class SalesTaxDecorator(CarFeature):
    def get_price(self):
        return self.car.get_price() * 1.10  # 10% sales tax


car = Car("Honda", "Accord", 2022, 25000)
car_with_sales_tax = SalesTaxDecorator(car)
car_with_navigation = NavigationDecorator(car_with_sales_tax)
car_with_sunroof = SunroofDecorator(car_with_navigation)

print(f"Make: {car_with_sunroof.get_make()}")
print(f"Model: {car_with_sunroof.get_model()}")
print(f"Year: {car_with_sunroof.get_year()}")
print(f"Price: {car_with_sunroof.get_price()}")

# https://salithachathuranga94.medium.com/decorator-design-pattern-in-java-1b0931ead0e4
