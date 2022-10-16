from utils import FileHandler, Compressor, Extractor, Parser, Decorator, logger

if __name__ == "__main__":
    parser = Parser()
    args = parser.parse_args()
    file_path, compress_rate = args.file, args.cr
    fl = FileHandler()
    file = fl.get_file(file_path)
    print(file)
