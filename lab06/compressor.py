from huffman.huffman_decompressor import HuffmanDecompressor
from huffman.huffman_compressor import HuffmanCompressor


if __name__ == '__main__':
    compressor = HuffmanCompressor()
    compressor.compress('tests/file.txt', 'tests/out')

    decompressor = HuffmanDecompressor()
    decompressor.decompress('tests/out', 'tests/res.txt')
