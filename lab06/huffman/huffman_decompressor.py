from typing import List, Dict, Any

from huffman.huffman_node import HuffmanNode


class HuffmanDecompressor:
    def __init__(self):
        self.__filename = ''
        self.__file_extension = ''

    def decompress(self, src: str, dst: str) -> None:
        file_bytes = self.__read_file(src)
        decoded_bytes = self.__decode(file_bytes)

        self.__save(dst, decoded_bytes)

    def __decode(self, encoded_bytes: str) -> List[bytes]:
        bits_stream = list(encoded_bytes)
        tree = self.__decode_tree(bits_stream)

        bits_stream = self.__remove_padding(bits_stream)
        reversed_lookup_table = self.__build_reversed_lookup_table(tree)
        byte_key = ''
        output_bytes = []

        for bit in ''.join(bits_stream):
            byte_key += bit
            byte_value = reversed_lookup_table.get(byte_key)

            if byte_value is not None:
                output_bytes.append(byte_value)
                byte_key = ''

        return output_bytes

    def __decode_tree(self, bits_stream: List[bytes]) -> HuffmanNode:
        bit = bits_stream.pop(0)
        if bit == '1':
            byte = ''
            for _ in range(8):
                byte += bits_stream.pop(0)
            return HuffmanNode(int(byte, 2))
        else:
            left = self.__decode_tree(bits_stream)
            right = self.__decode_tree(bits_stream)
            return HuffmanNode(left=left, right=right)

    def __build_reversed_lookup_table(self, huffman_tree: HuffmanNode) -> Dict[str, bytes]:
        lookup_table = {}
        self.__build_reversed_lookup_table_impl(huffman_tree, '', lookup_table)

        if len(lookup_table) == 1:
            key = next(iter(lookup_table))
            lookup_table[key] = '1'

        return {v: k for k, v in lookup_table.items()}

    def __build_reversed_lookup_table_impl(self, node: HuffmanNode, code: str, lookup_table: Dict[Any, str]) -> None:
        if node.is_leaf():
            lookup_table[node.byte] = code
        else:
            self.__build_reversed_lookup_table_impl(node.left, code + '0', lookup_table)
            self.__build_reversed_lookup_table_impl(node.right, code + '1', lookup_table)

    @staticmethod
    def __save(output_file_name: str, output_bytes_num: List[bytes]) -> None:
        output_bytes = ''
        for num in output_bytes_num:
            output_bytes += format(num, '08b')

        data = bytearray()
        for i in range(0, len(output_bytes), 8):
            data.append(int(output_bytes[i:i + 8], 2))

        with open(output_file_name, 'wb') as f:
            f.write(data)

    @staticmethod
    def __remove_padding(bits_stream: list) -> bytes:
        num_of_zeros_bin = bits_stream[:8]
        num_of_zeros_int = int(''.join(num_of_zeros_bin), 2)
        bits_stream = bits_stream[8:]
        bits_stream = bits_stream[num_of_zeros_int:]

        return bits_stream

    @staticmethod
    def __read_file(filename: str) -> str:
        encoded_bytes = ''
        with open(filename, 'rb') as f:
            byte = f.read(1)
            while len(byte) > 0:
                encoded_bytes += f'{bin(ord(byte))[2:]:0>8}'
                byte = f.read(1)

        return encoded_bytes
