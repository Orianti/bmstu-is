import base64
from des.des import Des


class FileDes(Des):
    def __init__(self):
        super().__init__()

    def encrypt_file(self, filename, key):
        with open(filename, 'rb') as f:
            data = f.read()
        data = base64.b64encode(data).decode('utf-8')
        return self.encrypt(key, data)

    def decrypt_file(self, filename, data, key):
        data = self.decrypt(key, data)
        data = base64.b64decode(data.encode('utf-8'))
        with open(filename, 'wb') as f:
            f.write(data)
