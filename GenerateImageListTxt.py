import os
import random
import shutil
import sys

def get_files_no_txt_list(dir_location):
  all_files = os.listdir(dir_location)
  filenames = []
  
  for file in all_files:
    if file.endswith(".txt"):
      #skip txt
      continue
    else :
      filenames.append(  "MangroveDataset/"+dir_location+"/"+file  )
  return filenames

folder = sys.argv[1]
images = get_files_no_txt_list(folder)
with open(folder+'/files.txt', 'w') as f:
  for image in images:
    f.write(image+"\n")