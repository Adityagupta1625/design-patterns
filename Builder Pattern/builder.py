class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    # not fluent
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # fluent
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)


# if you want to build a simple HTML paragraph using a list
hello = 'hello'
parts = ['<p>', hello, '</p>']
print(''.join(parts))

# now I want an HTML list with 2 words in it
words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f'  <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))

# ordinary non-fluent builder
# builder = HtmlBuilder('ul')
builder = HtmlElement.create('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print('Ordinary builder:')
print(builder)

# fluent builder
builder.clear()
builder.add_child_fluent('li', 'hello') \
    .add_child_fluent('li', 'world')
print('Fluent builder:')
print(builder)

# Certainly! The Builder Pattern is a creational design pattern used to construct complex objects step by step. It separates the construction of an object from its representation, allowing the same construction process to create different representations.

# Let's break down the example code using the Builder Pattern:

# 1. **HtmlElement Class**: This class represents an HTML element. It has attributes for the element's name, text content, and child elements. The constructor (`__init__`) initializes these attributes.

# 2. **HtmlBuilder Class**: This class acts as a builder for constructing HTML elements. It provides methods for adding child elements (`add_child` and `add_child_fluent`), clearing the builder state (`clear`), and generating the string representation of the built HTML (`__str__`).

# 3. **create Method**: This is a static method of the `HtmlElement` class that initializes an `HtmlBuilder` instance with the specified root element name.

# 4. **Fluent Interface**: The `HtmlBuilder` class provides a fluent interface through methods like `add_child_fluent`. This allows method chaining, enhancing readability and conciseness when building HTML structures.

# 5. **Demonstration**: The code demonstrates the construction of HTML elements using both non-fluent and fluent approaches. It builds an unordered list (`<ul>`) with list items (`<li>`) containing the words "hello" and "world".

# 6. **Clear Method**: The `clear` method in the `HtmlBuilder` class resets the builder to its initial state, allowing for the construction of a new HTML structure.

# 7. **String Representation**: The `__str__` methods in both `HtmlElement` and `HtmlBuilder` classes facilitate obtaining the string representation of the HTML elements or structures built using the builder.

# In summary, the Builder Pattern in this example separates the construction of HTML elements from their representation, providing a flexible and readable way to construct HTML structures. It promotes code clarity, reusability, and allows for the construction of complex HTML hierarchies through a simple and intuitive interface.

