from os import getcwd, listdir, rename, rmdir
from shutil import move
from multiprocessing import Process

def Extend(Path):
    if len(listdir(Path)) == 0:
        rmdir(Path)
    else:
        if not "About" in listdir(Path):
            rename(f"{Path}\\{listdir(Path)[0]}", f"{Path}\\{listdir(Path)[0]}a")
            move(f"{Path}\\{listdir(Path)[0]}", getcwd())
        if len(listdir(Path)) == 0:
            rmdir(Path)

if __name__ == "__main__":
    pss = []
    for i in listdir(getcwd()):
        if not (".py" in i or ".exe" in i or ".txt"):
            p = Process(None, Extend, args=[f"{getcwd()}\\{i}"])
            pss.append(p)
            p.start()

    [proc.join() for proc in pss]
