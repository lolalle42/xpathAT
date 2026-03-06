import csv
import os

# Path to Firefox profiles directory
profiles_dir = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")

# Path to proxies.csv
csv_file = "proxies.csv"

def update_userjs(profile_name, proxy_host, proxy_port):
    # Find the profile folder
    profile_folder = None
    for entry in os.listdir(profiles_dir):
        if profile_name in entry:
            profile_folder = os.path.join(profiles_dir, entry)
            break

    if profile_folder is None:
        print(f"Profile folder not found for {profile_name}")
        return

    userjs_path = os.path.join(profile_folder, "user.js")

    # Proxy prefs to inject
    proxy_prefs = [
        f'user_pref("network.proxy.type", 1);',
        f'user_pref("network.proxy.http", "{proxy_host}");',
        f'user_pref("network.proxy.http_port", {proxy_port});',
        f'user_pref("network.proxy.ssl", "{proxy_host}");',
        f'user_pref("network.proxy.ssl_port", {proxy_port});',
        f'user_pref("network.proxy.ftp", "{proxy_host}");',
        f'user_pref("network.proxy.ftp_port", {proxy_port});',
        f'user_pref("network.proxy.socks", "{proxy_host}");',
        f'user_pref("network.proxy.socks_port", {proxy_port});',
    ]

    # Append or create user.js
    with open(userjs_path, "a", encoding="utf-8") as f:
        f.write("\n".join(proxy_prefs) + "\n")

    print(f"Updated proxy for {profile_name}: {proxy_host}:{proxy_port}")

def main():
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 3:
                continue
            profile_name, proxy_host, proxy_port = row
            update_userjs(profile_name.strip(), proxy_host.strip(), proxy_port.strip())

if __name__ == "__main__":
    main()
