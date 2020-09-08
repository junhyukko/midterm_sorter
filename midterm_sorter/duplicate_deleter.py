import os
import shutil
import stat

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

moved_files_lst = york_lst + western_lst + waterloo_lst + uoft_lst + ryerson_lst + guelph_lst + mcmaster_lst
for item in moved_files_lst:
    if item in unsorted_lst:
         unsorted_lst.remove(item)
         os.remove(unsorted + "/" + item)