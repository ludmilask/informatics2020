from os.path import isdir


def tenet(input_file_path: str, output_file_path: str) -> None:
    if isdir(input_file_path):
        raise ValueError(f"Expect file as input, but got directory: \"{input_file_path}\"!")
    if input_file_path == output_file_path:
        raise ValueError(f"input and output files are the same")
    file_for_reading = open(input_file_path, "r")
    file_for_writing = open(output_file_path, "w")
    for row in file_for_reading.readlines():
        file_for_writing.write((row.replace("\n", ""))[::-1] + "\n")
    file_for_reading.close()
    file_for_writing.close()


if __name__ == '__main__':
    tenet("input.txt", "output.txt")
