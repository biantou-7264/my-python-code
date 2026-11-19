from bleak import BleakScanner, BleakClient
import asyncio, sys


def scan_devices_sync(timeout=5):
    async def _scan():
        devices = await BleakScanner.discover(timeout=timeout)

        unique = {}
        for dev in devices:
            addr = dev.address
            name = dev.name if dev.name else '未知设备'
            if addr not in unique or (name != '未知设备'):
                unique[addr] = name

        device_list = [(addr, name) for addr, name in unique.items()]
        device_list.sort(key=lambda x: x[1])
        return device_list

    return asyncio.run(_scan())


def connect_device_sync(addr, timeout=10):
    async def _connect():
        try:
            client = BleakClient(addr, timeout=timeout)
            await client.connect()

            if client.is_connected:
                services = await client.services
                device_info = await client.get_device_name() if hasattr(client, 'get_device_name') else 'Unknown'
                await client.disconnect()
                return True, len(services), device_info
            return False, 0, None
        except Exception as e:
            return False, 0, str(e)

    success, service_count, info = asyncio.run(_connect())
    return success, service_count, info


if __name__ == '__main__':
    print('正在扫描...')
    devices = scan_devices_sync(timeout=10)
    print('\n' + '=' * 55)
    print(f'{'序号':<6} {'设备名称':<32} {'MAC地址'}')
    print('-' * 50)
    for idx, (addr, name) in enumerate(devices, 1):
        display_name = name[:30] + '..' if len(name) > 32 else name
        print(f'{idx:<6} {display_name:<32} {addr}')
    print('=' * 50)
    while True:
        try:
            choice = input(f'\n选择设备 (1-{len(devices)}，0退出): ')
            if choice == '0':
                print('退出')
                sys.exit()

            idx = int(choice)
            if 1 <= idx <= len(devices):
                selected = devices[idx - 1]
                break
            else:
                print(f'请输入 1-{len(devices)}')
        except ValueError:
            print('请输入数字')

    print(f"\n连接 {selected[1]} ...")
    success, service_count, info = connect_device_sync(selected[0])

    if success:
        print(f"连接成功！发现 {info} 个服务")
    else:
        print(f"连接失败: {info}")
