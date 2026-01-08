import psutil
import time

def scaling_monitor():
    print("--- EduScale E-Learning Monitoring Started ---", flush=True) # flush=True add pannunga
    while True:
        cpu = psutil.cpu_percent(interval=1)
        print(f"Current Traffic Loading : {cpu}%", flush=True)
        
        if cpu > 70:
            print(">>> ALERT: High Traffic! Scaling up...", flush=True)
        elif cpu < 40:
            print(">>> Normal Traffic: Minimum Servers.", flush=True)
        
        time.sleep(1) # Interval-ah 1 second-ah kammi pannunga

if __name__ == "__main__":
    scaling_monitor()