import glob
import sys
import getopt
import os
from zipfile import ZipFile, ZIP_DEFLATED


class AppHackerRankQuiz:

    def __init__(self):
        self.str_full_argv = sys.argv
        self.str_opt_argv = self.str_full_argv[1:]
        self.str_path_extension = self.str_opt_argv[0]

    def main(self, param1=None):
        txtfiles = []
        nameOnly = []


        for file in glob.glob(self.str_path_extension):
            txtfiles.append(file)
            nameOnly.append(file.split(os.sep)[-1])

        print(txtfiles)
        print(txtfiles[0][:-3])

        for i in range(len(txtfiles)):
            file = txtfiles[i]
            name = nameOnly[i]

            with ZipFile(file[:-3] + "zip", mode='w', compression=ZIP_DEFLATED, compresslevel=9) as obj_zip:
                print("Zipping ..." + file + " ... as ... " + file[:-3] + "zip")
                obj_zip.write(file, name)


