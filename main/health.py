

def execute_healt():
    import time
    import sys
    import os
    from db import Context
    from health_information import provide_info
    from logger import save_error_log

    sys.path.append(
        "/home/arash/work/IOT/Health/venv/lib/python3.7/site-packages/")
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

    count = 0
    context = Context()
    while True:
        count += 1
        if count >= 10:
            os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
            count = 0
        try:
            interval = context.get('rpi-setting/-LtJuVPbvUAVAtqkc5MT/healthCheckPeriod')
            data = provide_info()
            write_result = context.add("RPI-health", data)
            if write_result != None:
                print(str(data))
            else:
                print("Health error")
            time.sleep(interval)
        except Exception as e:
            print(str(e))
            error_id = save_error_log(e, "Health/main.py", "...")
            data = {
                "success": False,
                "error": error_id
            }
            context.add("RPI-health", data)
            time.sleep(interval)
