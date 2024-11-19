import zipfile
import pathlib

def make_archive(filepaths, dest_dir, zip_name):
    dest_path = pathlib.Path(dest_dir, zip_name)
    with zipfile.ZipFile(dest_path, 'w') as archive: 
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname = filepath.name)


if __name__ == "__main__":
    print("Hello")