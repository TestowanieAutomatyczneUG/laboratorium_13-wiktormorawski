class FizzBuzz:
    def game(self, num):
        if(type(num) == int):
            if ((num % 15) == 0):
                return "Fizz Buzz"
            if ((num % 5) == 0):
                return "Buzz"
            if ((num % 3) == 0):
                return "Fizz"
            else:
                return "Not even Fizz"
        else:
            return "Not number Passed"

