from pathlib import Path

while True:
    print("Welcome to RB File Finder tool! This tool allows you to scan any directory on your computer and its subfolders \nto find the file you're looking for, or all the files that contain the specific format you've entered! ")
    directory_input = input("Enter your directory name (Example: /path/to/directory): ")
    directory = Path(directory_input)

    if not directory.exists():
        print("Error: Directory not found or does not exist!")
    else:
        r_or_not = input("Would you like to scan its subfolders aswell? (Y/N): ").upper()

        while r_or_not not in ("Y", "N"):
            r_or_not = input("Please enter Y or N: ")

        files_input = input("Enter your file name or file format (The file format has to start with a '*' for example: *.txt): ")

        if r_or_not == "Y":
            files = list(directory.rglob(files_input))

        if r_or_not == "N":
            files = list(directory.glob(files_input))

        if not files:
            print("No files were found!")
        else:
            for file in files:
                print(file)

            print(f"{len(files)} files were found.")

    again = input("Would you like to run the program again? (Y/N): ").upper()

    while again not in ("Y", "N"):
        again = input("Please enter Y or N: ")

    if again == "N":
        break