# Topic: Why documentation matters (docstring)
def add(a, b):
    """Return the sum of a and b."""  # docstring explains the function
    return a + b
print(add(2, 3))
print(add.__doc__)  # reading the documentation
