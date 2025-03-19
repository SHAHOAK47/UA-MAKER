import random
import os
import time
import sys
import webbrowser
import subprocess
import requests
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama for colored output
init(autoreset=True)

# Define color choices globally
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

# Function to get the current date and time
def get_current_date():
    """Return the current date and time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to get public IP
def get_public_ip():
    """Fetch the public IP address of the system."""
    try:
        ip = requests.get("https://api64.ipify.org", timeout=5).text
    except requests.RequestException:
        ip = "Unable to fetch IP"
    return ip

# Function to display the logo with Date and IP
def display_logo():
    """Display the updated FBMF logo along with Date and IP Address."""
    current_date = get_current_date()
    public_ip = get_public_ip()

    logo = f"""{Fore.CYAN}
          e    e           e      888~-_   Y88b    / 
         d8b  d8b         d8b     888   \   Y88b  /  
        d888bdY88b       /Y88b    888    |   Y88b/   
       / Y88Y Y888b     /  Y88b   888    |   /Y88b   
      /   YY   Y888b   /____Y88b  888   /   /  Y88b  
     /          Y888b /      Y88b 888_-~   /    Y88b 🔰XD
{Style.RESET_ALL}
{Fore.YELLOW}📅 Date: {current_date}
🌐 IP Address: {public_ip}{Style.RESET_ALL}
"""
    print(logo)

# Function to generate a random Facebook User-Agent string
def generate_user_agent():
    """Generate a random Facebook User-Agent string."""
    rr = random.randint  # Shortcut for randint
    android_versions = ["7.0", "8.1", "9.0", "10.0", "11.0", "12.0", "13.0", "14.0"]
    mobile_networks = ["Jio 4G", "Airtel", "Vi", "T-Mobile", "AT&T", "Vodafone"]

    # Realme RMX models
    realme_rmx_models = [
        "RMX1945", "RMX1911", "RMX1921", "RMX2020", "RMX2081", "RMX2151", "RMX2170",
        "RMX2193", "RMX3031", "RMX3081", "RMX3363", "RMX3381", "RMX3501"
    ]

    # Oppo CPH models
    oppo_cph_models = [
        "CPH1803", "CPH1853", "CPH1909", "CPH1923", "CPH1933", "CPH1945", "CPH2001",
        "CPH2015", "CPH2069", "CPH2083", "CPH2095", "CPH2127", "CPH2139", "CPH2219"
    ]

    # Samsung Galaxy models
    samsung_models = [
        "SM-A105F", "SM-A205F", "SM-A305F", "SM-A505F", "SM-A705F", "SM-A908B",  # A-series
        "SM-M105F", "SM-M205F", "SM-M305F", "SM-M405F", "SM-M505F", "SM-M705F",  # M-series
        "SM-G960F", "SM-G965F", "SM-G970F", "SM-G973F", "SM-G975F",  # S-series
        "SM-N960F", "SM-N970F", "SM-N975F", "SM-N980F", "SM-N985F"  # Note-series
    ]

    # Infinix models
    infinix_models = [
        "Infinix-X6810", "Infinix-X682B", "Infinix-X688C", "Infinix-X689C", "Infinix-X690B", 
        "Infinix-X693", "Infinix-X695", "Infinix-X697", "Infinix-X6511B", "Infinix-X663", 
        "Infinix-X680", "Infinix-X670", "Infinix-X677", "Infinix-X652", "Infinix-X610"
    ]

    # Vivo models
    vivo_models = [
        "Vivo-Y11", "Vivo-Y12", "Vivo-Y15", "Vivo-Y17", "Vivo-Y20", "Vivo-Y21", "Vivo-Y30",
        "Vivo-Y31", "Vivo-Y33s", "Vivo-Y51", "Vivo-Y53s", "Vivo-Y73", "Vivo-V9", "Vivo-V11",
        "Vivo-V15", "Vivo-V17", "Vivo-V19", "Vivo-V20", "Vivo-V21", "Vivo-V23", "Vivo-X50",
        "Vivo-X60", "Vivo-X70", "Vivo-X80", "Vivo-T1", "Vivo-T2"
    ]

    # Randomly choose between brands
    brand_choice = random.choice(["Realme", "Oppo", "Samsung", "Infinix", "Vivo"])

    if brand_choice == "Realme":
        brand = "Realme"
        device_model = random.choice(realme_rmx_models)
    elif brand_choice == "Oppo":
        brand = "Oppo"
        device_model = random.choice(oppo_cph_models)
    elif brand_choice == "Samsung":
        brand = "Samsung"
        device_model = random.choice(samsung_models)
    elif brand_choice == "Infinix":
        brand = "Infinix"
        device_model = random.choice(infinix_models)
    else:
        brand = "Vivo"
        device_model = random.choice(vivo_models)

    android_version = random.choice(android_versions)
    
    return f"[FBAN/FB4A;FBAV/{rr(250, 300)}.0.0.{rr(10, 60)}.{rr(100, 200)};FBBV/{rr(200000000, 300000000)};" \
           f"FBDM/{{density={random.choice(['2.0', '3.0'])},width={random.choice([720, 1080])},height={random.choice([1412, 1812])}}};" \
           f"FBLC/en_US;FBRV/{rr(100000000, 300000000)};FBCR/{random.choice(mobile_networks)};" \
           f"FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{device_model};FBSV/{android_version};" \
           f"FBOP/1;FBCA/armeabi-v7a:armeabi;]"

# Function to generate and save User-Agent strings
def simulate_user_agent(limit=5, filename="user_agents.txt"):
    """Generate and save a specified number of User-Agent strings."""
    ua_list = {generate_user_agent() for _ in range(limit)}

    with open(filename, "w") as file:
        for ua in ua_list:
            color = random.choice(colors)
            print(color + f"UA GENERATED🔰: {ua}\n" + Style.RESET_ALL)
            file.write(ua + "\n")

    print(Fore.LIGHTGREEN_EX + f"✔ Total UA saved: {len(ua_list)}" + Style.RESET_ALL)

# Function to open contact link
def open_contact():
    """Open the Facebook contact link using xdg-open (Linux) or web browser as fallback."""
    contact_link = "fb://profile/61551778768632"  # Facebook app deep link
    fallback_link = "https://www.facebook.com/profile.php?id=61551778768632"

    print(Fore.YELLOW + "🔗 Opening Facebook Contact Page..." + Style.RESET_ALL)
    time.sleep(1)

    try:
        if sys.platform.startswith("linux"):  # Use xdg-open on Linux
            subprocess.run(["xdg-open", contact_link], check=True)
        else:  # Default to webbrowser for Windows/Mac
            webbrowser.open(contact_link)
    except:
        print(Fore.RED + "⚠ Could not open in the Facebook app. Opening in browser..." + Style.RESET_ALL)
        webbrowser.open(fallback_link)

# Main Menu
def main():
    """Main function for running the script."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for better UI
    display_logo()
    print(Fore.LIGHTYELLOW_EX + "🎉 WELCOME TO UA ZONE! 🔰\n" + Style.RESET_ALL)

    while True:
        print(Fore.CYAN + "📌 1. Generate User Agents")
        print(Fore.GREEN + "📂 2. View Saved User Agents")
        print(Fore.RED + "❌ 3. Exit")
        print(Fore.BLUE + "📞 4. Contact (Facebook Profile)" + Style.RESET_ALL)

        option = input(Fore.LIGHTMAGENTA_EX + "\n🔹 Enter option (1-4): " + Style.RESET_ALL).strip()

        if option == '1':
            try:
                limit = int(input(Fore.LIGHTYELLOW_EX + "⏳ ENTER LIMIT FOR USER AGENTS (e.g., 5): " + Style.RESET_ALL) or 5)
                simulate_user_agent(limit)
            except ValueError:
                print(Fore.RED + "⚠ Invalid input! Please enter a number." + Style.RESET_ALL)

        elif option == '2':
            try:
                with open("user_agents.txt", "r") as file:
                    lines = file.readlines()
                    if not lines:
                        print(Fore.RED + "⚠ No User-Agents found!" + Style.RESET_ALL)
                    else:
                        print(Fore.LIGHTCYAN_EX + "\n📜 SAVED USER AGENTS:\n" + Style.RESET_ALL)
                        for line in lines:
                            color = random.choice(colors)
                            print(color + "📝 " + line.strip() + Style.RESET_ALL)
            except FileNotFoundError:
                print(Fore.RED + "⚠ No User-Agents file found!" + Style.RESET_ALL)

        elif option == '3':
            print(Fore.GREEN + "✅ Goodbye! Exiting..." + Style.RESET_ALL)
            break

        elif option == '4':
            open_contact()

        else:
            print(Fore.RED + "⚠ Invalid choice! Please select a valid option." + Style.RESET_ALL)

# Run the Main Function
if __name__ == '__main__':
    main()