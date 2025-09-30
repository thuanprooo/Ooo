import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import init, Fore
import time

init(autoreset=True)

# config
INPUT_FILE = "proxies.txt"
OUTPUT_FILE = "live_proxies.txt"
THREADS = 100
TIMEOUT = 5

# lọc
def check_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=TIMEOUT)
        if r.status_code == 200:
            print(f"{Fore.GREEN}[ Live ] {proxy}")
            with open(OUTPUT_FILE, "a") as f:
                f.write(proxy + "\n")
        else:
            print(f"{Fore.RED}[ Die ] {proxy}")
    except:
        print(f"{Fore.RED}[ Die ] {proxy}")

def main():
    with open(INPUT_FILE, "r") as f:
        proxies = [line.strip() for line in f if line.strip()]

    print(f"Tổng proxy : {len(proxies)}\nĐang lọc...\n")
    start = time.time()

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = [executor.submit(check_proxy, proxy) for proxy in proxies]
        for _ in as_completed(futures):
            pass

    end = time.time()
    print(f"\nHoàn thành trong {round(end - start, 2)} giây.")

if __name__ == "__main__":
    main()
