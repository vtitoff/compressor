import abc
from typing import TextIO, Dict, List, Tuple, Union, BinaryIO
import logging
from utils import Decorator
import zipfile

logger = logging.getLogger("compressor")


class Compressor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def compress(self, file: str, archive_name: str) -> None:
        pass


class ZipCompressor(Compressor):
    def compress(self, file: str, archive_name: str) -> None:
        zip = zipfile.ZipFile(f'{archive_name}.zip', 'w')
        zip.write(file, compress_type=zipfile.ZIP_DEFLATED, compresslevel=5)
        zip.close()


class CompressController:
    def __init__(self, compressor: Compressor):
        self.compressor = compressor

    def choice_compressor(self, compressor: Compressor) -> None:
        pass

    def compress(self, path: str, archive_name: str) -> None:
        self.compressor.compress(path, archive_name)
