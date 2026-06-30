import pandas as pd
import numpy as np

def inject_cyber_attacks(input_file="industrial_telemetry.csv", output_file="anomaly_telemetry.csv"):
    print(f"[*] Ingesting baseline industrial dataset: {input_file}")
    df = pd.read_csv(input_file)
    
    # Explicityly verify the baseline is marked as NORMAL
    df['Operational_Status'] = 'NORMAL'

    print(f"[*] Simulating industrial cyeber-attack injection verctors...")

    # Vector 1: Rapid Trajectory Override (Simulate malicious Modbus write commands)
    # Target 30 random rows between indices 200 and 400 to simulate a cyber-attack
    v1_indices = np.random.choice(range(200, 400), size=30, replace=False)
    for idx in v1_indices:
        df.loc[idx, 'Joint_Velocity_rads'] = round(df.loc[idx, 'Joint_Velocity_rads'] * random_multiplier(2.5, 3.5), 3)
        df.loc[idx, 'Current_Amps'] = round(df.loc[idx, 'Current_Amps'] * random_multiplier(2.0, 3.0), 2)
        df.loc[idx, 'Operational_Status'] = 'ATTACK_MODBUS_OVERRIDE'

    # Vector 2: "Slow-Drift" Thermal Sabotage (Simulate a stealth firmware manipulation)
    # Target a continuous black of rows between indices 700 and 800 to model a creeping thermal curve
    v2_start, v2_end = 700, 800
    for idx in range(v2_start, v2_end):
        # Linearly increase the temperature excess over time to bypass static alarms
        thermal_creep = ((idx - v2_start) / (v2_end -  v2_start)) * 18.5
        df.loc[idx, 'Motor_Temp_C'] = round(df.loc[idx, 'Motor_Temp_C'] + thermal_creep, 2)
        # Even though velcocity stays normal, the relationship to temperature is broken
        df.loc[idx, 'Operational_Status'] = 'ATTACK_THERMAL_DRIFT'

    df.to_csv(output_file, index=False)
    print(f"[+] Success! Cyber threats injeced. Exploded dataset saved to: {output_file}")

def random_multiplier(low, high):
    import random
    return np.random.uniform(low, high)

if __name__ == "__main__":
    inject_cyber_attacks()