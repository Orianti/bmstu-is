from enigma.enigma import Enigma


def main():
    enigma = Enigma()

    print('Do you want to generate Enigma config file [Y/n]?', end=' ')
    if str(input()) in ['Y', 'y']:
        enigma.generate_config()
        config = str(input('New config file name: '))
        enigma.save_config(config)
        print('Config file was saved successfully.')
    else:
        config = str(input('Config file name: '))
        try:
            enigma.set_config(config)
        except FileNotFoundError:
            print(f'Error! No such file: \'%s\'' % config)
            exit(1)
    print('Enigma was configured successfully.', end='\n\n')

    src = str(input('Source file name: '))
    dst = str(input('Destination file name: '))
    if src == dst:
        print('Error! Source and destination file must be different.')
        exit(1)
    try:
        enigma.encrypt_file(src, dst)
    except FileNotFoundError:
        print(f'Error! No such file: \'%s\'' % src)
        exit(1)
    print('File was encrypted successfully.')


if __name__ == '__main__':
    main()
