import os

def combine_files_to_text(output_file="combined_output.txt"):
    # Open the output file in write mode
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Iterate over all files in the current directory
        for file_name in os.listdir("."):
            # Ensure we process only files (not directories)
            if os.path.isfile(file_name):
                # Extract file name and extension
                name, extension = os.path.splitext(file_name)
                
                # Read the file content
                try:
                    with open(file_name, "r", encoding="utf-8") as infile:
                        content = infile.read()
                except Exception as e:
                    content = f"Error reading file: {e}"

                # Write the file details and content to the output file
                outfile.write(f"=== File: {file_name} ===\n")
                outfile.write(f"Name: {name}\n")
                outfile.write(f"Extension: {extension}\n")
                outfile.write("Content:\n")
                outfile.write(content)
                outfile.write("\n\n")
    print(f"All files have been combined into {output_file}")

# Run the function
combine_files_to_text()
