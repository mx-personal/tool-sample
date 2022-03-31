import tool.core.toolkit as toolkit


def func_foo(x, y, z):
    return toolkit.add(x, toolkit.mult(y, z))


def script_foo():
    print(func_foo(1, 3, 5))


