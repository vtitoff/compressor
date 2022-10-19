from utils import FileHandler, Extractor, Parser, Decorator, logger
from compressor import CompressController, ZipCompressor

if __name__ == "__main__":
    parser = Parser()
    args = parser.parse_args()
    file_path, compress_rate = args.file, args.cr
    compress_controller = CompressController(ZipCompressor())
    compress_controller.compress(file_path, 'test')
