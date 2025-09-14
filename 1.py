import os
import requests
import concurrent.futures
import time
from datetime import datetime
from colorama import Fore, Style, init
from tqdm import tqdm
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

init(autoreset=True)
console = Console()

# ====== BANNER ======
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    console.print(Panel.fit(
        "[bold cyan]🌌 TRẦN HÀO DEV[/bold cyan] | [bold red]TEAM DARKSTACK[/bold red]\n"
        "[yellow]📌 TELE: [green]@Haomilknn[/green][/yellow]",
        title="[bold magenta]BLACKNET PROXY TOOL[/bold magenta]",
        border_style="cyan"
    ))

    menu = Table(show_header=True, header_style="bold magenta")
    menu.add_column("Số", style="cyan", width=5)
    menu.add_column("Chức năng", style="green")
    menu.add_row("1", "Thu nhập proxy → ghi vào file")
    menu.add_row("2", "Check proxy từ file → lưu kết quả")
    menu.add_row("3", "Thu nhập + Check → nhập file lưu")
    menu.add_row("4", "Auto Refresh (lặp lại)")
    console.print(menu)

# ====== NGUỒN PROXY ======
SOURCES = [
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt"
]

# ====== GHI LOG ======
def write_log(total, good, out_file):
    with open("proxy_log.txt", "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}] Tổng: {total} | Sống: {good} | File: {out_file}\n")

# ====== HÀM THU NHẬP ======
def fetch_proxies(out_file):
    proxies = []
    for url in SOURCES:
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                proxies.extend(r.text.strip().split("\n"))
        except:
            pass
    proxies = list(set([p.strip() for p in proxies if p.strip()]))
    with open(out_file, "w") as f:
        for p in proxies:
            f.write(p + "\n")
    console.print(f"📥 Thu được [yellow]{len(proxies)}[/yellow] proxy (lưu ở {out_file})")
    return proxies

# ====== HÀM CHECK ======
def check_proxy(proxy):
    test_url = "http://httpbin.org/ip"
    try:
        r = requests.get(test_url, proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=3)
        if r.status_code == 200:
            return proxy
    except:
        return None

def filter_proxies(in_file, out_file):
    if not os.path.exists(in_file):
        console.print(f"[red]❌ Không tìm thấy file {in_file}[/red]")
        return
    with open(in_file) as f:
        proxy_list = [line.strip() for line in f if line.strip()]

    good = []
    console.print(f"⚡ Đang kiểm tra [cyan]{len(proxy_list)}[/cyan] proxy...\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = list(tqdm(executor.map(check_proxy, proxy_list), total=len(proxy_list), desc="🔍 Checking", unit="proxy"))
        for res in results:
            if res:
                good.append(res)

    with open(out_file, "w") as f:
        for proxy in good:
            f.write(f"{proxy}\n")

    console.print(Panel.fit(
        f"✅ Lọc xong, còn [green]{len(good)}[/green] proxy sống\n💾 Lưu ở [bold]{out_file}[/bold]",
        border_style="green"
    ))

    write_log(len(proxy_list), len(good), out_file)

# ====== AUTO REFRESH ======
def auto_refresh(interval_min=10, out_file="good_proxies.txt"):
    while True:
        banner()
        console.print(f"♻️ [yellow]Auto Refresh sau mỗi {interval_min} phút[/yellow]\n")
        proxies = fetch_proxies(out_file.replace("good_", "all_"))
        filter_proxies(out_file.replace("good_", "all_"), out_file)
        console.print(f"⏳ Đợi [magenta]{interval_min} phút[/magenta] rồi chạy lại...\n")
        time.sleep(interval_min * 60)

# ====== MAIN MENU ======
if __name__ == "__main__":
    banner()
    choice = input(Fore.CYAN + "👉 Nhập lựa chọn (1/2/3/4): " + Style.RESET_ALL).strip()

    if choice == "1":
        out_file = input("💾 Nhập tên file để lưu proxy thu được (.txt): ").strip()
        if out_file == "":
            out_file = "all_proxies.txt"
        fetch_proxies(out_file)

    elif choice == "2":
        in_file = input("📂 Nhập file chứa proxy cần check (.txt): ").strip()
        out_file = input("💾 Nhập file để lưu proxy sống (.txt): ").strip()
        if out_file == "":
            out_file = "good_proxies.txt"
        filter_proxies(in_file, out_file)

    elif choice == "3":
        out_file_all = input("💾 Nhập file lưu proxy thô (.txt): ").strip()
        if out_file_all == "":
            out_file_all = "all_proxies.txt"
        fetch_proxies(out_file_all)

        out_file_good = input("💾 Nhập file lưu proxy sống (.txt): ").strip()
        if out_file_good == "":
            out_file_good = "good_proxies.txt"
        filter_proxies(out_file_all, out_file_good)

    elif choice == "4":
        try:
            interval = int(input(Fore.CYAN + "⏱️ Nhập số phút auto refresh: " + Style.RESET_ALL).strip())
        except:
            interval = 10
        out_file_good = input("💾 Nhập file lưu proxy sống khi auto refresh (.txt): ").strip()
        if out_file_good == "":
            out_file_good = "good_proxies.txt"
        auto_refresh(interval, out_file_good)

    else:
        console.print("[red]❌ Lựa chọn không hợp lệ![/red]")
