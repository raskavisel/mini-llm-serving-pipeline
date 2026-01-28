THRESHOLD_LATENCY = 2.0

def is_drift_detected(avg_latency):
    return avg_latency > THRESHOLD_LATENCY
