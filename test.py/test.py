import os

def block_website(website):
  """Blocks a website by adding it to the hosts file.

  Args:
    website: The website to block.
  """

  with open("C:/Windows/System32/drivers/etc/hosts", "r+") as f:
    hosts = f.readlines()
    if website not in hosts:
      hosts.append("127.0.0.1 {}\n".format(website))
      f.seek(0)
      f.writelines(hosts)
      f.truncate()

# Example usage:

block_website("www.myntra.com")