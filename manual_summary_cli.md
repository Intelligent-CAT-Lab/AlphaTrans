# Summary of bugs in Commons-CLI
This document provides a summary of the translation bugs in Commons-CLI, which were manually fixed for achieving 100% test success.

1. **Incorrect use of static fields**.

In Java, even if instance fields are initialized outside of a constructor, they are still initialized at the beginning of the constructor in the bytecode. During translation, all field declarations in Java are translated to static fields in Python. Eventually when the constructor is called, the static fields are masked by the instance fields of the same name if the field was initialized in the constructor. Otherwise all methods continue to use the static field. This ususually works when the fields are of _simple_ datatypes.

However this does not work if the instance fields are of mutable types like lists, are initialized outside the constructor, and are then modified by instance methods. Doing so changes the value of the static field and since all instances share the same static field, the value of the field is changed for all instances. The fix for this was to move such fields inside the constructor.

This occured in `CommandLine`, `OptionGroup`, `Option`, `Options`.

2. Usage of `configparser.ConfigParser` instead of `dict()` for Java `Properties`. This occured in `CommandLine`.

3. **Erroneous logic in overloaded methods**

Some overloaded methods that are supposed to simply make a call to another overloaded method with a default value, contained some erroneous logic (like checking for `None` or throwing some exceptions, etc.). 

This occured in `DefaultParser`, `OptionGroup`, `TypeHandler`.

4. While translating Java code for comparing two strings for equality without case sensitivity, the LLM placed `.casefold` method on the wrong string. For example, instead of `variable.casefold() == "constant"`, it produced `"constant".casefold() == variable`. This occured in `DefaultParser`.

5. Use of incorrect variable while calling a method. This led to very subtle bugs since both the variables were defined in the same scope and had the same type. This occured in `DefaultParser`, `GnuParser`.

6. Incorrect looping logic. This involves cases where there is additional logic related to modifying the loop variable inside the loop, besides the basic increment step. This occured in `GnuParser`.

7. Incorrectly assuming the existence of methods in Python that are present in Java, like `String.compareTo`. This occured in `HelpFormatter`.

8. Use of comparators for sorting, while a key-function was expected. The fix was to use `functools.cmp_to_key`. Moreover a comparator class can only be used if it is callable, and so the fix was to add a `__call__` method to the comparator class. This occured in `HelpFormatter`.

9. Missing field declarations. This occured in `HelpFormatter`.

10. Interchangeably using `str` and `StringIO`. This lead to some deeper bugs in the caller code too, where it sometimes assumed methods to be pure instead of making changes in place. This occured in `HelpFormatter`.

11. Logical errors, like using `!=` instead of `==`. This occured in `HelpFormatter`.

12. Using `\n` instead of `os.linesep`. This occured in `HelpFormatter`.

13. Incorrectly using `StringIO` instead of `sys.stdout`. This occured in `HelpFormatter`.

14. Incorrectly initializing string fields with `""` instead of `None`. This also led to some subtle bugs in the caller code, where it assumed the unset fields to be `""` instead of `None`. This occured in `Option`.

15. Missing local imports. This occured in `OptionGroup`.

16. Adding a `__str__` and `__eq__` methods which call `toString` and `equals` respectively. The former is executed implicitly in functions involving printing of the object. The latter is executed implicitly while checking for containment in lists, etc. This occured in `Option`, `Options`.

17. Java `char` and `int` can interconvert seamlessly, but in Python the LLM accidentally applied `ord` on the character (which was actually `str`) in order to convert it to `int`. However this was not expected by the caller. This occured in `Option`.

18. Incorrect field names, for example missing leading underscores, or not taking mangling into account. This occured in `Option`.

19. Incorrectly wrapping lists with `typing.Collections`. This is an abstract class and cannot be instantiated. This was unnecessary and the fix was to remove the wrapping. This occured in `Options`.

20. Implementing a `BiDirectionalIterator` class for `Parser`, since the logic involving the iterator required the ability to step back.

21. Incorrect looping logic in loops involving iterators, where termination depends on `hasNext` in Java. The fix is to catch the `StopIteration` exception in Python. This occured in `Parser`.

22. Incorrect use of `io.FileIO` instead of `io.TextIOWrapper`. This occured in `PatternOptionBuilder`.

23. Incorrect use of `datetime.date` instead of `datetime.datetime`. This occured in `PatternOptionBuilder`.

24. Using the constant `"1"` instead of `"!"`. This occured in `PatternOptionBuilder`.

25. Implemented and added a metaclass `GlobalStateSync` to `TypeHandler` in order to synchronize the namespace with the caller code.

26. Added URL validation logic to `TypeHandler` to simulate the Java `URL` class which raises `MalfomedURLExeption` on invalid URLs.

27. Include the `builtins` while finding classes from their string names, in `TypeHandler`.

28. The LLM sometimes implemented unimplemented methods which were simply supposed to throw `NotImplementedError`. This occured in `TypeHandler`.
