# Python
Python Basics


#Important points related to os module

The OS module allows us to interact wiht the underlying operating system in several different ways.

- Navigate the file system
- Get file information
- Look up and change the environment variables
- Move files around
- Many more

To begin, import the os module. This is a built in module, no third party modules need to be installed.


# Get current working directory
os.getcwd()


# Change directory, this requires a path to change to
os.chdir(path)


# List directory, you can pass a path, but by default it is in the current directory
os.listdir()


# Multiple options for creating directories
mkdir()  # Use for making one directory
makedirs(). # Use if you want to create multiple directories at once


# Remove directories
rmdir(file). # Recommended use case
removedirs(file)  # Removes intermediate directories if specified


# Rename a file or folder
os.rename(‘test.txt’, ‘demo.txt’). # This renames text.txt to demo.txt


# Look at info about files
os.stat(test.txt)
# Useful stat results: st_size (bytes), st_mtime (time stamp)


# To see entire directory tree and files within
# os.walk is a generator that yields a tuple of 3 values as it walks the directory tree

for dirpath, dirnames, filenames in os.walk(routepath): 
    print(‘Current Path:’, dirpath)
    print(‘Directories:’, dirnames)
    print(‘Files:’, filenames)
    print()

# This is useful for locating a file that you can’t remember where it was
# If you had a web app, and you wanted to keep track of the file info within a certain directory structure, then you could to thru the os.walk method and go thru all files and folders and collect file information.


# Access home directory location by grabbing home environment variable
os.environ.get(‘HOME’). # Returns a path
# To properly join two files together use os.path.join()
file_path = os.path.join(os.environ.get(‘HOME’), ‘test.txt’)
# the benefit of os.path.join, is it takes the guess work out of inserting a slash


# os.path has other useful methods

os.path.basename
# This will grab filename of any path we are working on

os.path.dirname(‘/tmp/test.txt’)
# returns the directory /tmp

os.path.split(‘/tmp/test.txt’)
# returns both the directory and the file as a tuple

os.path.exists(‘/tmp/test.txt’)
# returns a boolean

os.path.isdir(‘/tmp/test.txt’)
# returns False

os.path.isfile(‘/tmp/test.txt’)
# returns True

os.path.splitext(‘/tmp/test.txt’)
# Splits file route of the path and the extension
# returns (‘/tmp/test’, ‘.txt’)
# This is alot easier than parsing out the extension. Splitting off and taking the first value is much better.
# Very useful for file manipulation

