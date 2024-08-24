
sudo apt install -y openvpn dialog python3-pip python3-setuptools
sudo pip3 install protonvpn-cli


# Download the latest version of geckodriver
GECKODRIVER_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep 'tag_name' | cut -d\" -f4)
wget "https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz"

# Extract the downloaded archive
tar -xvzf "geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz"

# Move the geckodriver binary to /usr/local/bin
sudo mv geckodriver /usr/local/bin/

# Make geckodriver executable
sudo chmod +x /usr/local/bin/geckodriver

# Clean up
rm "geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz"