

#some functions for test cases
def print_success(test_name):
    print(f"{test_name}:\t Pass ✅")
def print_fail(test_name):
    print(f"{test_name}:\t Fail ❌")

def test_fizzbuzz(func):
    """
    This is a function to make sure our solution is working
    """ 
    expected_output = ["1","2","Fizz","4","Buzz",
    "Fizz","7","8","Fizz","Buzz",
    "11","Fizz","13","14","FizzBuzz"]

    if func(15) == expected_output:
        print_success(func.__name__)
    else:
        print_fail(func.__name__)
    
def fizzbuzz(n):
    list = []
    for i in range(1, n+1):
        if i > 2 and i % 3 == 0 and i % 5 != 0:
            list.append("Fizz")
        elif i > 4 and i % 5 == 0 and i % 3 != 0:
            list.append("Buzz")
        elif i > 14 and i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        else:
            list.append(str(i))
    print(list)
    return list

test_fizzbuzz(fizzbuzz)

def test_isPowerOfThree(func):
    """
    This is a function to make sure our solution is working
    """ 
    if func(27) == True and func(26) == False:
        print_success(func.__name__)
    else:
        print_fail(func.__name__)

def powerOfThree(n):
    if n < 1: return False

    while (n % 3 == 0):
        n /= 3
    return n == 1

test_isPowerOfThree(powerOfThree)


def test_romanToInt(func):
    """
    This is a function to make sure our solution is working
    """     
    if func("LVIII") == 58 and func("MCMXCIV") == 1994:
        print_success(func.__name__)
    else:
        print_fail(func.__name__)

def romanToInt(string):
    dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    }
    total = 0
    for index, char in enumerate(string):
        #checks for two character instances
        new_index = index - 1
        char_before = string[new_index]
        if new_index == -1:
            total += dict[char]
        elif char == "V" and char_before == "I":
            total += 3
        elif char == "X" and char_before == "I":
            total += 8
        elif char == "L" and char_before == "X":
            total += 30
        elif char == "C" and char_before == "X":
            total += 80
        elif char == "D" and char_before == "C":
            total += 300
        elif char == "M" and char_before == "C":
            total += 800
        else:
            total += dict[char]
    return total

test_romanToInt(romanToInt)
