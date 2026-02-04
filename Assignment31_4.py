import os 
import sys
import shutil

def DirectoryScanner(DirName1 , DirName2 , FileExtension):
    Border = "-" * 50

    fobj = open("Mangyaa.Log","w") 
    os.mkdir(DirName2)                     # To create the new folder
    fobj.write(Border+"\n")
    fobj.write("This log file is created by Nandini\n")
    fobj.write(f"This is script to copy the file {DirName1} into {DirName2} with {FileExtension} \n")
    fobj.write(Border+"\n")

    Ret = False
    
    Ret = os.path.exists(DirName1)
    if(Ret == False):
        print("There is no such a directory")
        return 
    
    Ret = os.path.isdir(DirName1)
    if(Ret == False):
        print("It is not directory")
        return
     
    for FolderName , SubFolderName , FileName in os.walk(DirName1):

        for fName in FileName:
            
                oldpath = os.path.join(FolderName,fName)
                
                newpath = os.path.join(DirName2,fName)
                if(fName.endswith(FileExtension)):
                   shutil.copy(oldpath , newpath)              # To copy the files from 1 folder to another folder
                   fobj.write(f"{fName} copied from {DirName1} into {DirName2}\n")

    fobj.write(Border+"\n")

    fobj.close()            

def main():

    Border = "-" * 50
    print(Border)
    print("---------------Directory Automation---------------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Invalid Number of Arguments")
        print("Please specify the number of directory")
        return
    
    DirectoryScanner(sys.argv [1],sys.argv[2] , sys.argv[3])

    print(Border)
    print("---------------Directory Automation---------------")
    print(Border)

if __name__ == "__main__":
    main()
