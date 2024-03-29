A context manager is a Python object that provides extra contextual information to an action. This extra information takes the form of running a callable upon initiating the context using the with statement, as well as running a callable upon completing all the code inside the with block. The most well known example of using a context manager is shown here, opening on a file:

with open('file.txt') as f:
    contents = f.read()

Anyone familiar with this pattern knows that invoking open in this fashion ensures that f’s close method will be called at some point. This reduces a developer’s cognitive load and makes the code easier to read.

There are two easy ways to implement this functionality yourself: using a class or using a generator. Let’s implement the above functionality ourselves, starting with the class approach:

[open-file.py]


This is just a regular Python object with two extra methods that are used by the with statement. CustomOpen is first instantiated and then its __enter__ method is called and whatever __enter__ returns is assigned to f in the as f part of the statement. When the contents of the with block is finished executing, the __exit__ method is then called.

And now the generator approach using Python’s own contextlib:

[context-lib.py]


This works in exactly the same way as the class example above, albeit it’s more terse. The custom_open function executes until it reaches the yield statement. It then gives control back to the with statement, which assigns whatever was yield’ed to f in the as f portion. The finally clause ensures that close() is called whether or not there was an exception inside the with.

Since the two approaches appear the same, we should follow the Zen of Python to decide when to use which. The class approach might be better if there’s a considerable amount of logic to encapsulate. The function approach might be better for situations where we’re dealing with a simple action.

