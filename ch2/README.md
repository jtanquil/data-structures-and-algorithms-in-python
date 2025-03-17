## Chapter 2 Notes

---

### Abstraction in Python

- **abstract data types** are mathematical models of data structures that specify the type of data store, the operations supported by the data structure, and the parameters on those operations
- there is no "compile time" checking of data types in Python, so programmers operate under the assumption that given objects support a set of known behaviors and the interpreter will throw runtime errors if those assumptions fail; this is known as **duck typing**
- **abstract base classes** cannot be instantiated, but it defines one or more common methods that all concrete implementations of the abstract base class must have
  - ABCs are realized through concrete classes that inherit from the ABC and provide implementations for the methods declared by the ABC
  - example: there are several ABCs in Python's `collections` module which include definitions for common data structure ADTs

### Naming Conventions

- classes should have a name that is a singular noun, capitalized (`Date` as opposed to `Dates` or `date`), using CamelCase when necessary (`CreditCard`)
- functions, including class methods, should be lowercase, with words separated by underscores: `make_payment`
- names that identify an individual object (a function parameter, instance variable, or local variable) should generally be a lowercase noun
- identifiers that represent constants should be all caps, with underscores to separate words: `MAX_SIZE`

### Docstrings

- string literals delimited within triple quotes `"""`, appearing as the first statement within the body of a module, class or function that generally serves to provide documentation for the corresponding block of code
- docstrings can be used to automatically generate documentation for the code

### Python Class Syntax

- `self` is an identifier that refers to the instance of the class upon which class methods are invoked
- `__init__` is the constructor for the class
- `super()` is used to access the parent class; it can be used to call parent methods like the parent constructor (`super().__init__(...)`) or parent methods (`super().make_payment(...)`)

### Operator Overloading and Type Checking with Different Operands

- given an expression with a binary operator where the operands are of different types, say `3 * "hi"`, Python determines the result of the expression as follows:
  - 1) checking the class of the left operand for a definition on how to operate on it with an instance of the right operand's class; in this case it will look for a `__mult__` method in the `Int` class that can multiply an integer by a string
  - 2) checking the class of the right operand for a definition on how to *right-operate* on it with an instance of the left operand's class; in this case, Python will look for an `__rmult__` method in the `String` class that an right-multiply an integer by a string
    - in this case Python looks for a defined right operation to account for operations that don't commute, like multiplying a matrix by a vector

### Implied Methods: `if` and `==`

- in general, expressions like `a + b` will raise an exception if `a` and `b` are user-defined classes that don't provide methods that defined this behavior (in this case, an `__add__` or `__radd__` method)
- there are some notable instances where even without these user-defined methods, operators can still act on user-defined classes:
  - **`__bool__`**: this method supports the syntax `if a`, and by default evaluates every object other than `None` as `True`. But for container types that have a `__len__` method, `if a` will return `True` if and only if the length of `a` is nonzero.
  - `==`: the semantics of `a == b` and `a is b` is typically different; the latter is generally meant to mean "`a` and `b` are aliases for the same object" since that is the only instance in which `a is b` is `True`, whereas `a == b` can also be `True` if `a` and `b` are aliases for objects that are equivalent in some sense. This equivalence can be defined through an `__eq__` class method, but if no such method exists, then `a == b` will be evaluated as `a is b`.

### Protected vs Private Members

- **protected** members are accessible by subclasses/inherited classes, but not to the general public
- **private** members are accessible to neither
- Python doesn't offer formal access control, just the convention that names beginning with a single underscore `_` are to be treated as protected members, and names beginning with a double underscore `__` as private members

### The Template Design Pattern

- a design pattern in which an abstract base class provides concrete behaviors that rely upon class to other abstract behaviors
- when an inheriting subclass provides definitions for these abstract behaviors, the inherited concrete behaviors within the abstract class become well-defined (for the inheriting subclass)
- **idea**: the abstract base class lays out some intended behavior for the inheriting classes, but the actual implementation of these behaviors are left to the subclasses
- **example**: the `collections.Sequence` ABC in Python provides concrete implementation of methods common to Python sequences, like `count`, `index`, and `__contains__` (which supports `element in sequence`) but those implementations are dependent on the inherited class defining behavior such as integer access of indices, etc.

### Namespaces and `__slots__`

- **instance namespace**: namespace that manages attributes specific to an instance of a class
- **class namespace**: namespace that manages members that are shared by *all* instances of a class
- by default, Python represents namespaces with its built-in `dict` class, with identifiers and objects as the key-value pairs
- for instance namespaces, a more streamlined approach uses the `__slots__` keyword:

```
class ClassName:
  __slots__ = 'instance_variable_1', 'instance_variable_2' # comma separated list of vars
```

- this is typically not necessary but useful for classes in which you expect to have a large number of instances of that class (nested classes representing data structures like trees or linked lists are an example)

### Shallow and Deep Copy

- the `copy` module provides a `deepcopy` method that creates a deep copy of its argument:

```
import copy

a = [[1], [2], [3]]
b = list(a) # creates a shallow copy of a, so a[0] and b[0] are aliases of the same object [1]
c = copy.deepcopy(a)

a[0][0] = 4

print(b) # [[4], [2], [3]]
print(c) # [[1], [2], [3]]
```