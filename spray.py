import asyncio
from bleak import BleakClient

ADDRESS = "A4:C1:38:C6:2C:47"
CHAR_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

# 16-byte verified spray command
SPRAY_CMD = bytes([
    0xbf, 0x62, 0x6d, 0x54, 0x18, 0x68, 0x62, 0x6d, 
    0x4e, 0x18, 0x9a, 0x62, 0x72, 0x49, 0x00, 0xff
])

async def trigger_spray():
    async with BleakClient(ADDRESS) as client:
        if client.is_connected:
            await client.write_gatt_char(CHAR_UUID, SPRAY_CMD, response=False)

if __name__ == "__main__":
    asyncio.run(trigger_spray())