import argparse
import constants


class FileHandler:
    def __init__(self):
        pass

    def get_file(self, path):
        pass


class Compressor:
    pass


class Extractor:
    pass


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--file", type=str, required=True)
        self.parser.add_argument(
            "--cr", type=int, default=constants.DEFAULT_COMPRESS_RATE
        )

    def parse_args(self) -> argparse.Namespace:
        args = self.parser.parse_args()
        return args
