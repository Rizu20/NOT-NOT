import sys
from msvcrt import kbhit,getch
from time import time,sleep
from random import choice


def intro_msg():
    sys.stdout.write("\n\tGame starting ")
    sys.stdout.flush()
    for i in range(3):
        sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    sleep(1)
    print("\n\n")
    print("\tKEY \t\t\t\t\tScore")
    print("\t--- \t\t\t\t\t-----")

def bye_msg(score):
    print("\n\n\tGame_finished.")
    print("\tYour Score : {}".format(score))
    print("\tThanks for playing.")
    r=input()
    
    


def main():
    input_dict={"UP       ":72,
                "LEFT     ":75,
                "DOWN     ":80,
                "RIGHT    ":77,
                "NOT UP   ":80,
                "NOT DOWN ":72,
                "NOT LEFT ":77,
                "NOT RIGHT":75}
    global score
    score=0
    timeout=3
    
    while True:
        key_shown=choice(list(input_dict.keys()))
        sys.stdout.write("\t%s \t\t\t\t%s" %(key_shown,score))
        sys.stdout.flush()
        key_in_ascii= ''
        start_time = time()
        while True:
            if kbhit():
                getch()
                key_in_ascii=ord(getch().decode('utf-8'))
                print()
                #print(key_in_ascii)
                if key_in_ascii == input_dict[key_shown]:
                    score += 1
                    break
                else:
                    print('\n\n\t\tWrong input. Sorry.')
                    return 0

            if key_in_ascii=='' and (time() - start_time) > timeout:
                print("\n\n\t\tTime out. You have to be faster.")
                return 0
            


intro_msg()
main()
bye_msg(score)

        
        
                
                
            
