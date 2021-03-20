print("Welcome to the program that could change your txt to srt for your video subtitle \n")

# allow the user to enter the file name which located in the same folder with this .py file
srt_file_name = input("Enter your .srt file name: ")
txt_file_name = input("Enter your .txt file name: ")

# check whether the files are exist in the same folder
try:
    srt_caption = open(srt_file_name + ".srt", "r")
    txt_caption = open(txt_file_name + ".txt", "r")

# catch the error, and remind the user to check the files location if this occurs
except FileNotFoundError as a:
    print("\n", a)
    exit()

# a function to read how many lines are there in the file
def file_len(fname):
    for i, l in enumerate(fname):
        pass
    return i + 1

# call the function to know how many lines are there in the file, and divide by 4 for the .srt file, as it's one caption uses 4 lines
srt_lines = file_len(srt_caption)
srt_lines_match = srt_lines/4
txt_lines_match = file_len(txt_caption)

# print the lines of the files
print("Lines of the .srt: ", srt_lines_match)
print("Lines of the .txt: ",txt_lines_match)

# check if the two file lines are the same
if srt_lines_match == txt_lines_match:
    print("Both files match")

    # allow the user to enter the new file name that will created
    new_file_name = input("Enter your new file name: ")

    # reset the pointer of the program in those files
    txt_caption.seek(0)
    srt_caption.seek(0)

    # read in lines of the files, and create the new .srt file
    txt_lines = txt_caption.readlines()
    captions = srt_caption.readlines()
    output_srt = open(new_file_name + ".srt", "w")

    # now change the caption lines, using a for loop, to go through both files, and copy it from the .txt, and paste it to .srt
    for i in range(txt_lines_match):
        text = txt_lines[i]
        if i == 0:
            k = 2
        else:
            k += 4
        captions[k] = text

    # create the new file and write the file
    output_srt.writelines(captions) 
    print("New file created with new captions.")

    output_srt.close()
else:
    print("It don't match \nCheck both files again...")

# close the files
txt_caption.close()
srt_caption.close()
