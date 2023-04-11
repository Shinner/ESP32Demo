# main.py
def main():
    with open('common/mqtt.py', 'r') as f:
        exec(f.read())


if __name__ == '__main__':
    main()
