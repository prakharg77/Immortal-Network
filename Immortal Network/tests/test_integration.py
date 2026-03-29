# tests/test_integration.py
import importlib.util
import os
import sys

# 1. Helper to load the agent without naming restrictions
def load_agent(relative_path, class_name):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_path, relative_path)
    
    spec = importlib.util.spec_from_file_location(class_name, full_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, class_name)

# 2. Add the root to path so we can find 'core.bus' normally
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.bus import global_bus

def test_bus_communication():
    print("🧪 Testing Nervous System (Core Bus Integration)...")
    
    try:
        # Load PulseMonitor dynamically
        PulseMonitorClass = load_agent("agents/01_pulse_monitor/monitor.py", "PulseMonitor")
        monitor = PulseMonitorClass()
        
        # Trigger a scan which should publish to the global_bus
        print("📡 Triggering Pulse Scan...")
        monitor.run_scan()
        
        # Check history (using the 'history' attribute from our Universal Bus)
        history = global_bus.history
        
        if len(history) > 0:
            print(f"✅ Integration passed: Bus received {len(history)} messages.")
            print(f"   Latest Topic: {history[-1]['topic']}")
            print(f"   Sender: {history[-1]['sender']}")
        else:
            print("❌ Integration failed: Bus is empty after agent action.")
            
    except Exception as e:
        print(f"❌ Integration Error: {e}")

if __name__ == "__main__":
    test_bus_communication()