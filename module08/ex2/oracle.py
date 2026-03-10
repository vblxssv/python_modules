import os
from dotenv import load_dotenv


def check_security(script_path: str) -> None:
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    bad_pattern_1 = 'API_KEY' + ' = "'
    bad_pattern_2 = 'DATABASE_URL' + ' = "'
    if content.count(bad_pattern_1) > 1 or content.count(bad_pattern_2) > 1:
        print("[WARN] Potential hardcoded secrets detected!")
    else:
        print("[OK] No hardcoded secrets detected")


def main():
    """Load and validate system configuration from environment variables."""
    env_found = load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...")

    mode = os.getenv("MATRIX_MODE", "unknown")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_lvl = os.getenv("LOG_LEVEL", "INFO")
    zion_url = os.getenv("ZION_ENDPOINT")

    if not all([db_url, api_key, zion_url]):
        print("\n[WARNING] Configuration incomplete! Variables missing.")
        print("Ensure .env is configured or environment variables are set.")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if db_url:
        db_status = ("Connected to local instance" if "localhost" in db_url
                     else "Connected to production cluster")
    else:
        db_status = "Not configured"

    print(f"Database: {db_status}")
    print(f"API Access: {'Authenticated' if api_key else 'Access Denied'}")
    print(f"Log Level: {log_lvl}")
    print(f"Zion Network: {'Online' if zion_url else 'Offline'}")

    print("\nEnvironment security check:")
    check_security(os.path.abspath(__file__))

    env_msg = 'properly configured' if env_found else 'not found'
    print(f"[{'OK' if env_found else '!!'}] .env file {env_msg}")

    is_prod = mode == "production"
    prod_msg = 'active' if is_prod else 'available'
    print(f"[{'OK' if is_prod else '--'}] Production overrides {prod_msg}")

    if mode == "unknown":
        print("\nThe Oracle is blind without MATRIX_MODE.")
    else:
        print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
