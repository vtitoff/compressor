import argparse
from typing import TextIO, Dict, List, Tuple, Union, BinaryIO
import constants
import traceback
import logging

logging.basicConfig(level="DEBUG")
logger = logging.getLogger("compressor")


class Decorator:
    @staticmethod
    def catch_errors(func):
        def _wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                logger.error(traceback.format_exc())

        return _wrapper


class FileHandler:
    def __init__(self):
        pass

    @Decorator.catch_errors
    def get_file(self, path: str) -> bytes:
        with open(file=path, mode="rb", buffering=0) as file:
            return file.read()


class Compressor:
    pass


class Extractor:
    pass


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(constants.FILE_ARGUMENT_NAME, type=str, required=True)
        self.parser.add_argument(
            constants.COMPRESS_RATE_ARGUMENT_NAME,
            type=int,
            default=constants.DEFAULT_COMPRESS_RATE,
        )

    def parse_args(self) -> argparse.Namespace:
        args = self.parser.parse_args()
        return args
