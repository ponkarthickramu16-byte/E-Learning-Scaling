import psutil
import time

def scaling_monitor():
    print("--- EduScale E-Learning Monitoring Started ---")
    while True:
        cpu = psutil.cpu_percent(interval=1)
        print(f"Current Traffic Load: {cpu}%")
        
        if cpu > 70:
            print(">>> ALERT: High Traffic! Scaling up New Servers...")
        elif cpu < 20:
            print(">>> Normal Traffic: Running on Minimum Servers.")
        
        time.sleep(2)

if __name__ == "__main__":
    scaling_monitor()