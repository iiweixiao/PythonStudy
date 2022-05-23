# 作者:  Bruce
# 时间： 2022/4/19
src_file = open('pic1.webp', 'rb')
tar_file = open('pic1_copy.webp', 'wb')
tar_file.write(src_file.read())
src_file.close()
tar_file.close()

with open('pic1.webp', 'rb') as src_file1:
    with open('pic1-1.webp', 'wb') as tar_file1:
        tar_file1.write(src_file1.read())