#!/bin/bash

# Initialize ProtonVPN CLI
sudo protonvpn-cli init

# Prompt user for ProtonVPN credentials
echo "Please enter your ProtonVPN credentials:"
read -p "Username: " username
read -sp "Password: " password
echo

# Log in to ProtonVPN
echo $password | sudo protonvpn-cli login $username

# Set the connection protocol (OpenVPN UDP is recommended)
sudo protonvpn-cli config -p udp

# Set the default server (optional, you can choose a specific server or let it auto-connect)
sudo protonvpn-cli config -f

# Confirm the setup
echo "ProtonVPN CLI has been initialized and configured."