# open file and store file object in a variable
file = open('Codingal.txt')

# read the contents of file
print(file.read())

# close the file
file.close()


# open the file in write mode
file_write = open('Codingal.txt', 'w')
# write in the file
file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old ")
file_write.close()

# open the file in append mode
file_append = open('Codingal.txt', 'a')
# append in the file 
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()






