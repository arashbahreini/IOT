def execute_healt(context):
    import time
    import sys
    import os
    from health_information import provide_info
    from logger import save_error_log

    sys.path.append(
        "/home/arash/work/IOT/Health/venv/lib/python3.7/site-packages/")
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

    count = 0
    while True:
        count += 1
        if count >= 10:
            os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
            count = 0
        try:
            interval = get_interval(context)
            data = provide_info()
            write_result = context.add("RPI-health", data)
            if write_result != None:
                print(str(data))
            else:
                pass

            if interval == None:
                interval = 2

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

def get_interval(context):
    from logger import save_error_log
    try:
        result = context.get('rpi-setting', "healthCheckPeriod")['value']
        return int(result)
    except Exception as e:
        save_error_log(e,"health.py","get_interval")
        return 60
