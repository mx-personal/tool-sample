import toolkit


def func_foo(x, y, z):
    return toolkit.add(x, toolkit.mult(y, z))


def script_foo():
    print(func_foo(18, 2, 50))


if __name__ == "__main__":
    print(script_foo())
