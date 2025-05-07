import os

def get_env_variable(key, default=None):
    """Retrieve environment variables with a default fallback."""
    return os.getenv(key, default)