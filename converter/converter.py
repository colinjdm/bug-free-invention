

def main():
    number = input('ppb?')
    length = len(number)
    factor = length - 1
    scientific = (int(number) / (magnitude(length)))

    print(f'{scientific} E {factor}')

    answer = convert(number)

    print(answer)
    


def convert(text):
    converted_number = int(text) * 1000
    return(converted_number)


def magnitude(length):
    return(10 ** (length - 1))


if __name__ == "__main__":
    main()