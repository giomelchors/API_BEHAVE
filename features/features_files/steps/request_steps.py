from behave import when, then, given, use_step_matcher

from features.pages.request_page import RequestPage

use_step_matcher("re")


@given("the user has been authenticated")
def step_impl(context):
    context.request_page = RequestPage()
    context.request_page.send_login_request()


@when("the user search all the user of the page")
def step_impl(context):
    context.request_page = RequestPage()
    context.all_user_info = context.request_page.search_all_users()


@then("the system  should display all the user")
def step_impl(context):
    print(context.all_user_info)
    assert context.all_user_info.status_code == 200, "no son iguales"
