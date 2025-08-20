from AUTOMATION.COMMON_AUTOMATION.COMMON_INTEGRATION.common_integration import *
from AUTOMATION.ZERO_YOUTUBE_AUTOMATION.INTEGRATION_MAIN.integration_main import *
from AUTOMATION.ZERO_AUTOMATION_GOOGLE.GOOGLE_INTEGRATION_MAIN.google_integration_main import *
from AUTOMATION.ZERO_BATTERY_AUTOMATION.BATTERY_INTEGRAITON.battery_integration_main import *


def Automation(text):
    youtube_cmd(text)
    google_cmd(text)
    battery_cmd(text)
    common_cmd(text)
