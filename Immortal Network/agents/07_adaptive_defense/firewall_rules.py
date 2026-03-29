import time
from core.bus import global_bus  # CRITICAL: Connects the firewall to the UI

class AdaptiveDefense:
    def __init__(self):
        self.agent_id = "AdaptiveDefense"
        self.active_blocklist = []
        self.security_level = "Standard"

    def apply_new_rule(self, attacker_data):
        """
        Receives data from Forensic Ghost and updates firewall rules in real-time.
        """
        ip_to_block = attacker_data.get("attacker_ip")
        
        if ip_to_block and ip_to_block not in self.active_blocklist:
            print(f"🛡️  [{self.agent_id}] ADAPTING SHIELDS...")
            
            # Simulate firewall update delay
            time.sleep(1)
            self.active_blocklist.append(ip_to_block)
            
            # Escalate security level based on volume
            if len(self.active_blocklist) > 3:
                self.security_level = "High Lockdown"

            # 🚀 UI UPDATE: Let the judges see the "Wall" going up
            global_bus.publish(
                sender_id="AdaptiveDefense",
                topic="FIREWALL_UPDATE",
                payload={
                    "status": "IP_BLOCKED",
                    "blocked_ip": ip_to_block,
                    "total_blocked": len(self.active_blocklist),
                    "protection_mode": self.security_level
                }
            )
            
            print(f"✅ Rule deployed. {ip_to_block} is now blacklisted.")
            return True
        return False

    def reset_rules(self):
        """Clears the firewall (used after a full Ghost Rebuild)."""
        self.active_blocklist = []
        self.security_level = "Standard"
        
        global_bus.publish(
            sender_id="AdaptiveDefense",
            topic="FIREWALL_RESET",
            payload={"status": "BASELINE_RESTORED"}
        )
        print(f"🔄 [{self.agent_id}] Firewall rules reset to baseline.")

if __name__ == "__main__":
    shield = AdaptiveDefense()
    shield.apply_new_rule({"attacker_ip": "192.168.1.105", "threat": "DDoS"})