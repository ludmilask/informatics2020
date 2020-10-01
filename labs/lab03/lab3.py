from os.path import isdir


def tenet(input_file_path: str, output_file_path: str) -> None:
    if isdir(input_file_path):
        raise ValueError()
    if input_file_path == output_file_path:
        raise ValueError()
    r = open(input_file_path, "r")
    w = open(output_file_path, "w")
    for i in r.readlines():
        w.write((i.replace("\n", ""))[::-1] + "\n")


if __name__ == '__main__':
    tenet("input.txt", "output.txt")