from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


class Printer:
    @abstractmethod
    def print(self, document): pass


class Scanner:
    @abstractmethod
    def scan(self, document): pass


# same for Fax, etc.

class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful


class MultiFunctionDevice(Printer, Scanner):  # , Fax, etc
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # oops!


# The Interface Segregation Principle (ISP) suggests that clients should not be forced to depend on interfaces they do not use. This principle is crucial in designing maintainable and flexible systems by preventing unnecessary coupling between components. Let's analyze the provided code in terms of the Interface Segregation Principle:

# 1. **Initial Machine Class**: The `Machine` class declares methods for printing, faxing, and scanning. However, not all machines support all these functionalities. This violates the ISP because clients of the `Machine` class may be forced to depend on methods they don't need.

# 2. **Implementations**:
#    - `MultiFunctionPrinter`: Implements all methods of the `Machine` class. It's suitable for clients that need all functionalities.
#    - `OldFashionedPrinter`: Implements only the `print` method. It's suitable for clients that only need printing functionality. However, it still inherits the `fax` and `scan` methods, violating the ISP.
#    - `MyPrinter`: Implements only the `print` method, adhering to the ISP by providing only the necessary functionality for its clients.

# 3. **Introduction of Abstract Classes**:
#    - `Printer` and `Scanner` are introduced as abstract classes, each defining only their respective methods. This aligns with the ISP because clients can now depend only on the interface they need.

# 4. **Usage of Abstract Classes**:
#    - `Photocopier` implements both `Printer` and `Scanner`, providing the necessary methods for each interface. It follows the ISP by allowing clients to depend only on the functionalities they require.

# 5. **Refactoring to Meet ISP**:
#    - `MultiFunctionDevice` introduces abstract methods for printing and scanning only. This is an improvement over the `Machine` class since it segregates the interfaces based on functionality.
#    - `MultiFunctionMachine` implements the `MultiFunctionDevice` interface, showing that a device can support multiple functionalities without forcing clients to depend on all of them.

# In summary, by applying the Interface Segregation Principle, the codebase becomes more modular, maintainable, and flexible. Clients are no longer forced to depend on unnecessary methods or functionalities, reducing coupling and improving the overall design of the system.

