import json
import time
import os
from core.bus import global_bus  # CRITICAL: Connects to the UI

class ForensicGhost:
    def __init__(self):
        self.agent_id = "ForensicGhost" # Standard ID for UI grouping
        # Simplified path to work from the project root (where main.py is)
        self.log_path = "data/logs/forensic_evidence.json"
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)

    def capture_evidence(self, threat_type, details):
        """
        Extracts digital fingerprints and sends them to both the file and the Live UI.
        """
        print(f"👻 [{self.agent_id}] Extracting digital fingerprints for: {threat_type}")
        
        evidence = {
            "timestamp": time.strftime("%H:%M:%S"),
            "threat": threat_type,
            "details": details,
            "status": "SECURED_IN_VAULT"
        }

        # 1. LIVE UI UPDATE
        # This makes the "ForensicGhost" row pop up in your Streamlit table
        global_bus.publish(
            sender_id="ForensicGhost",
            topic="EVIDENCE_COLLECTION",
            payload=evidence
        )

        # 2. FILE PERSISTENCE (For the audit trail)
        try:
            with open(self.log_path, "a") as f:
                f.write(json.dumps(evidence) + "\n")
            print(f"✅ Evidence saved to {self.log_path}")
        except Exception as e:
            print(f"❌ Failed to save evidence: {e}")
            
        return evidence

if __name__ == "__main__":
    ghost = ForensicGhost()
    ghost.capture_evidence("HACKATHON_TEST", {"attack_vector": "XSS", "node": "ALPHA_01"})