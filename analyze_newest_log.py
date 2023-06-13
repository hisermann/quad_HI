import os
from os.path import dirname, basename, splitext
import glob


if __name__ == "__main__":
    base = dirname(__file__)
    os.chdir(base)
    try:
        logname = os.path.abspath(sorted(glob.glob("mjbots-quada1*.log"),reverse=True)[0])
    except IndexError:
        print("no file found")
        exit()
    name = splitext(basename(logname))[0]
    rename = input("New name for data: ")
    if not rename:
        rename = name
    new_path = os.path.join(base,"analysis",rename,"")
    try:
        os.makedirs(new_path,exist_ok=False)
    except FileExistsError:
        if input(f"File {new_path} already exists. Overwrite? Y/n\n") not in {"","Y","y","J","j"}:
            exit()
    newlogname = os.path.join(new_path,rename+".log")
    os.rename(logname, newlogname)
    logname = newlogname
    name = rename
        
    os.system(f"{os.path.abspath('./bazel-out/k8-opt/bin/utils/video_aligner')} -l {logname}")
    os.system(f"python {os.path.join(base,'analysis','plot_data.py')} -f {new_path}")
    