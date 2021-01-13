from behave import *
from assertpy import *
use_step_matcher("re")

@given(u'two inputs')
def step_impl(context):
    context.inputs = context.text.split(",")


@when(u'word with letters')
def step_impl(context):
    context.result = (len(context.inputs[0]) == len(context.inputs[1]))



@given(u'three inputs')
def step_impl(context):
    context.inputs = context.text.split(",")


@when(u'one word is shorter')
def step_impl(context):
    context.result = (len(context.inputs[0]) == len(context.inputs[1]) and len(context.inputs[1]) == len(context.inputs[2]))

@then(u'returns False')
def step_impl(context):
    assert_that(context.result).is_equal_to(False)


@when(u'their lengths are equal')
def step_impl(context):
    print("CHUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUj", context.inputs)
    context.result = (len(context.inputs[0]) == len(context.inputs[1]) and len(context.inputs[1]) == len(context.inputs[2]))

@then(u'returns True')
def step_impl(context):
    assert_that(context.result).is_equal_to(True)

@when(u'they are null')
def step_impl(context):
    context.result = "Enter correct words"


@then(u'Enter correct words')
def step_impl(context):
    assert_that(context.result).is_equal_to("Enter correct words")


@given(u'two numbers')
def step_impl(context):
    context.inputs = context.text.split(",")


@when(u'their lengths are the same')
def step_impl(context):
    context.result = (len(context.inputs[0]) == len(context.inputs[1]))


@when(u'their lengths are different')
def step_impl(context):
    context.result = (len(context.inputs[0]) == len(context.inputs[1]))


@given(u'nothing')
def step_impl(context):
    context.result = "Enter correct words"

@when(u'they are the same')
def step_impl(context):
    context.result = (len(context.inputs[0]) == len(context.inputs[1]))


@given(u'Nones')
def step_impl(context):
    context.inputs = context.text.split(",")


@given(u'two words')
def step_impl(context):
    context.inputs = context.text.split(",")




