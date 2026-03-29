import time
import random
from core.bus import global_bus  # CRITICAL: Connects the traps to the UI

class DeceptionAgent:
    def __init__(self):
        self.agent_id = "DeceptionMesh"
        self.active_traps = []

    def deploy_trap(self, trap_type="Fake_DB"):
        """
        Creates a decoy service to distract attackers and updates the UI.
        """
        trap_id = f"DECOY_{random.randint(100, 999)}"
        port = random.choice([8080, 21, 3306, 22])
        
        print(f"🎭 [{self.agent_id}] DEPLOYING TRAP: {trap_id} ({trap_type})")
        
        trap_details = {
            "id": trap_id,
            "type": trap_type,
            "port": port,
            "status": "ACTIVE_BAIT"
        }
        
        self.active_traps.append(trap_details)

        # 🚀 UI UPDATE: Show the "Bait" being set
        global_bus.publish(
            sender_id="DeceptionMesh",
            topic="TRAP_DEPLOYED",
            payload=trap_details
        )
        
        print(f"🪤  Trap is live on Port {port}. Waiting for unauthorized interaction...")
        return trap_details

    def alert_on_intrusion(self, trap_id):
        """
        Called when a 'hacker' touches the decoy. Updates UI with the Alert.
        """
        print(f"🚨 [ALERT] TRAP TRIGGERED: {trap_id} is being accessed!")
        
        # 🚀 UI UPDATE: Make the dashboard show a red alert for the trap
        global_bus.publish(
            sender_id="DeceptionMesh",
            topic="INTRUSION_ALERT",
            payload={
                "trap_id": trap_id,
                "status": "ATTACKER_TRAPPED",
                "mode": "TARPIT_DELAY"
            }
        )

        # Simulate a "Tarpit" (slowing the attacker down)
        for i in range(3):
            print(f"  ...sending fake data packet {i+1}...")
            time.sleep(1)
            
        return "ATTACKER_DELAYED_SUCCESSFULLY"

if __name__ == "__main__":
    deceiver = DeceptionAgent()
    my_trap = deceiver.deploy_trap("Admin_Portal_Decoy")
    deceiver.alert_on_intrusion(my_trap['id'])