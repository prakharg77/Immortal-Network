import time
from core.bus import global_bus  # CRITICAL: Connects the scheduler to the UI

class PriorityScheduler:
    def __init__(self):
        self.agent_id = "PriorityScheduler"
        # Service Tiers: 1 is highest priority, 3 is lowest
        self.service_registry = {
            "Emergency_Comms": 1,
            "Primary_Database": 1,
            "User_Authentication": 2,
            "Public_Website": 3,
            "Internal_Chat": 3
        }

    def get_recovery_order(self, affected_services):
        """
        Sorts services so the most important ones are handled first.
        """
        print(f"⚖️  [{self.agent_id}] CALIBRATING RECOVERY ORDER...")
        
        to_recover = []
        for service in affected_services:
            priority = self.service_registry.get(service, 3) 
            to_recover.append({"name": service, "priority": priority})

        # Sort by priority (1 comes before 3)
        sorted_list = sorted(to_recover, key=lambda x: x['priority'])
        
        # 🚀 UI UPDATE: Show the Plan to the judges
        global_bus.publish(
            sender_id="PriorityScheduler",
            topic="RECOVERY_PLAN_READY",
            payload={
                "order": [s['name'] for s in sorted_list],
                "status": "PLANNING_COMPLETE"
            }
        )
        
        print(f"✅ Recovery Plan Ready: {[s['name'] for s in sorted_list]}")
        return sorted_list

    def execute_sequenced_start(self, plan):
        """
        Simulates the step-by-step boot up and updates the UI for each service.
        """
        for service in plan:
            p_label = "CRITICAL" if service['priority'] == 1 else "STANDARD"
            
            # 🚀 UI UPDATE: Let the dashboard "tick" as services come online
            global_bus.publish(
                sender_id="PriorityScheduler",
                topic="SERVICE_BOOT",
                payload={
                    "service": service['name'],
                    "tier": p_label,
                    "status": "BOOTING..."
                }
            )
            
            print(f"🚀 [Booting] {service['name']} (Tier: {p_label})...")
            time.sleep(1.5) # Simulate boot time for visual effect in UI
            
            global_bus.publish(
                sender_id="PriorityScheduler",
                topic="SERVICE_ONLINE",
                payload={
                    "service": service['name'],
                    "status": "ONLINE"
                }
            )
        
        print("🏁 All priority services are back online.")

if __name__ == "__main__":
    scheduler = PriorityScheduler()
    broken = ["Internal_Chat", "Emergency_Comms", "User_Authentication"]
    plan = scheduler.get_recovery_order(broken)
    scheduler.execute_sequenced_start(plan)