import os
import sys
import winreg

# Define the list of websites you want to block
blocked_websites = [ "www.sarkarinaukari.com","www.myntra.com"]

# Define the IP address to which the websites will be redirected
redirect_ip = "127.0.0.1"

# Define the path to the hosts file
hosts_file_path = r"C:/Windows/System32/drivers/etc/hosts"

def add_website_to_hosts(website):
    try:
        with open(hosts_file_path, "a") as hosts_file:
            hosts_file.write(f"{redirect_ip} {website}\n")
        return True
    except Exception as e:
        print(f"An error occurred while adding {website} to the hosts file:", str(e))
        return False

def block_websites():
    blocked_count = 0
    for website in blocked_websites:
        if add_website_to_hosts(website):
            print(f"{website} blocked successfully.")
            blocked_count += 1

    if blocked_count == 0:
        print("No websites were blocked.")

def unblock_websites():
    try:
        with open(hosts_file_path, "r") as hosts_file:
            lines = hosts_file.readlines()

        with open(hosts_file_path, "w") as hosts_file:
            for line in lines:
                if not any(website in line for website in blocked_websites):
                    hosts_file.write(line)

        print("Websites unblocked successfully.")
    except Exception as e:
        print("An error occurred while unblocking websites:", str(e))

# Main program
while True:
    user_choice = input("Enter 'block' to block websites or 'unblock' to unblock: ").strip().lower()

    if user_choice == "block":
        block_websites()
    elif user_choice == "unblock":
        unblock_websites()
    elif user_choice == "exit":
        break
    else:
        print("Invalid choice. Please enter 'block' or 'unblock' or 'exit' to quit.")

print("Program terminated.")
