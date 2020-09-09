import os
import shutil
import stat
import fitz

os.chdir("C:/Users/Bluekey/Desktop/midterm_sorter")

unsorted = "C:/Users/Bluekey/Desktop/midterm_sorter/unsorted"

uoft = "C:/Users/Bluekey/Desktop/midterm_sorter/University of Toronto"
uoft_lst = os.listdir(uoft)

unsorted_lst = os.listdir(unsorted)
dir_size = len(unsorted_lst)


i = 0
while i < dir_size:
    print(unsorted_lst[i])
    doc = fitz.open(unsorted + "/" + unsorted_lst[i])
    #currently only inspecting first page for which school
    page = doc[0]
    text = page.getText()
    print(text)
    if text.find("www.oxdia.com") != -1:
        os.chmod(uoft, stat.S_IWRITE)
        shutil.copy("unsorted/" + unsorted_lst[i], uoft + " Oxdia")

    # l = -1
    # while l > -(len(text) + 1):
    #     if text[l].find("www.oxdia.com"):
    #         os.chmod(uoft, stat.S_IWRITE)
    #         shutil.copy("unsorted/" + unsorted_lst[i], uoft + " Oxdia")
    #     l -= 1    
    i += 1