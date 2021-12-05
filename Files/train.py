# this file get all the images form the data/obj folder 
# and creates a file train.txt with contaiting list of all images

import os
files_list = []

path = os.path.join('data', 'obj')
#list all files
for file in os.listdir(path):
    if file.endswith('.jpg'):
        files_list.append(("data/obj/"+file))
print(files_list) 
with open("data/train.txt","w") as new_file:
    for file in files_list:
        new_file.write(file)
        new_file.write("\n")
    new_file.close()
