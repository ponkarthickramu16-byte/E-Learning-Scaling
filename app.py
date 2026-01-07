import psutil
import time

def scaling_monitor():
    print("--- EduScale E-Learning Monitoring Started ---")
    while True:
        cpu = psutil.cpu_percent(interval=1)
        print(f"Current Traffic Load: {cpu}%")
        
        if cpu > 70:
            print(f">>> Current Load: {cpu}% | ALERT: High Traffic! Scaling up...")
        elif cpu < 40:  # 20-ku badhula 40 nu mathunga
            print(f">>> Current Load: {cpu}% | Normal Traffic: Running on Minimum Servers.")
        else:
            print(f">>> Current Load: {cpu}% | Moderate Traffic: Monitoring...")
        
        time.sleep(2)

if __name__ == "__main__":
    scaling_monitor()