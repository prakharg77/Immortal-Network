# agents/01_pulse_monitor/monitor.py
import random
import time
from core.bus import global_bus  # <--- Essential Import

class PulseMonitor:
    def __init__(self):
        self.agent_id = "AGENT_01_MONITOR"

    def run_scan(self):
        """
        Simulates checking server health and traffic.
        Returns a 'pulse' dictionary.
        """
        # Simulate a random threat (90% chance it's fine, 10% chance of attack)
        threat_roll = random.random()
        
        status = "HEALTHY"
        level = 0.1
        
        if threat_roll > 0.9:
            status = "DDoS_ATTACK"
            level = 0.95
        elif threat_roll > 0.8:
            status = "MALWARE_BREACH"
            level = 0.85

        pulse_data = {"status": status, "level": level}

        # 📡 PUBLISH TO THE BUS
        # This is what triggers the rest of the 10-agent chain
        global_bus.publish(
            sender_id=self.agent_id, 
            topic="SYSTEM_HEALTH_UPDATE", 
            payload=pulse_data
        )
        
        return pulse_data

if __name__ == "__main__":
    monitor = PulseMonitor()
    while True:
        monitor.run_scan()
        time.sleep(3)