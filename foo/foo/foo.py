"""Module containing dummy function."""


def foo(bar):
    """foo dummy function, takes user input: bar"""
    bar = str(bar)
    print('Function to do something with user input: "%s"' % bar)
    return


if __name__ == "__main__":
    print("Demonstration mode:")
    foo("bar")
