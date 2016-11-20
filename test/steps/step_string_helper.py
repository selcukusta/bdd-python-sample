from behave import given, when, then
from nose.tools import assert_equals
from app.StringHelper import StringHelper
 
@given(u'StringHelper sinifindan kopya olusturacagim')
def create_string_helper_instance(context):
    context.string_helper = StringHelper()
 
 
@when(u'RemoveDiacritics metoduna parametre olarak "{literal}" ve "{to_lower}" gececegim')
def step_fire_process(context, literal, to_lower):
    context.result = context.string_helper.remove_diacritics(literal, to_lower)
 
 
@then(u'Sonuc "{result}" seklinde olmali')
def show_result(context, result):
    actual_result = context.result
    assert_equals(result, actual_result)