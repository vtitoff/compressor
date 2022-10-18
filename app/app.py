from utils import FileHandler, Extractor, Parser, Decorator, logger
from compressor import CompressController, RLECompressor

if __name__ == "__main__":
    parser = Parser()
    args = parser.parse_args()
    file_path, compress_rate = args.file, args.cr
    fl = FileHandler()
    file = fl.get_file(file_path)
    compress_controller = CompressController(RLECompressor())
    compress_file = compress_controller.compress(file)
    print(compress_file)
