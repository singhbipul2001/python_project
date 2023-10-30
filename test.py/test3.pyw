import os
import ctypes

# Define the list of websites you want to block
blocked_websites = ["flipkart.com", "sarkarinaukari.com"]

# Define the IP address to which the websites will be redirected
redirect_ip = "127.0.0.1"

# Function to block websites
def block_websites():
    try:
        # Open the hosts file in write mode
        with open(r'C:\Windows\System32\drivers\etc\hosts', 'a') as hosts_file:
            for website in blocked_websites:
                # Add an entry to block the website
                hosts_file.write(f"{redirect_ip} {website}\n")

        # Trigger a system refresh to apply changes without restarting the computer
        ctypes.windll.kernel32.SetDllDirectoryW(None)
        ctypes.windll.kernel32.Wow64DisableWow64FsRedirection(ctypes.byref(ctypes.c_void_p()))

        print("Websites blocked successfully.")
    except Exception as e:
        print("An error occurred while blocking websites:", str(e))

if __name__ == "__main__":
    block_websites()
