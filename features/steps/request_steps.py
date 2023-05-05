from behave import when, then

from features.pages.request_page import RequestPage


@when(u'the user search all the user of the page')
def step_impl(context):
    context.request_page = RequestPage()
    context.all_user_info = context.request_page.search_all_users()


@then(u'the system  should display all the user')
def step_impl(context):
    context.request_page = RequestPage()
