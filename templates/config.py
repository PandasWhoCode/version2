import os
import logging
import sys
import json

class BaseConfig:
    """Base configuration class for environment variables."""

    def __init__(self):
        pass
    
    def load_config(self, config_file, env_var):
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                if(not config.get(env_var)):
                    logging.error(f"Missing required environment variable '{env_var}'")
                    sys.exit(1)
            return config.get(env_var)
        
        except Exception as e:
            logging.error(f"Failed to load configuration: {e}")
            return None

    @classmethod
    def get(self, key: str, default=None):
        """Retrieve an environment variable dynamically."""
        return getattr(self, key, default)
    
class VersionTwoConfig(BaseConfig):
    """SecretDetector configuration class for environment variables."""

    # SECRETS VARIABLES
    GITHUB_PAT = getattr("GITHUB_PAT")

    # LOGGER VARIABLES
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    
    def __init__(self):
        # GITHUB VARIABLES
        self.GITHUB_ORGS = super().load_config(self.CONFIG_FILE, "GITHUB_ORGS")
        self.GITHUB_TOKEN = super().load_config(self.CONFIG_FILE, "GITHUB_TOKEN")

        # SLACK VARIABLES
        self.SLACK_BOT_TOKEN = super().load_config(self.CONFIG_FILE, "SLACK_BOT_TOKEN")
        self.SLACK_CHANNEL_ID = super().load_config(self.CONFIG_FILE, "SLACK_CHANNEL_ID")