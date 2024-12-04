import os
import time
def main():

    print(os.system("ls -l"))
    time.sleep(2)
    print(os.system('pwd'))



if __name__ == '__main__':
    main()
