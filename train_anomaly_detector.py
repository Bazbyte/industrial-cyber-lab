import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix

def train_and_evaluate():
    print("[*] Loading compromised industrial dataset for model training...")
    df = pd.read_csv("anomaly_telemetry.csv")
    
    # 1. Feature Selection: Train the model ONLY on the pyhsical telemetry variables)
    # We strip out timestamps, IDs, and the ground-truth labels to the model has to rely on pure physics
    features =["Motor_Temp_C", "Joint_Velocity_rads", "Current_Amps"]
    X = df[features]

    print("[*] Training Unsupervised Isolation Forest Anomaly Detection Engine...")
    # Initialise model with an estimated contamination level representing our expected anomaly ratio around 13%
    model = IsolationForest(contamination=0.13, random_state=42)
    model.fit(X)

    # 2. Predict Anomalies: The model will label each row as either -1 (anomaly) or 1 (normal)
    predictions = model.predict(X)

    # Map predictions back to our human-readable strings for clear reporting
    # If the model says -1, we flag it as an predicted anomaly
    df['Predicted_Status'] = ['ANOMALY' if pred == -1 else 'NORMAL' for pred in predictions]

    # 3. Validation and Metrics Comparison
    # Create a binary mapping to mathematically evluate our detection accuracy
    df['True_Binary'] = df['Operational_Status'].apply(lambda x: 1 if x != 'NORMAL' else 0)
    df['Pred_Binary'] = df['Predicted_Status'].apply(lambda x: 1 if x == 'ANOMALY' else 0)

    print("\n" + "="*50)
    print("     OT CYBER OPERATIONS SECURITY INTEGRITY MATRIX")
    print("="*50)
    print("\n[+] Confusion Matrix:")
    print(confusion_matrix(df['True_Binary'], df['Pred_Binary']))

    print("\n[+] Detailed Analytics Report:")
    print(classification_report(df['True_Binary'], df['Pred_Binary'], target_names=['Normal State', 'Cyber Attack']))

    # Save the processed predictions so Microsoft Sentinel or Power BI can ingest them later
    df.to_csv("predicted_telemetry.csv", index=False)
    print("[+] Enriched telemetry dataset saved to: predicted_telemetry.csv")

if __name__ == "__main__":
    train_and_evaluate()