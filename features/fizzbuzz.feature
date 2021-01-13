Feature: Fizzbuzz


    Scenario: OutPut FizzBuzz
        Given Fizzbuzz is running
        When I input "-75"
        Then I get "Fizz Buzz"
        
    Scenario: OutPut Buzz
        Given Fizzbuzz is running
        When I input "10"
        Then I get "Buzz"

    Scenario: OutPut Fizz
        Given Fizzbuzz is running
        When I input "9"
        Then I get "Fizz"

    Scenario: OutPut not in Fizz Buzz
        Given Fizzbuzz is running
        When I input "-4"
        Then I get "Not even Fizz"

    Scenario: Input not int
        Given Fizzbuzz is running
        When I input "12"
        Then I get "Not number Passed""