import os
import shutil
import stat
import fitz

os.chdir("C:/Users/Bluekey/Desktop/midterm_sorter")

unsorted = "C:/Users/Bluekey/Desktop/midterm_sorter/unsorted"

york = "C:/Users/Bluekey/Desktop/midterm_sorter/York University"
york_lst = os.listdir(york)

western = "C:/Users/Bluekey/Desktop/midterm_sorter/Western"
western_lst = os.listdir(western)

waterloo = "C:/Users/Bluekey/Desktop/midterm_sorter/Waterloo"
waterloo_lst = os.listdir(waterloo)

uoft = "C:/Users/Bluekey/Desktop/midterm_sorter/University of Toronto"
uoft_lst = os.listdir(uoft)

ryerson = "C:/Users/Bluekey/Desktop/midterm_sorter/Ryerson University"
ryerson_lst = os.listdir(ryerson)

guelph = "C:/Users/Bluekey/Desktop/midterm_sorter/University of Guelph"
guelph_lst = os.listdir(guelph)

mcmaster = "C:/Users/Bluekey/Desktop/midterm_sorter/McMaster"
mcmaster_lst = os.listdir(mcmaster)



unsorted_lst = os.listdir(unsorted)
dir_size = len(unsorted_lst)


i = 0
while i < dir_size:
    print(unsorted_lst[i])
    doc = fitz.open(unsorted + "/" + unsorted_lst[i])
    #currently only inspecting first page for which school
    page = doc[0]
    text = page.getText()
    #if "York" in text:
    if "York" in text:
        os.chmod(york, stat.S_IWRITE)
        shutil.copy("unsorted/" + unsorted_lst[i], york)
    elif "Waterloo" in text:
        os.chmod(waterloo, stat.S_IWRITE)
        shutil.copy("unsorted/" + unsorted_lst[i], waterloo)
    elif "Ryerson" in text:
        os.chmod(ryerson, stat.S_IWRITE)
        shutil.copy("unsorted/" + unsorted_lst[i], ryerson)
    #currently I believe this college is in Guelph
    elif "Guelph" or "College of Business and Economics" in text:
        os.chmod(guelph, stat.S_IWRITE)
        shutil.copy("unsorted/" + unsorted_lst[i], guelph)
    elif "McMaster" in text:
        os.chmod(mcmaster, stat.S_IWRITE)
        shutil.copy("unsorted/" + unsorted_lst[i], mcmaster)
    elif "Western" in text:
        os.chmod(western, stat.S_IWRITE)
        shutil.copy("unsorted/" + unsorted_lst[i], western)
    #accounting for Rotman Commerce that may not include the U of T in it
    elif "Toronto"or "Rotman" in text:
        os.chmod(uoft, stat.S_IWRITE)
        shutil.copy("unsorted/" + unsorted_lst[i], uoft)
    #oxdia files are also U of T midterms but adding "-oxdia" at the end to signify that it has watermark
    elif "www.oxdia.com" in text:
        os.chmod(uoft, stat.S_IWRITE)
        shutil.copy("unsorted/" + unsorted_lst[i], uoft + " Oxdia")
    i += 1




