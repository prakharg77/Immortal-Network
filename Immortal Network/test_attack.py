# test_attack.py
import importlib.util
import os
import sys

def load_agent(relative_path, class_name):
    """Dynamically loads a class from a specific file path."""
    # Get the absolute path to the file
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, relative_path)
    
    # Load the module
    spec = importlib.util.spec_from_file_location(class_name, full_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Return the class
    return getattr(module, class_name)

def simulate_attack():
    print("🔥 MANUAL ATTACK TRIGGERED...")

    try:
        # Manually loading the agents because of the numbered folder names
        PulseMonitor = load_agent("agents/01_pulse_monitor/monitor.py", "PulseMonitor")
        ForensicGhost = load_agent("agents/05_forensic_ghost/analyzer.py", "ForensicGhost")

        monitor = PulseMonitor()
        ghost = ForensicGhost()

        # 1. Force a bad pulse
        bad_pulse = {"status": "CRITICAL_FAILURE", "level": 0.99}
        print(f"📡 Monitor Reporting: {bad_pulse['status']}")

        # 2. Force the Ghost to investigate
        ghost.capture_evidence(bad_pulse['status'], "Manual stress test trigger")
        print("✅ Simulation complete. Check your data/logs folder!")

    except Exception as e:
        print(f"❌ ERROR: {e}")
        print("\n💡 TIP: Make sure you are running this from the main project folder.")

if __name__ == "__main__":
    simulate_attack()