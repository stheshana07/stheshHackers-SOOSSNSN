import time, os, banner

def combinations():
    banner.main()
    print("""\n          This will help you generate possible password combinations for a later Brute Force attack
          Here is a key concept of this file
          This is straight forward, you just run the main file and select password generator and provide a charset.
          To avoid overcooking your Operating System, abusing your RAM and burning your CPUs
          the code will sleep for 5seconds after every 2500 combinations generated""")

def brute_force():
    banner.main()
    print("""\n      This will help you Brute Force a password in a login page of any website.
      Here is how it works:
      1. Manually visit the page you want to Brute Force into e.g. https://stheshhackers.com/login.php
      2. Right Click on the page and go to inspect
      3. Locate the page source
      4. Find the form tag
      5. Locate the input with type password and find it's ID, you'll need it
      6. Go back to the form tag and look for actions, you'll need it too
      7. Run the main file and select Brute Force then you will provide what you have(id and action)
      Then BOOM you're good to go!""")

def brute_mobile():
    banner.main()
    print("""      For this attack, you will need a text file with possible PIN codes
      Run the main file and choose Brute Force PIN codes and follow the prompts""")

def hashes():
    banner.main()
    print("""\n      This code also requires a text file containing all possible passwords, and the hash itself.
      This code will try the passwords against the hash until it finds the correct decrypted password
      Run the main file and select Attack MD5 and SHA1 encrypted passwords(hashes)""")

def main():
    try:
        banner.main()
        help = int(input("""      Enter a tool you need help with
        1. Combinations Generator
        2. Website Login Brute Force
        3. Mobile Phone Brute Force
        4. MD5 and SHA1 hash decryptor
        5. Exit
                        
        Your choice: """))
        match help:
            case 1:
                combinations()
            case 2:
                brute_force()
            case 3:
                brute_mobile()
            case 4:
                hashes()
            case 5:
                print("Thank you for visiting")
                time.sleep(3)
                os.system('exit')
    except Exception as e:
        print(f"There was a runtime error in this file. please fix this error and run again\nERROR: {e}")
        os.system('exit')
if __name__ == "__main__":
    main()