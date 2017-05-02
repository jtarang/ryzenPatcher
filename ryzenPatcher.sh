# chmod +x this file 
# run it as sudo

echo "Type your destination path.. ie /Volumes/RyzenSierra :"
read pathToDisk

# ditto merges
ditto -V ~/Downloads/Ryzen\ Essentials/kernel_rc2_ryzen/Extensions/System.kext $pathToDisk/System/Library/Extensions/.
ditto ~/Downloads/Ryzen\ Essentials/kernel_rc2_ryzen/Extensions/System.kext $pathToDisk/System/Library/Extensions/.
ditto -V ~/Downloads/Ryzen\ Essentials/kernel_rc2_ryzen/Frameworks/IOKit.framework/* $pathToDisk/System/Library/Frameworks/IOKit.framework/*
ditto -V ~/Downloads/Ryzen\ Essentials/kernel_rc2_ryzen/Frameworks/Kernel.framework/* $pathToDisk/System/Library/Frameworks/Kernel.framework/*
ditto -V ~/Downloads/Ryzen\ Essentials/kernel_rc2_ryzen/Frameworks/System.framework/* $pathToDisk/System/Library/Frameworks/System.framework/*

# cp bronya kernel over
cp -rv ~/Downloads/Ryzen\ Essentials/kernel_rc2_ryzen/Kernels/kernel $pathToDisk/System/Library/Kernels/.

# these are the Spakk extensions
cp -rv ~/Downloads/Extra/Extensions/* $pathToDisk/System/Library/Extensions/.

# prelinked error
# source : http://www.insanelymac.com/forum/topic/308384-how-to-rebuild-my-prelinked-kernel-after-updating-to-el-capitan/
rm -f $pathToDisk/System/Library/PrelinkedKernels/prelinkedkernel 
kextcache -u $pathToDisk
