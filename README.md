🚀 Getting Started
1. Find your Device MAC Address
To control your specific unit, you need its unique hardware address. You can find this in two ways:

From the Godrej aer App: Open the app, go to your paired device, and look for the MAC Address (e.g., A4:C1:38:C6:2C:47) in the Settings or Device Info menu.

Using a Scanner: If the app is unavailable, use nRF Connect or a similar BLE scanner to find the address of the device broadcasting as Smart Matic.

2. Configure the Script
In the provided spray.py file, locate the ADDRESS variable at the top and replace the placeholder with your retrieved address:

Python
# Replace with your specific device address
ADDRESS = "XX:XX:XX:XX:XX:XX" 
3. Execution
Ensure your phone's Bluetooth is OFF (the device only allows one connection at a time) and run:

Bash
pip install bleak
python spray.py
⚙️ Technical Details
Library: Built using bleak for cross-platform BLE support.

Payload: Uses a verified 16-byte handshake for newer firmware versions.

Target: Commands are sent to the TX characteristic (...0003) using write_without_response.
