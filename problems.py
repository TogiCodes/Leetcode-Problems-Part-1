

#printing the result of test cases
def print_success(test_name):
    print(f"{test_name}: Pass ✅")
def print_fail(test_name):
    print(f"{test_name}: Fail ❌")

#* First Problem: FizzBuzz

def testFizzBuzz(func):
    #Now we will make test functions for every problem so we can check if our solutions are working!

    #Rules:
    #Given an integer n, return a string array (answer) 1-indexed where:
    #answer[i] == FizzBuzz if i is dividable by three and five 
    #answer[i] == Fizz if i is dividable by 3
    #answer[i] == Buzz if i is dividable by 5

    expected_output = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

    if func(15) == expected_output:
        print_success(func.__name__)
    else:
        print_fail(func.__name__)


def fizzBuzz(n):
    answer = []

    for i in range(1, n+1):
        if i > 2 and i % 3 == 0 and i % 5 != 0:
            answer.append("Fizz") #for three
        elif i > 4 and i % 5 == 0 and i % 3 != 0:
            answer.append("Buzz")
        elif i > 14 and i % 5 == 0 and i % 3 == 0:
            answer.append("FizzBuzz")
        else:
            answer.append(str(i))

    return answer


testFizzBuzz(fizzBuzz)

def test_isPowerOfThree(func):
    #Rules:
    #Given an integer n, return a True if it is a power of three. Otherwise, return False
    #an Integer n is power of three, if there exists an integer x such that n == 3 ** x

    #Now we will make 2 test cases 1 for True and 1 for False to double check our solution

    if func(27) == True and func(26) == False:
        print_success(func.__name__)
    else:
        print_fail(func.__name__)    


def isPowerOfThree(n):
    if n == 1:
        return True

    while (n % 3 == 0):
        n /= 3
    
    return n == 1

test_isPowerOfThree(isPowerOfThree)

#* Last problem: Roman To Integer (Probably the hardest so far)

def test_romanToInt(func):
    #Rules:
    #Roman numerals are repsented by seven different symbols (I, V, X, L, C, D, M)
    #For example: 2 is written like II and 9 is written like IX 

    #Let's generate a new roman number to make sure it works perfectly


    if func("LVIII") == 58 and func("MCMXCIV") == 1994 and func("MMMXC") == 3090:
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
    #I can be placed before V and X to make (4, 9)
    #X can be placed before L and C to make (40, 90)
    #C can be placed before D and M to make (400, 900)
    total = 0
    for index, char in enumerate(string):
        index_before = index - 1
        char_before = string[index_before]
        if index_before == -1:  #to make sure it doesn't loop
            total += dict[char]
        elif char == "V" and char_before == "I":
            total += 3 #because 1 is already added before to make 4
        elif char == "X" and char_before == "I":
            total += 8
        elif char == "L" and char_before == "X":
            total += 30
        elif char == "C" and char_before == "X":
            total += 80
        elif char == "C" and char_before == "D":
            total += 300
        elif char == "M" and char_before == "C":
            total += 800
        else:
            total += dict[char]
    return total

 
test_romanToInt(romanToInt)

#Our solutions work perfectly as you can see :)
#Please don't forget to subsribe to my channel and like the video if you enjoyed it.
#See you in next video


