from pathlib import Path

#store path of important file
root = Path(__file__).resolve().parents[2]
config_path = root / "app" / "config" / "config.json"
cred_path = root / ".secrets" / "healthcare-capstone-service.json"