class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as a {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    me = pb\
        .called('Dmitri')\
        .works_as_a('quant')\
        .born('1/1/1980')\
        .build()  # this does NOT work in C#/C++/Java/...
    print(me)

# In the provided code, the Builder Pattern is implemented along with a form of inheritance to progressively add information to a `Person` object. Let's explain how binder inheritance is utilized in this context:

# 1. **Person Class**: Represents a person with attributes for name, position, and date of birth. The `__str__` method generates a string representation of the person's details.

# 2. **PersonBuilder Class**: Serves as the base builder class. It initializes a `Person` object and provides a `build` method to return the constructed `Person` instance.

# 3. **PersonInfoBuilder Class**: Inherits from `PersonBuilder` and adds the ability to specify the person's name. The `called` method sets the name attribute of the `Person` object.

# 4. **PersonJobBuilder Class**: Inherits from `PersonInfoBuilder` and extends it further by allowing the specification of the person's position. The `works_as_a` method sets the position attribute of the `Person` object.

# 5. **PersonBirthDateBuilder Class**: Inherits from `PersonJobBuilder` and adds the ability to specify the person's date of birth. The `born` method sets the date_of_birth attribute of the `Person` object.

# 6. **Usage in `__main__` Block**: In the main block, an instance of `PersonBirthDateBuilder` is created. Through method chaining, various aspects of the person's information (name, position, and date of birth) are specified. Finally, the `build` method is called to construct the `Person` object.

# 7. **Explanation of Binder Inheritance**: In this implementation, each builder class inherits from the previous one, progressively extending its functionality. This inheritance hierarchy forms a "binder" where each subclass binds additional information to the `Person` object. As a result, the `Person` object is constructed step by step, with each builder adding specific details.

# 8. **Advantages of Binder Inheritance**: Binder inheritance provides a structured and intuitive way to build objects incrementally. It promotes code reuse and separation of concerns by organizing the construction process into modular and specialized components.

# Overall, the code demonstrates how binder inheritance can be effectively used in conjunction with the Builder Pattern to construct complex objects in a systematic and flexible manner.