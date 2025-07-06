# setup_check.py
import sys, platform

print("--- Robotics Environment Check ---")
print(f"Executing with Python version: {sys.version}")
print(f"Running on operating system: {platform.system()} ({platform.release()})")

if sys.prefix == sys.base_prefix:
    print("\nWARNING: Not in a venv!")
else:
    print("\nSUCCESS: Running in a Python virtual environment.")

print("\n--- WSL setup complete. Ready to code! ---")