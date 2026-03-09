pages = 100
lines_in_page = 50
chars_in_line = 25
bytes_in_char = 4
disk_mb = 1.44
disk_bytes = disk_mb * 1024 * 1024
book_bytes = pages * lines_in_page * chars_in_line * bytes_in_char
num_books = int(disk_bytes // book_bytes)
print("Количество книг, помещающихся на дискету:", num_books)
