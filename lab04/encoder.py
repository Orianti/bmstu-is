from rsa import Rsa


def main():
    crypto = Rsa()

    print(f'Public key:  {crypto.get_public_key()}')
    print(f'Private key: {crypto.get_private_key()}')

    crypto.encrypt_file('file.png', 'out')
    crypto.decrypt_file('out', 'res.png')


if __name__ == '__main__':
    main()
