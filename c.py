import os
import time
import requests
import threading
from termcolor import colored
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

# Danh sách từ khóa cho VPN/Datacenter (bạn có thể mở rộng thêm)
VPN_DATACENTER_KEYWORDS = [
    # Các nhà cung cấp cloud và datacenter phổ biến
    'Amazon', 'DigitalOcean', 'OVH', 'Vultr', 'Linode', 'Hetzner', 'LeaseWeb',
    'Alibaba Cloud', 'Google Cloud', 'Microsoft Azure', 'IBM Cloud', 'Oracle Cloud',
    'Scaleway', 'Equinix', '1&1 IONOS', 'Contabo', 'PhoenixNAP', 'Hostwinds', 'DreamHost',
    'Rackspace', 'Liquid Web',
    # Các nhà cung cấp VPN nổi tiếng
    'NordVPN', 'ExpressVPN', 'Surfshark', 'Private Internet Access', 'ProtonVPN',
    'CyberGhost', 'IPVanish', 'TorGuard', 'Hotspot Shield', 'Windscribe', 'TunnelBear',
    'Mullvad', 'IVPN', 'SaferVPN', 'Hide.me', 'PrivateVPN', 'VyprVPN', 'ZenMate', 'PureVPN',
    # Một số từ khóa liên quan đến hạ tầng mạng và Tier 1
    'AT&T', 'CenturyLink', 'Lumen', 'NTT', 'Tata Communications', 'Deutsche Telekom', 'Orange'
]

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def filter_duplicates(proxies):
    return list(set(proxy.strip() for proxy in proxies if proxy.strip()))

def check_website_access(proxy, url, timeout=4):
    """ Kiểm tra xem proxy có thể truy cập trang web url không """
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=timeout)
        return response.status_code == 200
    except:
        return False

def check_captcha_access(proxy, timeout=4):
    """
    Kiểm tra proxy có thể sử dụng với CAPTCHA không.
    Ví dụ: request đến một endpoint của reCAPTCHA (chỉ mang tính chất minh họa).
    """
    captcha_url = "https://www.google.com/recaptcha/api2/anchor"  # Endpoint của reCAPTCHA
    try:
        response = requests.get(captcha_url, proxies={"http": proxy, "https": proxy}, timeout=timeout)
        return response.status_code == 200
    except:
        return False

def get_latency(proxy, url="https://ipinfo.io/json", timeout=4):
    """ Đo thời gian phản hồi (latency) khi request đến url """
    try:
        start = time.time()
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=timeout)
        latency = time.time() - start
        if response.status_code == 200:
            return round(latency, 2)
        return None
    except:
        return None

def process_proxy(proxy):
    """
    Hàm xử lý cho 1 proxy.
    Trả về 1 dict với các kết quả của proxy:
      - 'proxy': proxy
      - 'live': True/False
      - 'google': True/False
      - 'facebook': True/False
      - 'youtube': True/False
      - 'captcha': True/False
      - 'vpn_dc': True/False (dựa trên từ khóa trong ISP)
      - 'latency': latency (hoặc None)
      - 'country', 'city', 'isp': thông tin từ ipinfo.io
    """
    result = {
        'proxy': proxy,
        'live': False,
        'google': False,
        'facebook': False,
        'youtube': False,
        'captcha': False,
        'vpn_dc': False,
        'latency': None,
        'country': None,
        'city': None,
        'isp': None
    }
    try:
        response = requests.get("https://ipinfo.io/json", proxies={"http": proxy, "https": proxy}, timeout=4)
        if response.status_code != 200:
            return result
        data = response.json()
        result['country'] = data.get("country", "Unknown")
        result['city'] = data.get("city", "Unknown")
        isp = data.get("org", "Unknown")
        result['isp'] = isp
        result['live'] = True

        result['latency'] = get_latency(proxy)

        result['google'] = check_website_access(proxy, "https://www.google.com/")
        result['facebook'] = check_website_access(proxy, "https://www.facebook.com/")
        result['youtube'] = check_website_access(proxy, "https://www.youtube.com/")
        result['captcha'] = check_captcha_access(proxy)
        # Kiểm tra VPN/Datacenter dựa trên từ khóa trong ISP
        if any(keyword.lower() in isp.lower() for keyword in VPN_DATACENTER_KEYWORDS):
            result['vpn_dc'] = True
    except Exception as e:
        # Bỏ qua lỗi cho proxy này
        pass
    return result

