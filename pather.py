import argparse
import pathlib

def get_absolute_path(argument: str) -> pathlib.Path:
    return pathlib.Path(argument).absolute()

def get_parser() -> argparse.ArgumentParser:
    _parser = argparse.ArgumentParser()
    _parser.add_argument(
        "document_path",
        type=get_absolute_path
    )
    return _parser

def process_document(document_path: pathlib.Path) -> None:
    print(document_path)

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    process_document(args.document_path)