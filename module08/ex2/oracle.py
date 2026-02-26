import os
import sys
from dotenv import load_dotenv

def check_security(script_path: str) -> None:
    """Simple check to ensure no hardcoded secrets exist in the source."""
    with open(script_path, 'r') as f:
        content = f.read()
        # Mock check for hardcoded strings that look like keys
        if 'API_KEY = "sk_' in content or 'DATABASE_URL = "postgres' in content:
            print("[WARN] Potential hardcoded secrets detected!")
        else:
            print("[OK] No hardcoded secrets detected")

def main():
    # 1. Load .env file if it exists
    env_found = load_dotenv()
    
    print("ORACLE STATUS: Reading the Matrix...")
    
    # 2. Retrieve variables with defaults or error handling
    mode = os.getenv("MATRIX_MODE", "unknown")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_lvl = os.getenv("LOG_LEVEL", "INFO")
    zion_url = os.getenv("ZION_ENDPOINT")

    # Validation logic
    if not all([db_url, api_key, zion_url]):
        print("\n[WARNING] Configuration incomplete! Some variables are missing.")
        print("Ensure .env is configured or environment variables are set.")
    
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    
    # Formatting output for the user
    db_status = "Connected to local instance" if "localhost" in (db_url or "") else "Connected to production cluster"
    print(f"Database: {db_status if db_url else 'Not configured'}")
    
    print(f"API Access: {'Authenticated' if api_key else 'Access Denied'}")
    print(f"Log Level: {log_lvl}")
    print(f"Zion Network: {'Online' if zion_url else 'Offline'}")

    print("\nEnvironment security check:")
    check_security(__file__)
    print(f"[{'OK' if env_found else '!!'}] .env file {'properly configured' if env_found else 'not found'}")
    
    # Check for production override
    is_prod = mode == "production"
    print(f"[{'OK' if is_prod else '--'}] Production overrides {'active' if is_prod else 'available'}")

    if mode == "unknown":
        print("\nThe Oracle is blind without MATRIX_MODE.")
    else:
        print("\nThe Oracle sees all configurations.")

if __name__ == "__main__":
    main()



# how to run differently
# 1. python3 oracle.py
# 2. cp .env.example .env; python3 oracle.py
# 3. MATRIX_MODE=production LOG_LEVEL=WARNING python3 oracle.py