import banner
import time
import os
import subprocess
from generate import generate

def main():
    banner.main()
    work_dir = subprocess.run('pwd', shell=True, text=True, capture_output=True, check=True).stdout.strip()
    th = int(input("Enter the number of current existing wordlists(0~inf): ")) + 1
    wordlist = input("Enter filename where generated passwords will be saved(do not include .txt file): ").strip() + str(th) + ".txt"
    if not(os.path.exists(f'{work_dir}/wordlists')):
        os.system(f'mkdir {work_dir}/wordlists && cd wordlists && touch {wordlist}')
    else:
        os.system(f'cd wordlists && touch {wordlist}')
    size = int(input("Enter the highest(or the exact) possible length for the password you are attacking: "))
    lowercases = 'abcdefghijklmnopqrstuvwxyz'
    upper_cases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = "0123456789"
    special = '!@#$%&*_-?.'
    banner.main()
    print("""
1. lowercase characters only
2. Uppercase characters only
3. digits only
4. special characters only
5. lowercases and upper cases
6. lowercases and digits
7. lowercases and special characters
8. Upper cases and digits
9. Upper cases and special cases
10. digits and special characters
11. lowercases, upper cases and digits
12. lowercases, upper cases and special characters
13. upper cases, digits and special characters
14. All
15. Custom charset
""")
    charset_choice = int(input("Enter an integer corresponding to the charset of your choice: "))
    match(charset_choice):
        case 1:
            charset = lowercases
            generate(charset, size, wordlist, work_dir)
        case 2:
            charset = upper_cases
            generate(charset, size, wordlist, work_dir)
        case 3:
            charset = digits
            generate(charset, size, wordlist, work_dir)
        case 4:
            charset = special
            generate(charset, size, wordlist, work_dir)
        case 5:
            charset = lowercases + upper_cases
            generate(charset, size, wordlist, work_dir)
        case 6:
            charset = lowercases + digits
            generate(charset, size, wordlist, work_dir)
        case 7:
            charset = lowercases + special
            generate(charset, size, wordlist, work_dir)
        case 8:
            charset = upper_cases + digits
            generate(charset, size, wordlist, work_dir)
        case 9:
            charset = upper_cases + special
            generate(charset, size, wordlist, work_dir)
        case 10:
            charset = digits + special
            generate(charset, size, wordlist, work_dir)
        case 11:
            charset = lowercases + upper_cases + digits
            generate(charset, size, wordlist, work_dir)
        case 12:
            charset = lowercases + upper_cases + special
            generate(charset, size, wordlist, work_dir)
        case 13:
            charset = upper_cases + special + digits
            generate(charset, size, wordlist, work_dir)
        case 14:
            charset = lowercases + upper_cases + digits + special
            generate(charset, size, wordlist, work_dir)
        case 15:
            charset = input("Enter your custom charset: ")
            generate(charset, size, wordlist, work_dir)
        case _:
            print("Please enter a valid choice, sincere hacker...")
            time.sleep(2)
            os.system('clear && exit')
if __name__ == "__main__":
    main()
