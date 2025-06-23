def fibonacci(x):
    if x < 0:
        return None
    if x == 0:
        return 0
    if x == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, x + 1):
        a, b = b, a + b
    return b

def test_fibonacci():
    assert fibonacci(-1) is None
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

