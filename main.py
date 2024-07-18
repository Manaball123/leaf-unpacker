import lac
import os
import shutil

def mkdir_if_not_exist(dir : str):
    if not os.path.isdir(dir):
        os.makedirs(dir)


dst_root = "WHITE_ALBUM2"
def main():
    packed_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".LAC"):
                packed_files.append(file)
    for file in packed_files:
        arcview = lac.ArcView(file)
        opener = lac.LacOpener(arcview)
        opener.TryOpen()
        
        for e in opener.directory:
            dst_path = f"{dst_root}/{e.name}"
            mkdir_if_not_exist(dst_path.rsplit("/", 1)[0])
            print(f"extracting {e.name} 2 {dst_path}")
            data = opener.ExtractFile(e)
            
            with open(dst_path, "wb+") as f:
                f.write(data)


main()