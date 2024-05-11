class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)


# The Liskov Substitution Principle (LSP) is one of the five SOLID principles of object-oriented programming. It states that objects of a superclass shall be replaceable with objects of its subclasses without affecting the correctness of the program. In simpler terms, it emphasizes that inheritance should not break the behavior of the base class.

# In the provided code, there is a `Rectangle` class and a subclass `Square`. According to the Liskov Substitution Principle, any instance of `Rectangle` should be replaceable with an instance of `Square` without affecting the behavior of the program. However, the `Square` class in the code violates the LSP.

# The violation occurs in the `Square` class's setter methods for `width` and `height`. In the `Rectangle` class, these setters correctly update both `_width` and `_height` attributes. But in the `Square` class, the setters are overridden to only update `_width` and `_height` locally, neglecting to update the attributes in the superclass. This behavior breaks the principle because it alters the behavior of the base class (`Rectangle`) when replaced by its subclass (`Square`).

# When the `use_it` function is called with an instance of `Rectangle`, everything works as expected. But when it's called with an instance of `Square`, the height is set to 10, which effectively changes the width as well (since they are always equal in a square), resulting in an incorrect area calculation.

# To adhere to the Liskov Substitution Principle, any subclass should extend the behavior of the superclass without altering it. In this case, the `Square` class should maintain the behavior of the `Rectangle` class, ensuring that setting the width or height updates both attributes to preserve the integrity of the square's dimensions.