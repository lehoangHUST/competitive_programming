# Read from the file file.txt and output the tenth line to stdout.
#!/bin/bash

# solution 1
sed -n 10p file.txt

# solution 2
tail -n+10 file.txt | head -1