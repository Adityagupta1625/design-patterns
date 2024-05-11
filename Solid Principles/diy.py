from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):  # low-level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))
            
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, relationships):
    #     # high-level: find all of john's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)

# The Dependency Inversion Principle (DIP) suggests that high-level modules should not depend on low-level modules but instead both should depend on abstractions. In the provided code, the Research class initially violates this principle by directly depending on the low-level Relationships class.

# However, by introducing the RelationshipBrowser abstract class, the code adheres to the Dependency Inversion Principle. Here's how:

# 1. **High-level Module (Research):** This class used to directly depend on the low-level Relationships class. It would iterate over relationships to find John's children. This direct dependency was inflexible because any changes in the low-level Relationships class would require corresponding changes in the Research class.

# 2. **Abstraction (RelationshipBrowser):** The introduction of the RelationshipBrowser abstract class serves as the abstraction layer. It defines the interface that the high-level module (Research) depends on. This interface includes the method `find_all_children_of`, which is used by the high-level module to interact with the low-level module without needing to know its implementation details.

# 3. **Low-level Module (Relationships):** This class originally implemented the storage and retrieval of relationships. However, with the introduction of the RelationshipBrowser abstract class, it now implements that interface. This means it adheres to the Dependency Inversion Principle because both the high-level module (Research) and low-level module (Relationships) depend on the abstraction (RelationshipBrowser), not on each other directly.

# By restructuring the code in this manner, it becomes more flexible and adheres better to the principles of object-oriented design, particularly the Dependency Inversion Principle. Now, if the implementation of the low-level module changes (for example, if relationships are stored in a different way), the high-level module does not need to change as long as the interface remains consistent.