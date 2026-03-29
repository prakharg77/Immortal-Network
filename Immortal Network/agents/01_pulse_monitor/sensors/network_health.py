# agents/01_pulse_monitor/sensors/network_health.py
import random

def get_traffic_load():
    """
    Simulates network traffic. 
    Returns a float between 0.0 (Quiet) and 1.0 (DDoS Attack).
    """
    # In a real app, this would use 'psutil' or 'scapy' to check real traffic
    return round(random.uniform(0.1, 0.95), 2)

def check_server_status():
    """Returns True if server is UP, False if DOWN."""
    statuses = [True, True, True, False] # 25% chance of simulating a crash
    return random.choice(statuses)