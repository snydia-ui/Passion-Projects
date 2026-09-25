
import re
RED = "\033[31m"
RESET = "\033[0m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_BLUE = "\033[94m"
MAGENTA = "\033[95m"
BRIGHT_YELLOW = "\033[93m"
one = ["RAFLY","JABEZ","RHUZZ","RUSSE","ZOFIA","LICEA"]
two = ["SEBAS","CATAL","KALEL", "FORRE","TEN-E","JIANA"]
three = ["YDRAE","JAZZZ","ZIVAA","JAELE","JEDAI","TRAMS"]
four = ["CHLOS","CHLOF","ALEXI","ROYJS","JADEN","IBANQ"]
five = ["POLLX","MIHRR","ISAIH","KYZEN","KETUR","NATEE"]

print(f'''
{MAGENTA}CAMIANS       - input = 1A,  B    2,3e, a4, f4, 1 b etc...{RESET}
---I--{BRIGHT_GREEN}A{RESET}--I-I--{BRIGHT_GREEN}B{RESET}--I-I--{BRIGHT_GREEN}C{RESET}--I--I--I--{BRIGHT_GREEN}D{RESET}--I-I--{BRIGHT_GREEN}E{RESET}--I-I--{BRIGHT_GREEN}F{RESET}--I---I
{BRIGHT_GREEN}1{RESET}---{one[0]}---{one[1]}---{one[2]}---I---{one[3]}---{one[4]}---{one[5]}---I
{BRIGHT_GREEN}2{RESET}---{two[0]}---{two[1]}---{two[2]}---I---{two[3]}---{two[4]}---{two[5]}---I
{BRIGHT_GREEN}3{RESET}---{three[0]}---{three[1]}---{three[2]}---I---{three[3]}---{three[4]}---{three[5]}---I
{BRIGHT_GREEN}4{RESET}---{four[0]}---{four[1]}---{four[2]}---I---{four[3]}---{four[4]}---{four[5]}---I
{BRIGHT_GREEN}5{RESET}---{five[0]}---{five[1]}---{five[2]}---I---{five[3]}---{five[4]}---{five[5]}---I
''')

while True:
    yes = input(f"{BRIGHT_BLUE}Who Do You Cross Out?:{RESET}")
    yes = yes.upper()
    yes = yes.replace(" ","")
    yes = re.sub(r"[^a-zA-Z0-9]", "", yes)
    if len(yes) == 2 and yes[0].isalpha() and yes[1].isdigit():
        lettah, digit = yes
        yes = f"{digit}{lettah}"




    if yes == "1A":
        one[0] = f"{RED}XXXXX{RESET}"
    elif yes == "1B":
        one[1] = f"{RED}XXXXX{RESET}"
    elif yes == "1C":
        one[2] = f"{RED}XXXXX{RESET}"
    elif yes == "1D":
        one[3] = f"{RED}XXXXX{RESET}"
    elif yes == "1E":
        one[4] = f"{RED}XXXXX{RESET}"
    elif yes == "1F":
        one[5] = f"{RED}XXXXX{RESET}"
    elif yes == "2A":
        two[0] = f"{RED}XXXXX{RESET}"
    elif yes == "2B":
        two[1] = f"{RED}XXXXX{RESET}"
    elif yes == "2C":
        two[2] = f"{RED}XXXXX{RESET}"
    elif yes == "2D":
        two[3] = f"{RED}XXXXX{RESET}"
    elif yes == "2E":
        two[4] = f"{RED}XXXXX{RESET}"
    elif yes == "2F":
        two[5] = f"{RED}XXXXX{RESET}"
    elif yes == "3A":
        three[0] = f"{RED}XXXXX{RESET}"
    elif yes == "3B":
        three[1] = f"{RED}XXXXX{RESET}"
    elif yes == "3C":
        three[2] = f"{RED}XXXXX{RESET}"
    elif yes == "3D":
        three[3] = f"{RED}XXXXX{RESET}"
    elif yes == "3E":
        three[4] = f"{RED}XXXXX{RESET}"
    elif yes == "3F":
        three[5] = f"{RED}XXXXX{RESET}"
    elif yes == "4A":
        four[0] = f"{RED}XXXXX{RESET}"
    elif yes == "4B":
        four[1] = f"{RED}XXXXX{RESET}"
    elif yes == "4C":
        four[2] = f"{RED}XXXXX{RESET}"
    elif yes == "4D":
        four[3] = f"{RED}XXXXX{RESET}"
    elif yes == "4E":
        four[4] = f"{RED}XXXXX{RESET}"
    elif yes == "4F":
        four[5] = f"{RED}XXXXX{RESET}"
    elif yes == "5A":
        five[0] = f"{RED}XXXXX{RESET}"
    elif yes == "5B":
        five[1] = f"{RED}XXXXX{RESET}"
    elif yes == "5C":
        five[2] = f"{RED}XXXXX{RESET}"
    elif yes == "5D":
        five[3] = f"{RED}XXXXX{RESET}"
    elif yes == "5E":
        five[4] = f"{RED}XXXXX{RESET}"
    elif yes == "5F":
        five[5] = f"{RED}XXXXX{RESET}"
    else:
        print(f"{BRIGHT_YELLOW}!!!!huhhhhh wrong format!!!!{RESET}")


    print(f'''
    {MAGENTA}CAMIANS       - input = 1A,1B,3e, 4a, 5f, 1b etc...{RESET}
    ---I--{BRIGHT_GREEN}A{RESET}--I-I--{BRIGHT_GREEN}B{RESET}--I-I--{BRIGHT_GREEN}C{RESET}--I--I--I--{BRIGHT_GREEN}D{RESET}--I-I--{BRIGHT_GREEN}E{RESET}--I-I--{BRIGHT_GREEN}F{RESET}--I---I
    {BRIGHT_GREEN}1{RESET}---{one[0]}---{one[1]}---{one[2]}---I---{one[3]}---{one[4]}---{one[5]}---I
    {BRIGHT_GREEN}2{RESET}---{two[0]}---{two[1]}---{two[2]}---I---{two[3]}---{two[4]}---{two[5]}---I
    {BRIGHT_GREEN}3{RESET}---{three[0]}---{three[1]}---{three[2]}---I---{three[3]}---{three[4]}---{three[5]}---I
    {BRIGHT_GREEN}4{RESET}---{four[0]}---{four[1]}---{four[2]}---I---{four[3]}---{four[4]}---{four[5]}---I
    {BRIGHT_GREEN}5{RESET}---{five[0]}---{five[1]}---{five[2]}---I---{five[3]}---{five[4]}---{five[5]}---I
    ''')