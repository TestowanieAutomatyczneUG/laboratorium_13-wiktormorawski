from behave import *
from src.fizz import FizzBuzz
from assertpy import *
use_step_matcher("re")

@given(u'Fizzbuzz is running')
def step_impl(context):
    context.fizzbuzz = FizzBuzz()

@when(u'I input "-75"')
def step_impl(context):
    context.result = context.fizzbuzz.game(-75)

@then(u'I get "Fizz Buzz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Fizz Buzz")

@when(u'I input "10"')
def step_impl(context):
    context.result = context.fizzbuzz.game(10)


@then(u'I get "Buzz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Buzz")


@when(u'I input "9"')
def step_impl(context):
    context.result = context.fizzbuzz.game(9)


@then(u'I get "Fizz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Fizz")


@when(u'I input "-4"')
def step_impl(context):
    context.result = context.fizzbuzz.game(-4)


@then(u'I get "Not even Fizz"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Not even Fizz")


@when(u'I input "12"')
def step_impl(context):
    context.result = context.fizzbuzz.game("12")


@then(u'I get "Not number Passed""')
def step_impl(context):
    assert_that(context.result).is_equal_to("Not number Passed")
