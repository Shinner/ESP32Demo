# main.py
def main():
    with open('led.py', 'r') as f:
        exec(f.read())


if __name__ == '__main__':
    main()
