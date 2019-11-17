
import math
import sys
import time
from grove.adc import ADC
import datetime
from moisture.wrapper import *
from wrapper import *
from logger import *

__all__ = ["GroveMoistureSensor"]


class GroveMoistureSensor:
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def moisture(self):
        value = self.adc.read_voltage(self.channel)
        return value


Grove = GroveMoistureSensor


def main():
    try:
        from db import Context
        from grove.helper import SlotHelper

        context = Context()
        sh = SlotHelper(SlotHelper.ADC)
        pin = sh.argv2pin()

        sensor = GroveMoistureSensor(pin)

        print('Detecting moisture...')
        while True:
            m = sensor.moisture
            if m >= 0 and m < 300:
                result = 'Dry'
            elif m >= 300 and m < 600:
                result = 'Moist'
            else:
                result = 'Wet'
            print('Moisture value: {0}, {1}'.format(m, result))
            data = {
                "moisture": m,
                "date": datetime.datetime.now()
            }
            write_result = context.add("RPI-health", data)
            if write_result != None:
                print(str(data))
            else:
                pass

            interval = get_interval(context)
            time.sleep(interval)
    except Exception as e:
        print(str(e))
        error_id = save_error_log(e, "Health/moisture.py", "...")
        data = {
            "success": False,
            "error": error_id
        }
        context.add("RPI-moisture", data)
        time.sleep(interval)


if __name__ == '__main__':
    main()


def get_interval(context):
    from logger import save_error_log
    try:
        result = context.get('rpi-setting', "healthCheckPeriod")['value']
        return int(result)
    except Exception as e:
        save_error_log(e, "health.py", "get_interval")
        return 60
