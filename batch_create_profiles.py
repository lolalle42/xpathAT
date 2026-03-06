import subprocess
import hashlib
import time
import os
import shutil

def create_profile(profile_name):
    # Create Firefox profile
    subprocess.run(["C:/Users/admin_8/AppData/Local/Firefox Nightly/firefox.exe", "-CreateProfile", profile_name], check=True)


    # Run generator in desktop-only mode
    subprocess.run(["python", "generate_userjs.py", "--desktop-only"], check=True)

    # Locate Firefox profiles directory
    profiles_dir = os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles")

    # Find the newly created profile folder
    profile_folder = None
    for entry in os.listdir(profiles_dir):
        if profile_name in entry:
            profile_folder = os.path.join(profiles_dir, entry)
            break

    if profile_folder is None:
        raise RuntimeError(f"Profile folder not found for {profile_name}")

    # Move user.js into that folder
    shutil.move("user.js", os.path.join(profile_folder, "user.js"))

    # Log profile name
    with open("created_profiles.txt", "a") as f:
        f.write(profile_name + "\n")

    print(f"Created Firefox profile: {profile_name}")
    print(f"user.js moved to: {profile_folder}")

def main():
    # Ask user for number of profiles
    try:
        count = int(input("How many desktop profiles do you want to create? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(count):
        timestamp = str(time.time()) + str(i)
        profile_hash = hashlib.sha256(timestamp.encode()).hexdigest()[:12]
        profile_name = f"Profile_{profile_hash}"
        create_profile(profile_name)

if __name__ == "__main__":
    main()
