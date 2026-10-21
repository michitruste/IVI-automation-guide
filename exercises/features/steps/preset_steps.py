from behave import when  # noqa: F401  (you'll use it)

# Importing the main suite's steps registers them here too, so "the radio is on" and
# 'the display shows "..."' already work. Don't write them again.
import features.steps.radio_steps  # noqa: F401, E402

# 10.1  Write the step for:  When I select preset 2
#       Use {n:d} so the number arrives as an int, and call context.ivi.radio.select_preset(n).
