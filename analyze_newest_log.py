import os
from os.path import dirname, basename, splitext
import glob
import pandas
import argparse
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",type=str, default="", help="file to analyze. If no file given, it analyzes the latest file.")
    parser.add_argument("-n", "--name",type=str, default="", help="name for output folder")
    args = parser.parse_args()
    
    base = dirname(__file__)
    if args.file: 
        logname = os.path.abspath(args.file)
        os.chdir(base)
    else:
        os.chdir(base)
        
        try:
            logname = os.path.abspath(sorted(glob.glob("mjbots-quada1*.log"),reverse=True)[0])
        except IndexError:
            print("no file found")
            exit()
    name = splitext(basename(logname))[0]
    
    if args.name:
        rename = args.name
    else:
        try:
            csv = pandas.read_csv(os.path.join(base,"gains.csv"))
            rename = f"kp{csv.kp[0]}kd{csv.kd[0]}"
        except:
            rename = False
        # rename = input("New name for data: ")
        if not rename:
            rename = name
    new_path = os.path.join(base,"analysis",rename,"")
    try:
        os.makedirs(new_path,exist_ok=False)
    except FileExistsError:
        if input(f"File {new_path} already exists. Overwrite? Y/n\n") not in {"","Y","y","J","j"}:
            exit()
    newlogname = os.path.join(new_path,rename+".log")
    # os.rename(logname, newlogname)
    try:
        shutil.copyfile(logname, newlogname)
    except shutil.SameFileError:
        pass
    logname = newlogname
    name = rename
        
    os.system(f"{os.path.abspath('./bazel-out/k8-opt/bin/utils/video_aligner')} -l {logname}")
    os.system(f"python {os.path.join(base,'analysis','plot_data.py')} -f {new_path}")
    