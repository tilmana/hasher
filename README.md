# hasher

Simple MD5 hasher that can generate both text and file checksums.

usage:

python3 hasher.py -t {text}
python3 hasher.py -f {file_location}


Text mode reads all input after the -t, so you can do: "python3 hasher.py -t test1 test2 test3" and the script will generate the checksum on: "test1 test2 test3".

Invalid use will make the script prompt the user manually for input, ensuring that the script use still goes through without having to re-run it.