def perform_check(proxies, num_threads, round_number):
    unique_proxies = filter_duplicates(proxies)
    results = []
    
    # Dùng ThreadPoolExecutor để xử lý song song
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_proxy = {executor.submit(process_proxy, proxy): proxy for proxy in unique_proxies}
        for future in as_completed(future_to_proxy):
            res = future.result()
            results.append(res)

    # Phân loại kết quả
    live_proxies = [r['proxy'] for r in results if r['live']]
    google_live_proxies = [r['proxy'] for r in results if r['google']]
    facebook_live_proxies = [r['proxy'] for r in results if r['facebook']]
    youtube_live_proxies = [r['proxy'] for r in results if r['youtube']]
    captcha_usable_proxies = [r['proxy'] for r in results if r['captcha']]
    vpn_dc_proxies = [r['proxy'] for r in results if r['vpn_dc']]
    proxy_latency = {r['proxy']: r['latency'] for r in results if r['latency'] is not None}

    # Thống kê địa chỉ, ISP
    country_counter = Counter(r['country'] for r in results if r['country'])
    city_counter = Counter(r['city'] for r in results if r['city'])
    isp_counter = Counter(r['isp'] for r in results if r['isp'])

    # Đường dẫn file kết quả (sử dụng số vòng)
    result_folder = "result"
    os.makedirs(result_folder, exist_ok=True)
    all_filename = os.path.join(result_folder, f"all{round_number}.txt")
    google_filename = os.path.join(result_folder, f"google_live{round_number}.txt")
    facebook_filename = os.path.join(result_folder, f"facebook_live{round_number}.txt")
    youtube_filename = os.path.join(result_folder, f"youtube_live{round_number}.txt")
    captcha_filename = os.path.join(result_folder, f"captcha_usable{round_number}.txt")
    vpndc_filename = os.path.join(result_folder, f"vpn_datacenter{round_number}.txt")
    latency_filename = os.path.join(result_folder, f"latency{round_number}.txt")

    # Lưu kết quả
    with open(all_filename, "w") as f:
        f.write("\n".join(set(live_proxies)) + "\n")
    with open(google_filename, "w") as f:
        f.write("\n".join(set(google_live_proxies)) + "\n")
    with open(facebook_filename, "w") as f:
        f.write("\n".join(set(facebook_live_proxies)) + "\n")
    with open(youtube_filename, "w") as f:
        f.write("\n".join(set(youtube_live_proxies)) + "\n")
    with open(captcha_filename, "w") as f:
        f.write("\n".join(set(captcha_usable_proxies)) + "\n")
    with open(vpndc_filename, "w") as f:
        f.write("\n".join(set(vpn_dc_proxies)) + "\n")
    with open(latency_filename, "w") as f:
        for proxy, latency in proxy_latency.items():
            f.write(f"{proxy} - {latency}s\n")

    # Tổng hợp proxy VIP (nếu có)
    vip_proxies = set(google_live_proxies) | set(facebook_live_proxies) | set(youtube_live_proxies) | set(captcha_usable_proxies) | set(vpn_dc_proxies)
    if vip_proxies:
        vip_filename = os.path.join(result_folder, f"vip{round_number}.txt")
        with open(vip_filename, "w") as f:
            f.write("\n".join(vip_proxies) + "\n")
        print(f"[INFO] Proxy VIP đã lưu vào {vip_filename}.")

    # In ra thông báo [INFO]
    print(f"[INFO] Proxy sống đã lưu vào {all_filename}.")
    print(f"[INFO] Proxy có thể truy cập Google đã lưu vào {google_filename}.")
    print(f"[INFO] Proxy có thể truy cập Facebook đã lưu vào {facebook_filename}.")
    print(f"[INFO] Proxy có thể truy cập YouTube đã lưu vào {youtube_filename}.")
    print(f"[INFO] Proxy sử dụng được với CAPTCHA đã lưu vào {captcha_filename}.")
    print(f"[INFO] Proxy thuộc VPN/Datacenter đã lưu vào {vpndc_filename}.")
    print(f"[INFO] Thông tin latency đã lưu vào {latency_filename}.")

    debug_info = {
        "UI": "2.0",
        "Version": "2.5",
        "Countries": list(country_counter.keys()),
        "Cities": list(city_counter.keys()),
        "ISPs": list(isp_counter.keys()),
        "Total Live Proxies": len(live_proxies),
        "Google Live": len(google_live_proxies),
        "Facebook Live": len(facebook_live_proxies),
        "YouTube Live": len(youtube_live_proxies),
        "CAPTCHA Usable": len(captcha_usable_proxies),
        "VPN/Datacenter": len(vpn_dc_proxies)
    }
    print(debug_info)
    print(f"[INFO] Kết thúc vòng {round_number}.")

def chunked_file_reader(file_path, chunk_size=10000):
    """ Đọc file theo từng chunk để tiết kiệm bộ nhớ """
    with open(file_path, "r") as f:
        chunk = []
        for line in f:
            chunk.append(line)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

def main():
    input_file = input("Nhập tên file proxy (.txt): ")
    while not os.path.isfile(input_file):
        print(colored(f"[ERROR] Không tìm thấy file {input_file}.", "red"))
        input_file = input("Nhập lại tên file proxy: ")
    
    try:
        num_threads = int(input("Nhập số lượng thread kiểm tra proxy: "))
        num_rounds = int(input("Nhập số vòng kiểm tra (mỗi vòng xử lý 1 chunk): "))
    except ValueError:
        print(colored("[ERROR] Số thread hoặc số vòng không hợp lệ.", "red"))
        return

    current_round = 1
    # Xử lý file theo từng chunk (mỗi chunk là 10,000 dòng, bạn có thể điều chỉnh chunk_size)
    for chunk in chunked_file_reader(input_file, chunk_size=10000):
        if current_round > num_rounds:
            break
        print(colored(f"Bắt đầu kiểm tra vòng {current_round}", "yellow"))
        perform_check(chunk, num_threads, current_round)
        current_round += 1

if __name__ == "__main__":
    main()