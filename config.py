def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError  as err:
        print(f"Couldn't find the config.txt file! {err}")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except Exception:
        print("No puedo encontrar  config.txt")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno ==2:
            print(f"Couldn't find the config.txt file! {err}")
        elif err.errno == 13:
            print(f"Found config.txt but couldn't read it: {err}")


if __name__ == '__main__':
    main()
