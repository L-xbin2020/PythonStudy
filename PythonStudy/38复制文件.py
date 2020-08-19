file_read = open("README")
file_write = open("readme_c", "w")

# text = file.read()
# file_write.write(text)
while True:
    # 读取一行内容
    text = file_read.readline()

    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()
