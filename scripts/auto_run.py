import schedule
import time
import subprocess

schedule.every(1440).minutes.do(subprocess.run, ["python3", "event_fetch.py"])
schedule.every(60).minutes.do(subprocess.run, ["python3", "weather_fetch.py"])
schedule.every(60).minutes.do(lambda: subprocess.run(["python3", "build_live_features.py"]))

while True:
    schedule.run_pending()
    time.sleep(1)

