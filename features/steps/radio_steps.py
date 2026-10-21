from behave import given, step, then, when


@given("the infotainment system is powered on")
def step_power_on(context):
    context.ivi.boot()                        # context.ivi made in environment.py


@given("the radio is on")
def step_radio_on(context):
    context.ivi.radio.power_on()


@when("I tune to {freq:g} MHz")               # {freq:g} arrives as a float; also matches "0"
def step_tune(context, freq):
    context.ivi.radio.tune(freq)


@step('the display shows "{text}"')           # @step matches Then and And
def step_display(context, text):
    assert context.ivi.display.text == text, context.ivi.display.text


@then('I see the error "{message}"')
def step_error(context, message):
    assert context.ivi.display.error == message
