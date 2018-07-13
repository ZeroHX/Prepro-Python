"""JOJO"""
def main():
    """main func"""
    word = input().upper()
    wordlist = []
    mudalist = []         #DIO
    oralist = []           #JOJO

    wordlist = word.split(" ")

    for i in range(len(wordlist)):
        if wordlist[i] == "MUDA":
            mudalist.append(wordlist[i])

        elif wordlist[i] == "ORA":
            oralist.append(wordlist[i])

    if len(mudalist) > 0:
        print(" ".join(mudalist))
        print(" ".join(oralist))

    if len(mudalist) > len(oralist):
        print("GOODBYE JOJO!")

    elif len(mudalist) < len(oralist):
        print("Yare Yare Daze")

    elif len(mudalist) == len(oralist) and len(mudalist) != 0:
        print("WR" + ("Y" * len(mudalist)))

    else:
        print("Menacing")

main()
