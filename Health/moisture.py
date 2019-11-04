
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
        from grove.helper import SlotHelper
        sh = SlotHelper(SlotHelper.ADC)
        pin = sh.argv2pin()
        pin1 = sh.argv2pin("")

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
            write_to_db(data)
            interval = get_check_interval()
            time.sleep(interval)
    except Exception as e:
        error_id = save_error_log(e, "moisture.py", "...")
        data = {
            "success": False,
            "error": error_id
        }
        write_to_db(data)
        write_to_db(str(data))
        print(str(e))

if __name__ == '__main__':
    main()
