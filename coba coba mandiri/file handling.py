import os
print(os.getcwd())  # Menampilkan direktori kerja saat ini

# 1. Using with block (recommended)
try:
    file = open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt" , 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: File 'sample.txt' tidak ditemukan. Pastikan file ada di direktori yang benar.")

# 2. Using open() dan close() manually

try:
    file = open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt" , 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: File 'sample.txt' tidak ditemukan. Pastikan file ada di direktori yang benar.") 


# 3. reading a file
with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt" , 'r') as file:
    content = file.read()
    print(content)

# 4. Writing to a file
with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt" , 'w') as file:
    file.write("sambil ditemani secangkir teh hangat. Hari ini adalah hari yang baik.")
    
with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt" , 'r') as file:
    print(file.read())

# 5. Appending to a file
with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt" , 'a') as file:
    file.write("\nIni adalah cerita ramayana yah bang")
    
with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt" , 'r') as file:
    print(file.read())
    

# 6. reading line into a list
with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt" , 'r') as file:
    lines = file.readlines()

print(lines)


# 7. iterating over each line a file
with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt" , 'r') as file:
    for line in file:
        print(line.strip())


# 8. Checking if a file exits
if os.path.exists("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt"):
    print('file exits')
else:
    print('file does not exits')

# 9. writing a list to a file
data = ["apple", "Banana", "Cherry"]

with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt", 'w') as file:
    for item in data:
        file.write(item + "\n")

with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt", 'r') as file:
    print(file.read())

# 10. Using with block for multiple files
with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt", 'w') as file1, open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample2.txt", 'w') as file2:
    file1.write('this is file 1')
    file2.write('this is file 2')

with open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample.txt", 'r') as file1, open("C:/Users/HP/OneDrive/Documents/GitHub/SIC6/coba coba mandiri/sample2.txt", 'r') as file2:
    print(file1.read())
    print(file2.read())


# 11. 
    