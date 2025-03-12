## Chapter 1 Notes

---

- identifiers are implicitly associated with the memory address of the object to which it refers
- **immutable types**: `bool`, `int`, `float`, `tuple`, `str` and `frozenset` are immutable; the other common built-in classes (`list`, `set`, `dict`) are mutable.
- **truthy values**: nonzero numbers, nonempty containers
- **falsy values**: `0`, empty containers

### `list`

- `list`s are **referential** structures: they technically store a sequence of references to its elements
- `list`s are dynmaically sized

### `set`

- represents and acts like the mathematical object
- only instances of immutable types can be added as elements to sets

### Equality Operators: `is`/`is not` vs `==`/`!=`

- `a is b` is `True` if and only if `a` and `b` are aliases for the *same* object.
- `a == b` is `True` if and only if `a is b` **or** when the identifiers refer to different objects that happen to have values that are deemed equivalent
  - the notion of equivalence depends on the data type; for instance, if `a` and `b` are distinct collections, then `a == b` if they have the same contents:

```
a = [1, 2]
b = [1, 2]

print(a is b) # False
print(a == b) # True
```

### Comparison Operators

- these use lexicographic ordering for strings and sequences
- raise an exception if the operands have incomparable types

### Arithmetic Operators

- `/` represents true, floating-point division
- `//` represents integer division (floor)
- Python extends the semantics of `//` and `%` to cases where one or more of the operands is negative, and to floating-point operands

### Pass by Value/Reference Behavior

- parameters *act as aliases to the arguments passed to the function*, so if the argument is a mutable type like a `list`, then it is possible for the function to mutate the argument through the parameter
- this can't happen with immutable types
- should be similar to js

### Iterators and Iterable Types

- **iterators** are objects that manage iteration through a sequence of values (either a static list of values of a dynamically generated sequence of values)
  - if `i` is an iteratble, then the call to the function `next(i)` returns the next element of the underlying sequence until a `StopIteration` exception is raised to indicate that there are no more elements
- **iterables** are types of objects that produce an iterator via the syntax `iter(obj)`
- iterators are used under the hood of the `for` loop syntax `for x in iterable`; each loop is performed by retrieving the next element of `iterable` via an iterator and assigning it to `element`

### Generators

- **generators** are a type of function that return an iterator; their syntax uses the `yield` keyword instead of `return`. Each invocation of the returned iterator yields the next element of the underlying sequence:

```
def fib():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# ...

i = fib()

print(next(i)) # 0
print(next(i)) # 1
print(next(i)) # 1
print(next(i)) # 2
print(next(i)) # 3
print(next(i)) # 5

# etc...
```

- **idea**: `fib` is a function that returns an iterator, which is assigned to `i`. The underlying sequence is defined by the function body of `fib`: on each call to `next`, the function body executes until it encounters a `yield` statement, which returns the value of the expression `a`. Execution of this function body is paused until the next call to `next`.

### Misc. Python Features

- **ternary expression**: `a if condition else b` is equivalent to `condition ? a : b` in javascript
- **list comprehensions**: `[ exp for value in iterable if condition ]` can be thought of as the list containing all `exp` that can be produced by the `value`s in `iterable` satisfying some `condition`; set/tuple/dictionary comprehensions can be defined similarly