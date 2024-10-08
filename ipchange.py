import os
import subprocess
import time


splash = """

 Built for Educational and testing Purposes only
 Built By [Bichitra-Linux]

 support the Project on:
 https://github.com/bichitra-linux
"""
print(splash)
time.sleep(3)


# Ask the user if they want to run the setup script
run_setup = input("Do you want to run the setup script? (yes/no): ").strip().lower()

if run_setup == 'yes':
    try:
        subprocess.run(["bash", "core/setup.sh"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running setup.sh: {e}")
        exit(1)
else:
    print("Setup script was not run.")

time.sleep(1)
os.system("clear")
print(splash)

# Prompt user for initialization
op = input("Did you already initialize it (Y/n) :").strip().lower()
if op == "n":
    try:
        subprocess.run(["bash", "core/init.sh"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running init.sh: {e}")
        exit(1)

# Run vpn.sh script
try:
    subprocess.run(["bash", "core/vpn.sh"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error occurred while running vpn.sh: {e}")
    exit(1)