# Read from the file file.txt and output all valid phone numbers to stdout.
#!/bin/bash

# File input
file="file.txt"

# Regex để kiểm tra định dạng số điện thoại
regex="^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$"

# Đọc từng dòng từ file
while IFS= read -r line; do
    # Kiểm tra xem chuỗi có khớp định dạng không
    if [[ $line =~ $regex ]]; then
        echo "$line"
    fi
done < "$file"