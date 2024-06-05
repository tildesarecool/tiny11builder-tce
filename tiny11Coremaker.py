# based upon
#  tiny11Coremaker.ps
# by Tiny11 by ntdevlabs - https://github.com/ntdevlabs/tiny11builder
# 5 June 2024
# 
#  Todo: check if script is running with local admin privileges.
#  Probably implment this last or later at least
# 
# 
import os

def get_processor_architecture():
    # processor_architecture = os.getenv('PROCESSOR_ARCHITECTURE')
    if os.getenv('PROCESSOR_ARCHITECTURE'):
        #print("processor arch found")
        return os.getenv('PROCESSOR_ARCHITECTURE')
    else:
        print("no value for processor arch found")
        return False

def set_temp_dir():
    defpath = os.getenv('USERPROFILE') + "\documents\\tiny11"
    if os.path.exists(defpath):        
        print(f"defpath is {defpath}")
    else:
        os.makedirs(defpath)
        print(f"Folder successfully created: {defpath}")
    print(f"Please enter path for a temp directory.\
    \nDefault: ({os.getenv('USERPROFILE')}\documents\\tiny11) \
    \nNote: Assume at least ~20GB of drive space will be required (for ISOs etc) ")
    setworkpath = input("Enter a path (no quotes): ")
    setworkpath = setworkpath.strip()

    if setworkpath == "":
        print(f"Working directory set to {defpath}")
        return defpath

    elif setworkpath != "":
        if os.path.exists(setworkpath):
            print(f"You entered '{setworkpath}', which does exist")
            return setworkpath
        else:
            print(f"The path '{setworkpath}' could not be found. Things to check: no quotes are required, make sure path is a folder not a file, also try shift+right click to 'copy as path' a folder and paste")
            return False

#        \nIf no path is entered then the a subdirectory called tiny 11 will be created in your 'documents' folder \
#        \n ")
#    pass



if __name__ == "__main__":
    cpu_arch = get_processor_architecture()
    set_temp_dir()
    print(f"CPU arch is {cpu_arch}")
