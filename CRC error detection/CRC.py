from generator import generator
from verifier import Verifier
from Alter import Alter
def main():
    while True:
        while True:
            try:
                inputFile = input("input file path: ")
                ifhand = open(inputFile)
            except FileNotFoundError:
                print("File not Found.")
                continue
            break
        message = ifhand.readline()
        genFunc = ifhand.readline()
        ## handling wrong inputs-> eg: extra spaces or \n
        message = message.replace(" ", "")
        message = message.replace("\n", '')
        genFunc = genFunc.replace(" ", "")
        genFunc = genFunc.replace("\n", "")
        print("Commands:\n  Generator only -> 1\n  Generator-verifier -> 2\n  Generator-Verifier-Alter-Verifier->3\n")
        command = input("Enter command number:")
        if command == '1':
            print("Transmitted message: " +generator(message,genFunc))
        elif command == '2':
            transmittedMessage = generator(message,genFunc)
            print("transmitted message: "+transmittedMessage)
            Verifier(transmittedMessage,genFunc)
        elif command == '3':
            transmittedMessage = generator(message, genFunc)
            print("transmitted message: " + transmittedMessage)
            Verifier(transmittedMessage, genFunc)
            bit_position = input("Which bit to alter? ")
            altered_msg = Alter(transmittedMessage,bit_position)
            Verifier(altered_msg,genFunc)
        else:
            print("Choose a valid command number")
            continue
        exit  = input("exit?Y/N\n")
        if exit == 'y' or exit == 'Y':
            break
        else:
            print("__________________________\n\n")
            continue

if __name__ == '__main__':
    main()