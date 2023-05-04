from behave import when, then

from features.pages.request_page import RequestPage


@when(u'the user search all the user of the page')
def step_impl(context):
    context.request_page = RequestPage()


@then(u'the system  should display all the user')
def step_impl(context):
    context.request_page = RequestPage()
