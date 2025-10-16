import asyncio
from bleak import discover

async def discover_devices():
    devices = await discover()
    for device in devices:
        print(f"设备地址: {device.address} - 设备名: {device.name}")

asyncio.run(discover_devices())
