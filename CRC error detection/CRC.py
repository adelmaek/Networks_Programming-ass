from generator import generator
from verifier import Verifier
from Alter import Alter
def main():
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
    print("message: "+ message)
    print("genFunc: "+genFunc)
    while True:
        print("Select command:\nGenerator only -> 1\nGenerator-verifier -> 2\nGenerator-Verifier-Alter-Verifier->3\n")
        command = input("Enter Command number:")
        if command == '1':
            #print("Generator")
            print("Transmitted message: " +generator(message,genFunc))
        elif command == '2':
            #print("Generator-Verifier")
            transmittedMessage = generator(message,genFunc)
            print("transmitted message: "+transmittedMessage)
            Verifier(transmittedMessage,genFunc)
        elif command == '3':
            #print("Generator-Varifier-Alter-Verifier")
            transmittedMessage = generator(message, genFunc)
            print("transmitted message: " + transmittedMessage)
            Verifier(transmittedMessage, genFunc)
            bit_position = input("Which bit to alter? ")
            altered_msg = Alter(transmittedMessage,bit_position)
            Verifier(altered_msg,genFunc)
        else:
            print("Choose a valid command number")
            continue
        exit  = input("exit?Y/N")
        if exit == 'y' or exit == 'Y':
            break
        else:
            continue

if __name__ == '__main__':
    main()