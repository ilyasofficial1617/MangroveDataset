import os
import random
import shutil

def get_annotated(dir_location):
  all_files = os.listdir(dir_location)
  annotated = []
  
  for file in all_files:
    if file.endswith(".txt"):
      if(file=="classes.txt"):
        #skip classes txt
        continue
      #get filename only without extension
      annotated.append(    os.path.splitext(file)[0]    )
  return annotated
  
annotated_mangrove = get_annotated("annotated/mangrove")
print("annotated mangrove length = ",len(annotated_mangrove))
annotated_tree = get_annotated("annotated/tree")
print("annotated tree length = ",len(annotated_tree))

#length of array
n_mangrove = len(annotated_mangrove)
n_tree = len(annotated_tree)

#randomize array for each class
random.shuffle(annotated_mangrove)
random.shuffle(annotated_tree)

#pick 80 20
mangrove_train = annotated_mangrove[:(n_mangrove*8//10)]
mangrove_test = annotated_mangrove[(n_mangrove*8//10):]
tree_train = annotated_tree[:(n_tree*8//10)]
tree_test = annotated_tree[(n_tree*8//10):]

#combine into one train and one test
train = mangrove_train + tree_train
test = mangrove_test + tree_test

#shuffle again
random.shuffle(train)
random.shuffle(test)

#empty out the folder first
rm_train_files = os.listdir("8020/train")
for rm_file in rm_train_files:
  os.remove("8020/train/"+rm_file)
rm_test_files = os.listdir("8020/test")
for rm_file in rm_test_files:
  os.remove("8020/test/"+rm_file)

#copy from annotated to 8020
dest = "8020/"
for dataname in train:
  if os.path.isfile("annotated/mangrove/"+dataname+".txt"):
    shutil.copy("annotated/mangrove/"+dataname+".jpg", dest+"train")
    shutil.copy("annotated/mangrove/"+dataname+".txt", dest+"train")
  else : 
    shutil.copy("annotated/tree/"+dataname+".jpg", dest+"train")
    shutil.copy("annotated/tree/"+dataname+".txt", dest+"train")
    
for dataname in test:
  if os.path.isfile("annotated/mangrove/"+dataname+".txt"):
    shutil.copy("annotated/mangrove/"+dataname+".jpg", dest+"test")
    shutil.copy("annotated/mangrove/"+dataname+".txt", dest+"test")
  else : 
    shutil.copy("annotated/tree/"+dataname+".jpg", dest+"test")
    shutil.copy("annotated/tree/"+dataname+".txt", dest+"test")