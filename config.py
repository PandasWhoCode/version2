import os
import logging
import sys
import json

class BaseConfig:
    """Base configuration class for environment variables."""

    # LOGGER VARIABLES
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

    def __init__(self):
        # SECRETS VARIABLES
        self.GITHUB_PAT = getattr("GITHUB_PAT")
    
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
