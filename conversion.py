SOURCE_ENCODING = 'iso-8859-1'
TARGET_ENCODING = 'utf-8'
INPUT_FILE = 'backend/api/tests.py'
OUTPUT_FILE = 'backend/api/tests.py.tmp'

try:
    with open(INPUT_FILE, 'r', encoding=SOURCE_ENCODING) as infile, \
    open(OUTPUT_FILE, 'w', encoding=TARGET_ENCODING) as outfile:
        for line in infile:
            outfile.write(line)

    import os
    os.replace(OUTPUT_FILE, INPUT_FILE)

    print(f"File '{INPUT_FILE}' successfully converted to UTF-8.")

except Exception as e:
    print(f"Error converting file: {e}")
