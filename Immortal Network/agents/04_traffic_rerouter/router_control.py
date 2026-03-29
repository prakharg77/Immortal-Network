import time
from core.bus import global_bus  # CRITICAL: Added for UI sync

class TrafficRerouter:
    def __init__(self):
        self.agent_name = "TrafficRerouter" # Removed space for consistent ID
        self.active_route = "PRIMARY_LINK"
        self.backup_link = "SECURE_SHADOW_LINK_B"

    def shift_traffic(self, reason="Maintenance"):
        """
        Moves traffic from Primary to Backup and updates the UI.
        """
        # 1. Logic & Terminal Feedback
        print(f"🔀 [{self.agent_name}] SHIFTING TRAFFIC: {self.active_route} -> {self.backup_link}")
        time.sleep(1) # Simulate routing delay
        
        self.active_route = self.backup_link

        # 2. UI UPDATE (This makes the bar charts and table move)
        global_bus.publish(
            sender_id="TrafficRerouter",
            topic="NETWORK_REROUTE",
            payload={
                "status": "DIVERSION_ACTIVE",
                "active_route": self.active_route,
                "reason": reason,
                "link_health": "STABLE"
            }
        )
        
        print(f"✅ SUCCESS: All users now on {self.active_route}.")
        return True

    def restore_traffic(self):
        """
        Moves traffic back to Primary and updates the UI.
        """
        print(f"🔄 [{self.agent_name}] RESTORING TRAFFIC to PRIMARY_LINK...")
        time.sleep(1)
        self.active_route = "PRIMARY_LINK"

        # 3. UI UPDATE (Show the recovery)
        global_bus.publish(
            sender_id="TrafficRerouter",
            topic="NETWORK_RESTORE",
            payload={
                "status": "NORMAL_OPERATIONS",
                "active_route": self.active_route,
                "reason": "Threat Neutralized"
            }
        )
        print("✅ SUCCESS: Network flow returned to normal.")

if __name__ == "__main__":
    router = TrafficRerouter()
    router.shift_traffic("DDoS Attack Detected")