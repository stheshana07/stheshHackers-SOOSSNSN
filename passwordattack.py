import hashlib
import sys
import banner
import time
import colorama

def crack_md5(target_hash, wordlist_path):
    print(f"\n[+] Algorithm: MD5")
    print(f"[+] Target Hash: {target_hash}")
    print(f"[+] Using Wordlist: {wordlist_path}\n")

    try:
        with open(wordlist_path, 'r', encoding='latin-1') as wordlist_file:
            for line in wordlist_file:
                password = line.strip()
                encoded_password = password.encode('utf-8')
                
                hash_object = hashlib.md5(encoded_password)
                generated_hash = hash_object.hexdigest()
                
                sys.stdout.write(f"\r[-] Testing: {password:<25}") 
                sys.stdout.flush()

                if generated_hash == target_hash:
                    print(f"\n\n[!!!] **PASSWORD FOUND (MD5):** {password}")
                    return True

        print("\n\n[x] Wordlist exhausted. Password not found.")
        return False

    except FileNotFoundError:
        print(f"\n[ERROR] Wordlist file not found: {wordlist_path}")
        return False
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")
        return False

def crack_sha1(target_hash, wordlist_path):
    print(f"\n[+] Algorithm: SHA1")
    print(f"[+] Target Hash: {target_hash}")
    print(f"[+] Using Wordlist: {wordlist_path}\n")
    time.sleep(1.5)

    try:
        with open(wordlist_path, 'r', encoding='latin-1') as wordlist_file:
            for line in wordlist_file:
                time.sleep(0.05)
                password = line.strip()
                encoded_password = password.encode('utf-8')
                
                hash_object = hashlib.sha1(encoded_password)
                generated_hash = hash_object.hexdigest()
                
                sys.stdout.write(colorama.Fore.YELLOW + f"\r[-] Testing: {password:<25}") 
                sys.stdout.flush()

                if generated_hash == target_hash:
                    print(colorama.Fore.GREEN + f"\n\n[!!!] PASSWORD FOUND (SHA1): {password}")
                    return True
                else:
                    print(colorama.Fore.RED + "Not correct!")

        print(colorama.Fore.RED + "\n\n[x] Wordlist exhausted. Password not found.")
        return False

    except FileNotFoundError:
        print(colorama.Fore.RED + f"\n[ERROR] Wordlist file not found: {wordlist_path}")
        return False
    except Exception as e:
        print(colorama.Fore.RED + f"\n[ERROR] An unexpected error occurred: {e}")
        return False


def main():
    banner.main()
    
    print("\n--- Password Cracking Module ---")
    
    print("\n[?] Select Hash Type:")
    print("    1) MD5")
    print("    2) SHA1")
    
    while True:
        choice = input("    Enter choice (1 or 2): ").strip()
        if choice == '1':
            algorithm = 'MD5'
            break
        elif choice == '2':
            algorithm = 'SHA1'
            break
        else:
            print("[!] Invalid choice. Please enter 1 or 2.")

    target_hash = input(f"[?] Enter Target {algorithm} Hash: ").strip()
    wordlist_path = input("[?] Enter Wordlist Path(eg /path/to/wordlist.txt): ").strip()

    if target_hash and wordlist_path:
        if algorithm == 'MD5':
            crack_md5(target_hash, wordlist_path)
        elif algorithm == 'SHA1':
            crack_sha1(target_hash, wordlist_path)
    else:
        print("\n[ERROR] Hash or wordlist path cannot be empty. Exiting.")
        time.sleep(1.5)

if __name__ == "__main__":
    main()