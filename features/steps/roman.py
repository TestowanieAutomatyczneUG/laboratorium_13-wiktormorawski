from behave import *
from src.roman import Roman
from assertpy import *
use_step_matcher("re")

@given(u'Roman is running')
def step_impl(context):
    context.roman = Roman()

@when(u'I input "3"')
def step_impl(context):
    context.result = context.roman.roman(3)

@then(u'I get "III"')
def step_impl(context):
    assert_that(context.result).is_equal_to("III")


@when(u'I input "7"')
def step_impl(context):
    context.result = context.roman.roman(7)


@then(u'I get "VII"')
def step_impl(context):
    assert_that(context.result).is_equal_to("VII")


@when(u'I input "13"')
def step_impl(context):
    context.result = context.roman.roman(13)


@then(u'I get "XIII"')
def step_impl(context):
    assert_that(context.result).is_equal_to("XIII")



@when(u'I input "50"')
def step_impl(context):
    context.result = context.roman.roman(50)


@then(u'I get "L"')
def step_impl(context):
    assert_that(context.result).is_equal_to("L")



@when(u'I input "49"')
def step_impl(context):
    context.result = context.roman.roman(49)


@then(u'I get "XLIX"')
def step_impl(context):
    assert_that(context.result).is_equal_to("XLIX")



@when(u'I input "70"')
def step_impl(context):
    context.result = context.roman.roman(70)


@then(u'I get "LXX"')
def step_impl(context):
    assert_that(context.result).is_equal_to("LXX")



@when(u'I input "-50"')
def step_impl(context):
    context.result = context.roman.roman(-50)


@then(u'I get "Please pass positive number"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Please pass positive number")


@when(u'I input "wiktor"')
def step_impl(context):
    context.result = context.roman.roman("wiktor")


@then(u'I get "Please pass correct arabic number"')
def step_impl(context):
    assert_that(context.result).is_equal_to("Please pass correct arabic number")

