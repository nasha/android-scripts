# Android-Scripts

# android_res_move.py
- Takes in 3 arguments
- source folder path containing the sub folders (e.g. mdpi, ldpi, ..)
- destination folder path (where you want to copy the files)
  - if it does not find the sub folder created, it will create them
- filename (e.g. "ic_push.png")
- Rename and Copy
  - If you want to rename the newly copied file to something else as well, you can add the new filename (along with extension) as the fourth argument.
  - If you do not want to rename the file, the extra argument is not needed.

- Run
  - python android_res_move.py [SOURCE] [DEST] [FILENAME] [NEW_FILE_NAME]

