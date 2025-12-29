import banner
import time
import os
import colorama
import random
import itertools
def generate(charset, length, wordlist, work_dir):
    banner.main()
    print(colorama.Fore.YELLOW + "This code will generate combinations based on the charset provided")
    time.sleep(1.5)
    wordlist = f'{work_dir}/wordlists/{wordlist}'
    for i in range(random.randint(0, 3)):
        print("Initiating attack")
        time.sleep(0.5)
        os.system('clear')
        banner.main()
        print("Initiating attack.")
        time.sleep(0.5)
        os.system('clear')
        banner.main()
        print("Initiating attack..")
        time.sleep(0.5)
        os.system('clear')
        banner.main()
        print("Initiating attack...")
        time.sleep(0.5)
        os.system('clear')
        banner.main()
    print("Code Injected Successfully")
    time.sleep(2)
    os.system('clear')
    banner.main()
    overcook = 0
    start_time = time.time()
    with open(f"{wordlist}") as file:
        start = time.time()
        for alpha in itertools.product(charset, repeat=length):
            os.system(f'echo "{"".join(alpha)}" >> {wordlist}')
            print("".join(alpha))
            os.system('clear')
            overcook += 1
            if overcook%2500 == 0:
                print("Avoiding overcook. The code will sleep for 5 seconds")
                for i in range(5, 0, -1):
                    print(f"Resumming in {i}seconds")
                    time.sleep(1)
                    os.system('clear')
    print(f"Combinations generated: {overcook}\nTime taken: {(time.time()-start):.2f}s\nAverage speed: {(overcook)/(time.time()-start)} combinations per second")
