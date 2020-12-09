from queue import PriorityQueue
from typing import Dict, Any

from huffman.huffman_node import HuffmanNode


class HuffmanCompressor:
    def __init__(self):
        self.__filename = None
        self.__queue = PriorityQueue()

    def compress(self, src: str, dst: str) -> None:
        self.__filename = src

        with open(src, 'rb') as f:
            data = f.read()

        frequency_table = self.__build_frequency_table(data)
        huffman_tree = self.__build_tree(frequency_table)
        lookup_table = self.__build_lookup_table(huffman_tree)
        encoded_bytes = self.__build_encoded_bytes(data, lookup_table)

        self.__save(dst, huffman_tree, encoded_bytes)

    def __build_tree(self, frequency_table: Dict[str, int]) -> HuffmanNode:
        for byte, frequency in frequency_table.items():
            self.__queue.put(HuffmanNode(byte, frequency))

        while self.__queue.qsize() > 1:
            left, right = self.__queue.get(), self.__queue.get()
            parent = HuffmanNode(None, left.freq + right.freq, left, right)
            self.__queue.put(parent)

        return self.__queue.get()

    def __build_lookup_table(self, huffman_tree: HuffmanNode) -> Dict[Any, str]:
        lookup_table = {}
        self.__build_lookup_table_impl(huffman_tree, '', lookup_table)

        if len(lookup_table) == 1:
            key = next(iter(lookup_table))
            lookup_table[key] = '1'

        return lookup_table

    def __build_lookup_table_impl(self, node: HuffmanNode, code: str, lookup_table: Dict[Any, str]) -> None:
        if node.is_leaf():
            lookup_table[node.byte] = code
        else:
            self.__build_lookup_table_impl(node.left, code + '0', lookup_table)
            self.__build_lookup_table_impl(node.right, code + '1', lookup_table)

    def __encode_tree(self, node: HuffmanNode, string: str) -> str:
        if node.is_leaf():
            string += '1'
            string += f'{node.byte:08b}'
        else:
            string += '0'
            string = self.__encode_tree(node.left, string)
            string = self.__encode_tree(node.right, string)

        return string

    def __save(self, filename: str, tree: HuffmanNode, encoded_bytes: str) -> None:
        encoded_tree = self.__encode_tree(tree, '')
        output_bytes = self.__add_padding(encoded_tree, encoded_bytes)

        data = bytearray()
        for i in range(0, len(output_bytes), 8):
            data.append(int(output_bytes[i:i + 8], 2))

        with open(filename, 'wb') as f:
            f.write(data)

    @staticmethod
    def __build_frequency_table(data: bytes) -> Dict[str, int]:
        frequency_table = {byte: 0 for byte in set(data)}
        for byte in data:
            frequency_table[byte] += 1

        return frequency_table

    @staticmethod
    def __build_encoded_bytes(data: bytes, lookup_table: Dict[Any, str]) -> str:
        encoded_bytes = ''
        for byte in data:
            encoded_bytes += lookup_table[byte]

        return encoded_bytes

    @staticmethod
    def __add_padding(encoded_tree: str, encoded_bytes: str) -> str:
        padding = 8 - (len(encoded_bytes) + len(encoded_tree)) % 8
        if padding != 0:
            encoded_bytes = padding * '0' + encoded_bytes

        return f'{encoded_tree}{padding:08b}{encoded_bytes}'
