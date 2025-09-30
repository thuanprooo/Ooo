import asyncio
import aiohttp
import aiofiles
import random
import time
from colorama import Fore, init
import requests

init(autoreset=True)

COMMON_PORTS = [80, 8080, 3128, 1080, 8000, 8888, 443]
CONCURRENT_IPS = 1000        # Tăng IP quét mỗi vòng
CONCURRENT_PORTS = 1000       # Số task cùng lúc
TIMEOUT = 0.5               # Timeout ngắn hơn để tăng tốc
SAVE_EVERY = 10

live_proxies = []
proxy_lock = asyncio.Lock()
semaphore = asyncio.Semaphore(CONCURRENT_PORTS)
output_file = "live.txt"

headers_list = [
    'Mozilla/5.0', 'Chrome/90.0', 'Safari/537.36', 'Edge/91.0', 'Opera/9.80'
]

def get_country(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=2).json()
        if res['status'] == 'success':
            return res.get('country')
    except:
        return None

async def check_proxy(ip, port):
    proxy = f"http://{ip}:{port}"
    async with semaphore:
        try:
            conn = aiohttp.ClientTimeout(total=TIMEOUT)
            headers = {'User-Agent': random.choice(headers_list)}
            async with aiohttp.ClientSession(timeout=conn, headers=headers) as session:
                start = time.perf_counter()
                async with session.get("http://httpbin.org/ip", proxy=proxy) as resp:
                    if resp.status == 200:
                        elapsed = time.perf_counter() - start
                        if elapsed < 1:
                            country = get_country(ip)
                            async with proxy_lock:
                                entry = f"{ip}:{port} - {country}" if country else f"{ip}:{port}"
                                live_proxies.append(entry)
                                print(Fore.GREEN + f"[LIVE] {entry} ({elapsed:.2f}s)")
                                if len(live_proxies) >= SAVE_EVERY:
                                    await save_proxies()
        except:
            pass

async def save_proxies():
    global live_proxies
    async with aiofiles.open(output_file, mode='a') as f:
        for proxy in live_proxies:
            await f.write(proxy + '\n')
    print(Fore.CYAN + f"==> Saved {len(live_proxies)} proxies to {output_file}")
    live_proxies = []

async def scan_ip(ip):
    tasks = [check_proxy(ip, port) for port in COMMON_PORTS]
    await asyncio.gather(*tasks)

def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

async def main():
    while True:
        tasks = []
        for _ in range(CONCURRENT_IPS):
            ip = generate_ip()
            tasks.append(scan_ip(ip))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Đã dừng bằng tay.")
