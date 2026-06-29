# Integrated IT/OT Cyber Security & Predictive Telemetry Lab

## Project Objective
This repository models an end-to-end Industrial Internet of Things (IIoT) and Operational Technology (OT) infrastructure pipeline. It bridges physical process telemetry with machine learning predictive anomaly detection, cloud-based SIEM threat hunting, and enterprise executive risk visualization. 

The ultimate goal of this framework is to defend Level 1 industrial control assets against malicious trajectory or parameter modifications while maintaining strict operational visibility across the enterprise.

## Technical Stack & Ecosystem
*   **Industrial/OT Controllers:** PLCnext Engineer logic simulation frameworks, Universal Robots (UR5e) multi-axis trajectory structures.
*   **Predictive Analytics & ML:** Python (`scikit-learn`, `pandas`) running unsupervised `IsolationForest` algorithms to detect subtle operational drift and unauthorized firmware alterations.
*   **Security Operations (SC-200 Domain):** Microsoft Sentinel SIEM tracking logic, Microsoft Defender for IoT configuration matrices, and custom Kusto Query Language (KQL) hunting queries.
*   **Operational Visualization:** Power BI Desktop (Interactive asset health dashboards, telemetry profiling, threat matrix mapping).
*   **Engineering Compliance Standards:** ISA/IEC 62443 network zoning policies, ACSC Essential 8 mitigation frameworks, and AS1100 technical drafting alignment.

---

## Network & Data Flow Architecture

```mermaid
graph TD
    subgraph Enterprise Zone [Level 4/5: Corporate IT & Management]
        A[Cloud Security SIEM: Microsoft Sentinel]
        F[Power BI Executive Security Dashboard]
    end

    subgraph Plant DMZ [Level 3.5: Security Convergence Boundary]
        B[Industrial Security Firewall / Event Ingestion Engine]
        G[Python Predictive ML Anomaly Engine]
    end

    subgraph Control Zone [Level 2/3: Industrial Supervisory Network]
        C[SCADA Master Monitoring Station]
    end

    subgraph Field Zone [Level 0/1: Physical Floor Automation]
        D[PLCnext Industrial Controller] -->|Modbus TCP Protocol| B
        E[UR5e Robotic Manipulator] -->|Continuous Telemetry Logs| B
    end

    B -->|Raw Log Aggregation| G
    G -->|Feature Vectors & ML Prediction Flags| B
    B -->|Enriched Event Data Streams| A
    A -->|Live Ingestion Connectors| F
