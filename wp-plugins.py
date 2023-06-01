import requests
import re
import sys

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[96m'
purple = '\033[95m'
reset = '\033[0m'

print """
WordPress Plugin OSINT Tool
""".format(green, green, green, green, red, red, red, reset)

a = 0
total = 0

def main(plugin, kntl):
    result = open(plugin + ".txt", "a")
    global a
    global total
    
    while a < int(kntl):
        a += 1
        print("[+] Scraping Page {}".format(a))
        headers = {"User-agent": "Mozilla 5/0 Linux"}
        
        try:
            text = requests.get("http://pluginu.com/" + plugin + "/" + str(a), headers=headers, timeout=10).text
            lst = re.findall('<p style="margin-bottom: 20px">(.*?)</p></a>', text)
            
            for i in lst:
                total += 1
                print("{}[X] {}----> {}{}".format(green, red, reset, str(i)))
                result.write(i + '\n')
        except Exception as err:
            print("[-] " + str(err))
        
        print("[*] Total Web Scraped: " + str(total))

try:
    plug = raw_input("Enter plugin name: ")
    page = raw_input("Enter page number: ")
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit(0)

main(plug, page)
