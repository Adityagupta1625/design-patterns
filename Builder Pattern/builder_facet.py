class Person:
    def __init__(self):
        print('Creating an instance of Person')
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment info
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' +\
            f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'


class PersonBuilder:  # facade
    def __init__(self, person=None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    p = pb\
        .lives\
            .at('123 London Road')\
            .in_city('London')\
            .with_postcode('SW12BC')\
        .works\
            .at('Fabrikam')\
            .as_a('Engineer')\
            .earning(123000)\
        .build()
    print(p)
    person2 = PersonBuilder().build()
    print(person2)


# In the provided code, the Builder Pattern is implemented using the concept of a "facade" builder, where different aspects of building a complex object are managed by separate builder classes. Let's break down the code and explain how it utilizes the Builder Pattern:

# 1. **Person Class**: Represents a person with attributes for address and employment information. The class has a `__str__` method to generate a string representation of the person's details.

# 2. **PersonBuilder Class**: Acts as a facade for constructing `Person` objects. It provides methods for accessing sub-builders for defining the address (`lives`) and employment (`works`) details, as well as a `build` method to finalize the construction and return the `Person` object.

# 3. **PersonJobBuilder Class**: Inherits from `PersonBuilder` and focuses on building the employment information of a person. It provides methods like `at`, `as_a`, and `earning` for setting the company name, position, and annual income, respectively.

# 4. **PersonAddressBuilder Class**: Also inherits from `PersonBuilder` and handles the construction of address details. It provides methods like `at`, `with_postcode`, and `in_city` for setting the street address, postcode, and city, respectively.

# 5. **Usage in `__main__` Block**: In the main block, an instance of `PersonBuilder` is created. Through method chaining, the address and employment details of a person are specified using the `lives` and `works` sub-builders. Finally, the `build` method is called to construct the `Person` object.

# 6. **Explanation of Facade Builder**: The facade builder (`PersonBuilder`) provides a simplified interface for constructing `Person` objects by delegating the construction process to specialized builders (`PersonAddressBuilder` and `PersonJobBuilder`). This segregation of concerns ensures that each builder focuses on a specific aspect of the object being constructed, promoting separation of concerns and maintainability.

# 7. **Flexibility and Readability**: The use of the Builder Pattern allows for flexible construction of `Person` objects. Clients can specify only the details they are interested in, and the builder takes care of the rest. Additionally, method chaining enhances readability by providing a fluent interface for building complex objects.

# Overall, the code demonstrates how the Builder Pattern can be used to construct complex objects with multiple components in a structured and maintainable manner, enhancing flexibility and readability.
