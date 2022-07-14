
def fizzbuzz(num):
    i = 0
    while i <= num:
        divByThree = (i % 3 == 0)
        divByFive = (i % 5 == 0)
        if divByThree and divByFive:
            print("FizzBuzz")
        elif divByThree and not divByFive:
            print("Fizz")
        elif divByFive and not divByThree:
            print("Buzz")
        else:
            print(i)
        i += 1
        


fizzbuzz(100)