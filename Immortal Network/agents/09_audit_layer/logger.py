import json
import time
import os
from core.bus import global_bus  # CRITICAL: Connects the auditor to the UI

class AuditLayer:
    def __init__(self):
        self.agent_id = "AuditLayer"
        # Adjusted path to work from the project root (where main.py is)
        self.audit_log_path = "data/logs/system_audit.json"
        
        # Ensure the logs directory exists
        os.makedirs(os.path.dirname(self.audit_log_path), exist_ok=True)

    def log_event(self, agent_id, action, reasoning, outcome="SUCCESS"):
        """
        Records a specific action taken by any agent and pushes it to the Live UI.
        """
        entry = {
            "timestamp": time.strftime("%H:%M:%S"),
            "agent": agent_id,
            "action_taken": action,
            "reasoning": reasoning,
            "outcome": outcome
        }

        print(f"📜 [{self.agent_id}] RECORDING: {agent_id} performed {action}")
        
        # 1. LIVE UI UPDATE
        # This sends the "Official Record" to the dashboard
        global_bus.publish(
            sender_id="AuditLayer",
            topic="OFFICIAL_AUDIT_LOG",
            payload=entry
        )

        # 2. PERSISTENCE (Writing to the same file the UI reads from)
        try:
            logs = self._load_logs()
            logs.append(entry)
            # Keep only the last 50 logs to prevent the UI from slowing down
            with open(self.audit_log_path, 'w') as f:
                json.dump(logs[-50:], f, indent=4)
        except Exception as e:
            print(f"❌ Audit Logging Error: {e}")

    def _load_logs(self):
        if not os.path.exists(self.audit_log_path):
            return []
        try:
            with open(self.audit_log_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

if __name__ == "__main__":
    # Test the Auditor
    auditor = AuditLayer()
    auditor.log_event(
        agent_id="StrategicBrain",
        action="TRIGGER_REROUTE",
        reasoning="Critical threat detected in Node Alpha",
        outcome="VERIFIED"
    )