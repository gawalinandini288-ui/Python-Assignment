import sys
import os

def DirectoryScanner(DirName,Filextension):
   Border = "-" * 50
   
   fobj = open("Assignment.log","w")

   fobj.write(Border+"\n")
   fobj.write("This is log file created by Nandini\n")
   fobj.write(f"This is the script for finding file in directory with{Filextension} \n")
   fobj.write(Border+"\n")

   Ret = False

   Ret = os.path.exists(DirName)
   if(Ret == False):
       print("There is no such directory")
       return  
   
   Ret = os.path.isdir(DirName)
   if(Ret == False):
       print("It is not a directory")
       return
   
   for FolderName , SubFolderName ,FileName in os.walk(DirName):
       

       for fName in FileName:
            fName = os.path.join(FolderName,fName)
            if fName.endswith(Filextension):
              fobj.write(fName+"\n")
           
   
   fobj.write(Border+"\n")

   fobj.close()

def main():
    Border = "-" * 50
    print(Border)
    print("------------Directory Automation------------------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalide Number of arguments")
        print("Please specify the name of directory")
        return 
    
    DirectoryScanner(sys.argv[1] , sys.argv[2])
    
    print(Border)
    print("------------Directory Automation------------------")
    print(Border)

if __name__ == "__main__":
    main()