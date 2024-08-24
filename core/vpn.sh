#!/bin/bash

read -p "Enter the time (in seconds): " t
servers=("JP" "NL" "US")

while true; do
  i=$(($RANDOM % ${#servers[@]}))
  
  # Disconnect from any current VPN session
  if ! protonvpn-cli d; then
    echo "Failed to disconnect from ProtonVPN. Exiting."
    exit 1
  fi
  
  # Connect to a random server
  if ! protonvpn-cli c --cc ${servers[$i]}; then
    echo "Failed to connect to ProtonVPN server ${servers[$i]}. Exiting."
    exit 1
  fi
  
  echo "Sleeping for $t seconds"
  sleep $t
done