from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


def sign(filename: str, pub_key_filename: str = 'id_rsa.pub', sign_filename: str = None) -> None:
    data = open(filename, 'rb').read()
    hash = SHA256.new(data)

    keys = RSA.generate(1024)
    pub_key = keys.publickey()
    open(pub_key_filename, 'wb').write(pub_key.exportKey())

    sign = pkcs1_15.new(keys).sign(hash)
    if sign_filename is None:
        sign_filename = filename + '.sig'
    open(sign_filename, 'wb').write(sign)


def check_sign(filename: str, pub_key_filename: str = 'id_rsa.pub', sign_filename: str = None) -> None:
    data = open(filename, 'rb').read()
    hash = SHA256.new(data)

    pub_key = RSA.import_key(open(pub_key_filename, 'rb').read())

    if sign_filename is None:
        sign_filename = filename + '.sig'
    signature = open(sign_filename, 'rb').read()

    try:
        pkcs1_15.new(pub_key).verify(hash, signature)
    except ValueError or TypeError:
        print('Attention! Signature is not confirmed.')
        exit(1)

    print('Signature confirmed.')


def main() -> None:
    sign('file.png')
    check_sign('file.png')


if __name__ == '__main__':
    main()
