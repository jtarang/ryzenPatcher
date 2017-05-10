import argparse
from os import makedirs as mkdirs
from shutil import rmtree as rmfr
from json import loads as jload
from fnmatch import fnmatch as match
from zipfile import ZipFile as zipf
from os import system
from os.path import exists
from sys import exit


class RyzenPatcher():

    files = {
        'patches' : '../ryzenFiles.zip',
        'tempDir' : './tmp/patcheR/ryzenFiles'
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

    def execute(self, pathToFiles, commands):
        cmds = commands.format(pathToFiles, args.volume, args.kernelVersion)
        for c in cmds.split('\n'):
            system(c)

    def everything(self):
        ditto_cmds = \
"""
export patchPath={}
export pathToDisk={}
export rcv={}
ditto -V $patchPath/RyzenEssentials/kernel_"$rcv"_ryzen/Extensions/System.kext $pathToDisk/System/Library/Extensions/.
ditto $patchPath/RyzenEssentials/kernel_"$rcv"_ryzen/Extensions/System.kext $pathToDisk/System/Library/Extensions/.
ditto -V $patchPath/RyzenEssentials/kernel_"$rcv"_ryzen/Frameworks/IOKit.framework/* $pathToDisk/System/Library/Frameworks/IOKit.framework/*
ditto -V $patchPath/RyzenEssentials/kernel_"$rcv"_ryzen/Frameworks/Kernel.framework/* $pathToDisk/System/Library/Frameworks/Kernel.framework/*
ditto -V $patchPath/RyzenEssentials/kernel_"$rcv"_ryzen/Frameworks/System.framework/* $pathToDisk/System/Library/Frameworks/System.framework/*
cp -rv $patchPath/RyzenEssentials/kernel_"$rcv"_ryzen/Kernels $pathToDisk/System/Library/Kernels
cp -rv $patchPath/Extra/Extensions/* $pathToDisk/System/Library/Extensions/.
rm -f $pathToDisk/System/Library/PrelinkedKernels/prelinkedkernel
kextcache -u $pathToDisk
"""

        self.execute(self.files['tempDir'], ditto_cmds)


    def kernel(self, pathToKernel):
        kernel_merge = \
"""
export patchPath={}
export pathToDisk={}
ditto -V $patchPath/Extensions/System.kext $pathToDisk/System/Library/Extensions/.
ditto -V $patchPath/Extensions/System.kext $pathToDisk/System/Library/Extensions/.
ditto -V $patchPath/Frameworks/IOKit.framework/* $pathToDisk/System/Library/Frameworks/IOKit.framework/*
ditto -V $patchPath/Frameworks/Kernel.framework/* $pathToDisk/System/Library/Frameworks/Kernel.framework/*
ditto -V $patchPath/Frameworks/System.framework/* $pathToDisk/System/Library/Frameworks/System.framework/*
cp -rv $patchPath/Kernels/ $pathToDisk/System/Library/Kernels
kextcache -u $pathToDisk
"""
        if exists(pathToKernel):
            self.execute(pathToKernel, kernel_merge)
        else:
            failure()



def failure():
    print 'Patcher failed! Please make sure you have cloned correctly!'
    exit(1)

def chameleon_bootloader():
    return None


if __name__ == "__main__":
    parser = argparse.\
    ArgumentParser(description='Image patcher for ryzen CPU')
    parser.add_argument('--volume',
                        help='volume to patch to target| --volume /Volumes/RyzenSierra', required=True)
    parser.add_argument('--kernelVersion',
                        help='version of kernel to use| --volume /Volumes/RyzenSierra --kernelVersion rc2', required=False)
    parser.add_argument('--kernelSwitch',
                        help='change kernel files only| --volume /Volumes/RyzenSierra --kernelSwitch ~/Downloads/kernel_rc2_ryzen', required=False)
    args = parser.parse_args()
    ryzen = RyzenPatcher()
    if args.kernelSwitch and not '':
        ryzen.kernel(args.kernelSwitch)
    else:
        if 'rc' in args.kernelVersion:
            pass
        else:
            failure()

        ryzen.check_for_files()
        ryzen.everything()
    print "\n\t\tPlease run kext wizard and rebuild caches!"
    print "\n\t\tPlease copy kernel file from {}/System/Library/Kernels/kernel to /Extra/Kernels/ and Extra/."

