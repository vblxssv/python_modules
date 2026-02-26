import sys
import os
import site

def get_venv_status() -> str | None:
    """Returns the name of the venv if active, otherwise None."""
    # Standard check for virtual environment
    if sys.prefix != sys.base_prefix:
        return os.path.basename(sys.prefix)
    return None

def main() -> None:
    venv_name: str | None = get_venv_status()
    current_python: str = sys.executable

    if venv_name:
        # Scenario: Inside the virtual environment
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        # Displaying the first site-packages directory found
        print(site.getsitepackages()[0])
    else:
        # Scenario: Global environment
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("  python -m venv matrix_env")
        print("  source matrix_env/bin/activate  # On Unix")
        print("  matrix_env\\Scripts\\activate      # On Windows")
        print("\nThen run this program again.")

if __name__ == "__main__":
    main()
