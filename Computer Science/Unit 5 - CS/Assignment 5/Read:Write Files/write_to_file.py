# Writing to file example
# opens the file "myTempFile.txt". The 'a' will append (add) to the end of the file
#****ONLY WORKS WITH STRINGS*****

#----METHOD 1-----
#writes to myTempFile.. changes everytime is saved
file1 = open("myTempFile.txt","a")  #(APPENDS to exisiting file) (doesn't remove previous)
file1.write("\nHello") #stops here, and continues onto next line, and on same lineline, (since no \n)
file1.write("\nWorld")
file1.close() #need to include - or else file may become corrupted, and locks file
# file must be closed in order to correctly use to the file

#*****File will keep what is existing previously, and thus there will be no changes to the list, just added to strings***** 


#----METHOD 2-----
#writes to myTempFile2... changes everytime saved
#preferable method since close() is automatic
# another way (close file automatically when the indented code is completed)
# creates a file "myTempFile2.txt".
# The 'w' will create a new file (deleting any existing file)
with open("myTempFile2.txt", 'w') as file2:  #instead of R (READ ONLY), using w (WRITE) - (creates a new file. If anything is there, it is deleted and writes over it)
    file2.write("Hello  World ") #as soon as done writing, file will close
    file2.write("Goodbye World ") #as soon as done writing, file will close
# 'w' write over existing file (loses current content)
    
