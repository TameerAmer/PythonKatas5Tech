
def do_n_times(func, n):
    """
    Executes the given function n times.

    Args:
        func: the function to execute
        n: the number of times to execute the function
    """
    global counter
    counter = 0  
    for f in range(n):
        counter+=1
        func()
    return counter


def say_hello():
    """A function that prints 'Hello!'."""
    print("Hello!")


def print_message():
    """A function that prints 'Python is fun!'."""
    print("Python is fun!")


if __name__ == '__main__':
    print("Calling function 3 times:")
    do_n_times(say_hello, 3)

    print("Calling another function 5 times:")
    do_n_times(print_message, 5)

    # Expected output:
    # Calling function 3 times:
    # Hello!
    # Hello!
    # Hello!
    # Calling another function 5 times:
    # Python is fun!
    # Python is fun!
    # Python is fun!
    # Python is fun!
    # Python is fun!