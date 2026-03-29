import json
import os
from core.bus import global_bus

class StrategicBrain:
    def __init__(self):
        self.agent_id = "02_STRATEGIC_BRAIN"
        self.strategy_path = "strategies.json"
        self.strategies = self.load_strategies()

    def load_strategies(self):
        if os.path.exists(self.strategy_path):
            with open(self.strategy_path, "r") as f:
                return json.load(f)
        return {}

    def decide_defense(self, threat_type, level):
        # Look up the threat in your JSON
        # Default to a generic response if the specific threat isn't found
        strategy = self.strategies.get(threat_type, {
            "description": "Unknown threat detected.",
            "primary_action": "MONITOR",
            "secondary_action": "LOG_EVENT",
            "priority": "LOW"
        })

        decision_data = {
            "analysis": strategy["description"],
            "primary": strategy["primary_action"],
            "secondary": strategy["secondary_action"],
            "priority": strategy["priority"],
            "threat_level": level
        }

        # Publish to the UI so the judges see the "Plan"
        global_bus.publish(
            sender_id="StrategicBrain",
            topic="STRATEGY_EXECUTION",
            payload=decision_data
        )

        return strategy["primary_action"]