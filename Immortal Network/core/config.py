# core/config.py
import os
from dotenv import load_dotenv

# This looks for the .env file at the root of your project
load_dotenv()

class Config:
    # Basic Project Info
    NETWORK_ID = os.getenv("NETWORK_ID", "IMMORTAL_V2_PROD")
    
    # Thresholds for the Strategic Brain (Agent 02)
    THREAT_THRESHOLD = float(os.getenv("MAX_THREAT_THRESHOLD", 0.8))
    
    # Environment Settings
    DEBUG = os.getenv("DEBUG_MODE", "True").lower() == "true"
    
    # File Paths for Agents
    LOG_DIR = "data/logs"
    BACKUP_DIR = "data/backups"

# Create a single instance to be used by all agents
settings = Config()