try:
    import banner
    import time
    import os
    import combinations
    import passwordattack as attackpass
    import brutepin
    import brute
    import about
except ModuleNotFoundError as e:
    print(f"There was an error while importing required libraries\n\n{e}\n\n. To make sure all the required libraries are installed\nrun pip install -r requirements.txt")
try:
    banner.main()
    banner.follow()
    time.sleep(5)
    os.system('clear')
    banner.main()
    print("\n\nWhat would you like to do, sincere and ethical hacker?\nHere are the options you can choose in:\n")
    todo = int(input("""      1. Generate combinations
      2. Attack MD5 and SHA1 encrypted passwords(hashes)
      3. Brute Force PIN codes
      4. Perform a brute force on passwords
      5. Help
      6. About
      7. Exit
                     
        Enter your choice: """)
    )
    match todo:
        case 1:
            combinations.main()
        case 2:
            attackpass.main()
        case 3:
            brutepin.main()
        case 4:
            brute.main()
        case 5:
            help.main()
        case 6:
            about.about()
        case 7:
            banner.main()
            banner.follow()
            print("\n\nThank you for using this tool. I hope you were ethical☺️")
            time.sleep(3)
            os.system('exit')
        case _:
            print("Invalid input, please choose ")
except Exception as e:
    print(f"There was is a run-time error in this file\n\n{e}\n\nPlease fix this error and run the program again")
    input("Press ENTER to continue")