import sys
from os import makedirs as mkdirs
from shutil import rmtree as rmfr
from json import loads as jload
from fnmatch import fnmatch as match
from zipfile import ZipFile as zipf
from os.path import exists

def failure():
    print 'Patcher failed! Please make sure you have cloned correctly!'
    sys.exit(1)

class RyzenPatcher():

    files123 = {
        'patches' : 'ryzenFiles.zip',
        'tempDir' : './tmp/patcheR'
        }

    def check_for_files(self):
        try:
            # remove the extracted files if they are there
            if exists(self.files['tempDir']):
                rmfr(self.files['tempDir'])
            # make the temp dir
            mkdirs(self.files['tempDir'])
            if exists(self.files['patches']):
                with zipf(self.files['patches'], "r") as zipr:
                    zipr.extractall(self.files['tempDir'])
        except:
            failure()


def chameleon_bootloader():
    return None


if __name__ == "__main__":
    ryzen = RyzenPatcher()
    ryzen.check_for_files()
    print 'lets see if it gets here!'