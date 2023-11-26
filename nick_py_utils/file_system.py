import os
""" A utility module for working with files """


def path_exists(path, level="print"):
    if not os.path.exists(path):
        if level == "silent":
            pass
        elif level == "print":
            print(f"Error: {path} not found")
        elif level == "except":
            raise Exception(FileNotFoundError)
        return False
    return True


# Will create a dirctory recursively, or exit and return False if directory exists
def create_dir(the_path):
    """Creates a directory on the file system, will create multiple directory levels if needed"""
    if path_exists(the_path):
        return False
    os.makedirs(the_path)
    return True


def delete_path(path):
    """ deletes a file or dir """
    import os
    import shutil

    if not path_exists(path):
        return False
    if os.path.isfile(path):
        # It's a file, remove it
        os.remove(path)
        return True
    elif os.path.isdir(path):
        # It's a directory, remove it and its contents
        shutil.rmtree(path)
        return True
    return False

def create_empty_file(path):
    with open(path, 'w'):
        pass

# quick and dirty file write
def write(filename, in_string):
    if not path_exists(filename):
        return False
    with open(filename, "w") as the_file:
        the_file.write(in_string)
    return True

 
# quick and dirty file append
def append(filename, in_string):
    if not path_exists(filename):
        return False
    with open(filename, "a") as the_file:
        the_file.write(in_string)


def to_string(filename):
    """ Get an entire file back as a string(non-buffering: loads entire file into memory, not meant for large files). """
    if not path_exists(filename):
        return False

    with open(filename, "r") as the_file:
        return the_file.read()



def list_all_in_dir(mypath, recurse=False, path=False):
    """ 
    Returns a string list of every file in a directory. 
    Pass recurse=True to get a list of all files in subdir as well.
    Pass path=True to get the full path instead of just file name.
    
    """
    if recurse:
        out = []
        for f in os.listdir(mypath):
            loc = os.path.join(mypath, f)
            if os.path.isfile(loc):
                if path:
                    out.append(loc)
                else:
                    out.append(f)
            elif os.path.isdir(loc):
                out = out + list_all_in_dir(loc, True, path)
        return out
    else:
        return [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]


def create_zip_file(input_location, output_location):
    import zipfile, shutil
    """
    can be file or directory,
    Note: .zip extension will be automatically appended to output_location string
    """
    # remove trailing zip extension if present
    output_location = output_location.split(".")
    if output_location[-1] == "zip":
        del output_location[-1]
    output_location = ".".join(output_location)
    try:
        if os.path.isdir(input_location):
            shutil.make_archive(output_location, 'zip', input_location)
        elif os.path.isfile(input_location):
            zipfile.ZipFile(f"{output_location}.zip", mode='w').write(input_location)
        else:
            raise Exception("Input path was neither a file or a directory or could not be found.")
    except Exception as e:
        print("Zip file not created Successfully: " + output_location)
        raise Exception(e)
    print("Zip file was created Successfully:" + output_location)