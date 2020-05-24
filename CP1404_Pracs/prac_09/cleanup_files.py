"""
CP1404/CP5632 Practical
Cleanup files program
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        #Option 1: rename file to new name - in place
        os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        #shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    print(new_name)
    for i in range(len(new_name)):
        temp=new_name[i]
        temp1 = new_name[i-1]
        temp2 = new_name[:i]
        temp3 = new_name[i:]
        if new_name[i].isupper() and new_name[i-1].islower():
            # if the current character is upper case and the previous case is lowercase
            if i-1 == -1:
                # Pass if it is the first letter in the name
                pass
            else:
                new_name = new_name[:i] + '_' + new_name[i:]
                # Add '_' in desired location
        elif new_name[i].islower() and new_name[i-1] == '_':
            # if a lower case letter follows an underscore
            new_name = change_to_upper(new_name, i)
        elif i == 0 and new_name[i].islower:
            # if the first letter is lowercase
            new_name = change_to_upper(new_name, i)
        elif new_name[i].isupper() and new_name[i-1].isupper():
            # If an uppercase letter is followed by an uppercase letter
            if i-1 == -1:
                pass
            else:
                new_name = new_name[:i] + '_' + new_name[i:]

    return new_name

def change_to_upper(new_name, i):
    old_name = new_name
    name_list = list(old_name)
    name_list[i] = new_name[i].upper()
    new_name = ''.join(name_list)
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))


        for filename in filenames:
            path_name = os.path.join(directory_name, filename)
            print(path_name)
            corrected_name = os.path.join(directory_name, get_fixed_filename(filename))
            print(corrected_name)
            os.rename(path_name, corrected_name)

# main()
demo_walk()