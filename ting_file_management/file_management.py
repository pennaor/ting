import sys


def txt_importer(path_file: str):
    name_ext = path_file.split(".")
    if len(name_ext) != 2 or name_ext[1] != "txt":
        return print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file) as file:
            content = file.read()
        return content.split("\n")
    except (FileNotFoundError):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
