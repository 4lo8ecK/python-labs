# tasks: 1.1, 2.15, 3.20, 4.18, 5.12

import sys

import os

import shutil
from pathlib import Path as pt

import zipfile

import random as rnd
import time

class Task1:
    PROJ_DIR = 'project'
    SRC_DIR = 'src'
    DOCS_DIR = 'docs'
    TESTS_DIR = 'tests'

    @staticmethod
    def mkdir(path) -> None:
        if not os.path.exists(path):
            os.mkdir(path)

    @staticmethod
    def touch(path: str) -> None: # touch - команда в unix системах
        with open(path, mode='w') as fl:
            pass

    @staticmethod
    def rm_rf(path: str) -> None:
        try:
            shutil.rmtree(path)
        except: pass

    @staticmethod
    def free() -> None:
        Task1.rm_rf(Task1.PROJ_DIR)

    def __init__(self) -> None:
        pass

    def exec(self) -> None:
        self.mkdir(self.PROJ_DIR)

        src_path = os.path.join(self.PROJ_DIR, self.SRC_DIR)

        self.mkdir(src_path)
        self.mkdir(os.path.join(self.PROJ_DIR, self.DOCS_DIR))
        self.mkdir(os.path.join(self.PROJ_DIR, self.TESTS_DIR))

        for i in range(3):
            new_fl_relative_path = os.path.join(src_path, f'file-{i}.py')
            self.touch(new_fl_relative_path)
            print(pt(new_fl_relative_path).resolve())

class Task2(Task1):

    SRC1_DIR = 'src1'
    SRC2_DIR = 'src2'
    MRGD_DIR = 'merged'

    @staticmethod
    def gen_files(name: str = '', ext:str = 'txt', path: str = './', count: int = 1) -> None:
        for i in range(count):
            Task2.touch(os.path.join(path, f"{name}-{i}.{ext}"))

    @staticmethod
    def get_files_list(path: str) -> list:
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    @staticmethod
    def get_dirs_list(path: str) -> list:
        return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]


    @staticmethod
    def cp(old: str, new: str) -> None:
        shutil.copy2(old, new)

    @staticmethod
    def free() -> None:
        Task2.rm_rf(Task2.SRC1_DIR)
        Task2.rm_rf(Task2.SRC2_DIR)
        Task2.rm_rf(Task2.MRGD_DIR)

    def __init__(self) -> None:
        self.mkdir(self.SRC1_DIR)
        self.mkdir(self.SRC2_DIR)
        self.mkdir(self.MRGD_DIR)

        self.gen_files(name="src1", path=self.SRC1_DIR, count=10)
        self.gen_files(name="src2", path=self.SRC2_DIR, count=10)
    
    def exec(self) -> None:
        for fl in self.get_files_list(self.SRC1_DIR):
            self.cp(os.path.join(self.SRC1_DIR, fl), os.path.join(self.MRGD_DIR, fl))
        for fl in self.get_files_list(self.SRC2_DIR):
            self.cp(os.path.join(self.SRC2_DIR, fl), os.path.join(self.MRGD_DIR, fl))

class Task3(Task2):
    DIR1 = 'dir1'
    DIR2 = 'dir2'
    DIR3 = 'dir3'

    @staticmethod
    def gen_dir(path: str = '', filenames: str = '', ext: str = 'txt', files_min: int = 1, files_max: int = 20) -> None:
        Task3.mkdir(path)
        Task3.gen_files(name=filenames, ext=ext, path=path, count=rnd.randint(files_min, files_max))

    @staticmethod
    def free() -> None:
        Task3.rm_rf(Task3.DIR1)
        Task3.rm_rf(Task3.DIR2)
        Task3.rm_rf(Task3.DIR3)


    def __init__(self) -> None:
        rnd.seed(int((time.time() * 10000) % 10000))    # unix-time для случайного сида

        self.gen_dir(path=self.DIR1, filenames=self.DIR1)
        self.gen_dir(path=self.DIR2, filenames=self.DIR2)
        self.gen_dir(path=self.DIR3, filenames=self.DIR3)
    
    def exec(self) -> None:
        dirs = self.get_dirs_list('./')

        for i in dirs:
            if len(self.get_files_list(i)) > 10:
                self.rm_rf(i)

class Task4(Task3):

    def exec(self) -> None:
        dirs = self.get_dirs_list('./')
        for i in dirs:
            if len(self.get_files_list(i)) > 10:
                print(i)

class Task5(Task4):
    TEXT_FILE = 'text.txt'
    TASK5_DIR = 'task5'

    @staticmethod
    def free() -> None:
        Task5.rm_rf(Task5.TASK5_DIR)

    def __init__(self) -> None:
        self.mkdir(self.TASK5_DIR)

    def exec(self) -> None:
        with zipfile.ZipFile(os.path.join(self.TASK5_DIR, f"{self.TEXT_FILE}.zip"), mode='w', compression=zipfile.ZIP_DEFLATED) as arc:
            arc.write(self.TEXT_FILE)
        

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(0)
    arg = sys.argv[1]
    if arg == 'free':
        Task1.free()
        Task2.free()
        Task3.free()
        Task4.free()
        Task5.free()
        sys.exit(0)

    elif arg == '1':
        t = Task1()
        t.exec()

    elif arg == '2':
        t = Task2()
        t.exec()

    elif arg == '3':
        t = Task3()
        t.exec()

    elif arg == '4':
        Task4.free()
        t = Task4()
        t.exec()
    elif arg == '5':
        t = Task5()
        t.exec()