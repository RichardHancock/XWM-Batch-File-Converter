import os
import subprocess

ConverterPath = "C:\\Users\\Richard\\Desktop\\Converter"
SrcPath = ConverterPath + "\\src"
DstPath = ConverterPath + "\\dst"

os.chdir(ConverterPath)

Files = os.listdir(SrcPath)

for SrcFile in Files:
    SrcFilePath = os.path.join(SrcPath,SrcFile)

    #Check if a file and not a directory
    if os.path.isfile(os.path.join(SrcPath,SrcFile)):

        print("Converting Source File: " + SrcFile)

        DstFile = SrcFile[:-3] + "wav"
        DstFilePath = os.path.join(DstPath,DstFile) #Need to add check for errors

        print("Converting...")
        subprocess.call(["xwmaencode.exe", SrcFilePath, DstFilePath])

        print("Created Output File: " + DstFile + "\n")

print("Conversion Finished")
