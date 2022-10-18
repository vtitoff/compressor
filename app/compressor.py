import abc
from typing import TextIO, Dict, List, Tuple, Union, BinaryIO
import logging
from utils import Decorator

logger = logging.getLogger("compressor")


class Compressor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def compress(self, file: bytes) -> bytes:
        pass


class RLECompressor(Compressor):
    def compress(self, file: bytes) -> bytes:
        compress_file = b""
        num = str(1).encode("utf-8")
        byte = "ssssss".encode("utf-8")
        compress_file += num
        compress_file += byte
        logger.debug(compress_file)

    def alghoritm(self, data):
        s = "AAAABBBCCDDEFFXXXXXXXX"
        temp = s[0]
        count = 1
        answer = []
        for i in range(1, len(s)):
            if s[i] == temp:
                count += 1
            else:
                if count > 1:
                    answer.append(f"{count}{temp}")
                    temp = s[i]
                    count = 1
                else:
                    answer.append(temp)
                    temp = s[i]
                    count = 1
        if count > 1:
            answer.append(f"{count}{temp}")
            temp = s[i]
            count = 1
        else:
            answer.append(temp)
            temp = s[i]
            count = 1
        print("".join(answer))


class CompressController:
    def __init__(self, compressor: Compressor):
        self.compressor = compressor

    def choice_compressor(self, compressor: Compressor) -> None:
        pass

    def compress(self, file: bytes) -> bytes:
        self.compressor.compress(file)
