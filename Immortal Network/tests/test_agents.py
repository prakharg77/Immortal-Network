# tests/test_agents.py
import importlib.util
import os
import sys

def load_agent(relative_path, class_name):
    """Dynamically loads a class from a specific file path."""
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_path, relative_path)
    
    spec = importlib.util.spec_from_file_location(class_name, full_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, class_name)

def test_brain_decision():
    print("🧪 Testing Agent 02: Strategic Brain...")
    try:
        # Load using the direct path to avoid the "02_" naming error
        StrategicBrain = load_agent("agents/02_strategic_brain/brain.py", "StrategicBrain")
        brain = StrategicBrain()
        
        decision = brain.decide_defense("CRITICAL_FAILURE", 0.95)
        
        if any(word in decision for word in ["REROUTE", "REBUILD", "CRITICAL"]):
            print("✅ Brain passed: Correctly identified high-priority threat.")
        else:
            print(f"❌ Brain failed: Decision was '{decision}'")
    except Exception as e:
        print(f"❌ Error loading Brain: {e}")

def test_priority_logic():
    print("\n🧪 Testing Agent 08: Priority Scheduler...")
    try:
        PriorityScheduler = load_agent("agents/08_priority_scheduler/scheduler.py", "PriorityScheduler")
        scheduler = PriorityScheduler()
        
        services = ["Internal_Chat", "Primary_Database"]
        plan = scheduler.get_recovery_order(services)
        
        if plan[0]['name'] == "Primary_Database":
            print("✅ Scheduler passed: Database prioritized over Chat.")
        else:
            print(f"❌ Scheduler failed: {plan[0]['name']} was first.")
    except Exception as e:
        print(f"❌ Error loading Scheduler: {e}")

if __name__ == "__main__":
    test_brain_decision()
    test_priority_logic()