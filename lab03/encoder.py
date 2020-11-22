from des.file_des import FileDes

if __name__ == '__main__':
    key = 'qwertyui'
    crypto = FileDes()
    data = crypto.encrypt_file('file.txt', key)
    crypto.decrypt_file('result.txt', data, key)
