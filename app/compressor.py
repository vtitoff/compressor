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
        # compress_file = b""
        # num = str(1).encode("utf-8")
        # byte = file.encode("utf-8")
        # compress_file += num
        # compress_file += byte
        compress_file = self.alghoritm(file)
        logger.debug(type(compress_file))
        return compress_file

    def alghoritm(self, data):
        temp = data[0]
        count = 1
        answer = []
        for i in range(1, len(data)):
            if data[i] == temp:
                count += 1
            else:
                if count > 1:
                    answer.append(f"{count}{temp}")
                    temp = data[i]
                    count = 1
                else:
                    answer.append(f"{count}{temp}")
                    temp = data[i]
                    count = 1
        if count > 1:
            answer.append(f"{count}{temp}")
            temp = data[i]
            count = 1
        else:
            answer.append(f"{count}{temp}")
            temp = data[i]
            count = 1
        compress_file = "".join(answer)
        return compress_file.encode('utf-8')


class CompressController:
    def __init__(self, compressor: Compressor):
        self.compressor = compressor

    def choice_compressor(self, compressor: Compressor) -> None:
        pass

    def compress(self, file: bytes) -> bytes:
        return self.compressor.compress(file)
