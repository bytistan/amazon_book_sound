from bs4 import BeautifulSoup
import parse 
from settings import *
from helper import append_to_json_file,read_file
import time

if __name__ == "__main__":
    for link in read_file("resources/links.txt"): 
        while True:
            try:
                response = parse.send_request(link,"resources/user_agent.txt")
                if response.status_code == 200:
                    print(f"[+] Status code :{response.status_code}")
                    soup = BeautifulSoup(response.text, "html.parser")
                    data = parse.scrapper(soup,scrapper_info)
                    append_to_json_file(data,"data.json")
                    break
                else:
                    print(f"[-] Status code : {response.status_code}")
            except Exception as e:
                print(f"[-] Site content could not be reached trial {c}.")
            finally:
                c += 1
                time.sleep(2)
