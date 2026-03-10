import importlib.metadata
import os
import sys


def check_dependencies() -> bool:
    """Check for required packages and return True if all are present."""
    required = {
        "pandas": "Data manipulation",
        "requests": "Network access",
        "matplotlib": "Visualization",
        "numpy": "Numerical computations"
    }

    print("Checking dependencies:")
    all_present = True

    for pkg, desc in required.items():
        try:
            version = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({version}) - {desc} ready")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {pkg} - {desc} is NOT installed")
            all_present = False

    return all_present


def perform_analysis():
    """Perform data processing and visualization after dependency check."""
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    n_points = 1000
    print(f"Processing {n_points} data points...")

    time = np.linspace(0, 10, n_points)
    signal = np.sin(time) + np.random.normal(0, 0.2, n_points)

    df = pd.DataFrame({'time': time, 'code_stream': signal})

    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df['code_stream'], color='#00FF41', linewidth=0.7)

    plt.title("NEURAL KINETICS: SIGNAL ANALYSIS", color='#00FF41', fontsize=14)
    plt.gcf().set_facecolor('black')
    plt.gca().set_facecolor('black')
    plt.gca().grid(color='#003300')
    plt.tick_params(colors='#00FF41')

    filename = "matrix_analysis.png"
    plt.savefig(filename)
    print("Analysis complete!")
    print(f"Results saved to: {filename}")


def main():
    """Run the main system check and signal analysis."""
    print("LOADING STATUS: Loading programs...")

    if not check_dependencies():
        print("\nERROR: Systems not synchronized. Missing packages.")
        sys.exit(1)

    try:
        perform_analysis()
    except Exception as e:
        print(f"CRITICAL ERROR: Matrix glitch - {e}")
        sys.exit(1)

    print("\n[SYSTEM REPORT]")
    is_venv = sys.prefix != sys.base_prefix
    is_poetry = os.path.exists("poetry.lock") or "POETRY_ACTIVE" in os.environ
    if is_poetry:
        env_type = "Isolated (Poetry)"
        manager = "Poetry"
    elif is_venv:
        env_type = "Isolated (venv/pip)"
        manager = "Standard Pip"
    else:
        env_type = "Global (Unsafe)"
        manager = "Standard Pip"

    print(f"Environment: {env_type}")
    print(f"Dependency Manager: {manager}")


if __name__ == "__main__":
    main()
