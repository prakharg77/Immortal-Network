import datetime
import json
import os

class MessageBus:
    def __init__(self):
        self.history = []
        self.log_path = "data/logs/system_audit.json"
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        if not os.path.exists(self.log_path):
            with open(self.log_path, "w") as f:
                json.dump([], f)

    def publish(self, sender_id, topic, payload):
        message = {
            "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
            "sender": sender_id,
            "topic": topic,
            "data": payload
        }
        
        self.history.append(message)
        
        # Keep only last 50 for UI performance
        try:
            with open(self.log_path, "w") as f:
                json.dump(self.history[-50:], f, indent=4)
        except Exception as e:
            print(f"❌ Bus Write Error: {e}")

        # Terminal Feedback
        print(f"📡 [{sender_id}] -> {topic}")
        return message

global_bus = MessageBus()