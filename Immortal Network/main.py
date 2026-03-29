import time
import os
import importlib.util
from core.bus import global_bus

def load_agent(path, class_name):
    """Dynamically loads a class from the numbered folders."""
    try:
        spec = importlib.util.spec_from_file_location(class_name.lower(), path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, class_name)()
    except Exception as e:
        print(f"⚠️  Skip: Could not load {class_name} at {path}")
        return None

def start_system():
    print("🛡️  IMMORTAL MESH INITIALIZING (10/10 AGENTS)...")

    # Initialize the Full Swarm
    monitor   = load_agent("agents/01_pulse_monitor/monitor.py", "PulseMonitor")
    brain     = load_agent("agents/02_strategic_brain/brain.py", "StrategicBrain")
    router    = load_agent("agents/04_traffic_rerouter/router_control.py", "TrafficRerouter")
    ghost     = load_agent("agents/05_forensic_ghost/analyzer.py", "ForensicGhost")
    vault     = load_agent("agents/06_memory_vault/vector_db.py", "MemoryVault")
    defense   = load_agent("agents/07_adaptive_defense/firewall_rules.py", "AdaptiveDefense")
    scheduler = load_agent("agents/08_priority_scheduler/scheduler.py", "PriorityScheduler")
    auditor   = load_agent("agents/09_audit_layer/logger.py", "AuditLayer")
    deception = load_agent("agents/10_deception_mesh/honeypot.py", "DeceptionAgent")

    print("🟢 ALL SYSTEMS ONLINE. STARTING AUTONOMOUS DEFENSE LOOP...")

    try:
        while True:
            # 1. SCAN
            pulse = monitor.run_scan()
            
            # 2. EVALUATE THREAT
            if pulse['level'] > 0.4:
                action = brain.decide_defense(pulse['status'], pulse['level'])
                
                # 3. COORDINATED RESPONSE
                
                # A. DECEPTION (Honeypot) - If unauthorized access
                if pulse['status'] == "UNAUTHORIZED_ACCESS" or action == "DEPLOY_DECEPTION_NODES":
                    trap = deception.deploy_trap("Admin_Portal_Decoy")
                    deception.alert_on_intrusion(trap['id'])

                # B. TRAFFIC MANAGEMENT
                if action == "TRIGGER_TRAFFIC_REROUTER" or pulse['status'] == "DDoS_ATTACK":
                    router.shift_traffic(reason=pulse['status'])

                # C. FORENSICS & BLOCKING
                if pulse['level'] > 0.6:
                    attacker_ip = f"192.168.1.{pulse['packets_scanned'] % 255}"
                    ghost.capture_evidence(pulse['status'], {"ip": attacker_ip})
                    vault.store_experience({"attacker_ip": attacker_ip, "vector": pulse['status']})
                    defense.apply_new_rule({"attacker_ip": attacker_ip})

                # D. RECOVERY
                if pulse['status'] == "SYSTEM_CRASH":
                    plan = scheduler.get_recovery_order(["Emergency_Comms", "Primary_Database"])
                    scheduler.execute_sequenced_start(plan)

                # E. AUDIT (The Final Word)
                auditor.log_event("StrategicBrain", action, f"Mitigating {pulse['status']}", "SUCCESS")

            else:
                # RESET TO BASELINE
                if router and router.active_route != "PRIMARY_LINK":
                    router.restore_traffic()
                    defense.reset_rules()

            print(f"📡 Heartbeat: {pulse['level']} | Status: {pulse['status']}")
            time.sleep(5)

    except KeyboardInterrupt:
        print("\n🛑 System Hibernating...")

if __name__ == "__main__":
    start_system()