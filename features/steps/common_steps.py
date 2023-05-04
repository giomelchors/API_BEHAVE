from behave import  Given

from features.pages.login import Login
from features.support.configuration import EMAIL_USER, PASSWORD_USER


@Given('the user has been authenticated')
def step_impl(context):
    context.login = Login()
    context.login.send_login_request(EMAIL_USER, PASSWORD_USER)
