import argparse

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Advent of code 2024!'
    )

def handle_args(args: argparse.Namespace):
    pass

def main():
    parser = get_parser()
    args = parser.parse_args()
    handle_args(args)

if __name__ == '__main__':
    main()
