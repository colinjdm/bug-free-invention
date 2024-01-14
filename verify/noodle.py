import sys

def main():
    names = set()
    try:
        while True:
            name = input("Name: ")
            names.add(name)
            print(sorted(names))
    except KeyboardInterrupt:
        sys.exit("\n")

if __name__ == "__main__":
    main()