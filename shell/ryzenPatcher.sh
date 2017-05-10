# chmod +x this file 
# run it as sudo
printf "\n\nRemember this does not configure/install the bootloader yet. Just the image."
sleep 3

printf "\n\n"
echo "Type your destination path.. ie /Volumes/RyzenSierra :"
read pathToDisk
printf "\nWriting files to " + $pathToDisk + "\n\n"
sleep 4

rFiles=../ryzenFiles.zip

# if extracted files are there remove em | we don't trust them
if [ -d /tmp/rPatcher ]; then
    echo "Removing Temp Files"
    rm -r /tmp/rPatcher
fi

# if can't find the zip file exit
if [ ! -f $rFiles ]; then
    echo "Files not found, make sure you are in the same path as the source."
    exit
fi

#unzip before 
mkdir -p /tmp/rPatcher
unzip ../ryzenFiles.zip -d /tmp/rPatcher 
sleep 4

# ditto merges
ditto -V /tmp/rPatcher/RyzenEssentials/kernel_rc2_ryzen/Extensions/System.kext $pathToDisk/System/Library/Extensions/.
ditto /tmp/rPatcher/RyzenEssentials/kernel_rc2_ryzen/Extensions/System.kext $pathToDisk/System/Library/Extensions/.
ditto -V /tmp/rPatcher/RyzenEssentials/kernel_rc2_ryzen/Frameworks/IOKit.framework/* $pathToDisk/System/Library/Frameworks/IOKit.framework/*
ditto -V /tmp/rPatcher/RyzenEssentials/kernel_rc2_ryzen/Frameworks/Kernel.framework/* $pathToDisk/System/Library/Frameworks/Kernel.framework/*
ditto -V /tmp/rPatcher/RyzenEssentials/kernel_rc2_ryzen/Frameworks/System.framework/* $pathToDisk/System/Library/Frameworks/System.framework/*

# cp bronya kernel over
cp -rv /tmp/rPatcher/RyzenEssentials/kernel_rc2_ryzen/Kernels $pathToDisk/System/Library/

# these are the Spakk extensions
cp -rv /tmp/rPatcher/Extra/Extensions/* $pathToDisk/System/Library/Extensions/.

# prelinked error
# source : http://www.insanelymac.com/forum/topic/308384-how-to-rebuild-my-prelinked-kernel-after-updating-to-el-capitan/
rm -f $pathToDisk/System/Library/PrelinkedKernels/prelinkedkernel
rm -r /tmp/rPatcher
kextcache -u $pathToDisk

echo "All done / Enjoy!"
