import csv
import random
from datetime import datetime, timedelta

def generate_baseline_data(filename="industrial_telemetry.csv", num_records=1000):
    # Standard baseline physical parameters for the automated system
    base_temp = 42.5       # Target baseline motor temperature in Celsius
    base_velocity = 1.2    # Target baseline joint velocity in rad/s
    base_current = 4.1     # Target baseline motor current draw in Amps
    
    start_time = datetime.now() - timedelta(days=1)
    
    fieldnames = [
        "Timestamp", "Asset_ID", "IP_Address", 
        "Motor_Temp_C", "Joint_Velocity_rads", "Current_Amps", 
        "Operational_Status"
    ]
    
    print(f"[*] Initializing baseline industrial data generation engine...")
    
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(num_records):
            # Advance logs sequentially by 30 seconds
            current_timestamp = (start_time + timedelta(seconds=i * 30)).strftime("%Y-%m-%d %H:%M:%S")
            
            # Inject natural white-noise variance to represent real-world sensors
            temp_noise = random.uniform(-1.5, 1.5)
            vel_noise = random.uniform(-0.05, 0.05)
            curr_noise = random.uniform(-0.2, 0.2)
            
            # Simulate a very slight linear heat rise over a continuous runtime cycle
            heating_factor = (i / num_records) * 2.0 
            
            writer.writerow({
                "Timestamp": current_timestamp,
                "Asset_ID": "UR5e_ARM_01",
                "IP_Address": "192.168.10.25",
                "Motor_Temp_C": round(base_temp + temp_noise + heating_factor, 2),
                "Joint_Velocity_rads": round(base_velocity + vel_noise, 3),
                "Current_Amps": round(base_current + curr_noise, 2),
                "Operational_Status": "NORMAL"
            })
            
    print(f"[+] Success! Generated {num_records} baseline log lines saved to: {filename}")

if __name__ == "__main__":
    generate_baseline_data()