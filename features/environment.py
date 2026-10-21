import re

from ivi.system import InfotainmentSystem


def before_all(context):
    context.config.setup_logging()


def before_scenario(context, scenario):
    context.ivi = InfotainmentSystem(simulated=True)    # fresh system per scenario


def after_scenario(context, scenario):
    if scenario.status.name == "failed":
        safe_name = re.sub(r"\W+", "_", scenario.name)  # no spaces or <> in file names
        context.ivi.save_screenshot(f"reports/{safe_name}.txt")
    context.ivi.shutdown()
