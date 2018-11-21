def main():
    while True:
        try:
            inputFile = input("input file path: ")
            ifhand = open(inputFile)
        except FileNotFoundError:
            print("File not Found.")
            continue
        break

    while True:
        print("Select command:\nGenerator only -> 1\nGenerator-verifier -> 2\nGenerator-Verifier-Alter-Verifier->3\n")
        command = input("Enter Command number:")
        if command == '1':
            print("Generator")
            
        elif command == '2':
            print("Generator-Verifier")
        elif command == '3':
            print("Generator-Varifier-Alter-Verifier")
        else:
            print("Choose a valid command number")
            continue

if __name__ == '__main__':
    main()