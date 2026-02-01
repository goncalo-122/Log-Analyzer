import os
import json

INPUT_DIR = "Input"
OUTPUT_DIR = "Output"

def process_logs(logs):
    # Initialize summary structure
    summary = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "last_error": None
    }
    # Count log levels and track last error
    for log in logs:
        level = log.get("level")

        if level in summary:
            summary[level] += 1

        if level == "ERROR":
            summary["last_error"] = {
                "timestamp": log.get("timestamp"),
                "message": log.get("message")
            }

    return summary


def main():
   # Ensure output folder exists (if it doesn't exist, it will create it automatically)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

   # Save all JSON filenames in the input folder as json_files
    json_files_names = [f for f in os.listdir(INPUT_DIR) if f.endswith(".json")]
    
    #Stop if no files found
    if not json_files_names:
        print("No JSON files were found in the input folder.")
        return
    #Iterates through all the filenames present in json_files
    for filename in json_files_names:
        input_path = os.path.join(INPUT_DIR, filename)

        # Read file
        with open(input_path, "r") as file:
            logs = json.load(file)

        # Transform logs from input files to output files
        summary = process_logs(logs)

        # Create output filename
        output_filename = f"processed_{filename}"
         # Create output filepath
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        # Create output file    
        with open(output_path, "w") as file:
            #Put the formatation of process_log into a file with 4 indentation spaces
            json.dump(summary, file, indent=4)

        print(f"Processed: {filename} → {output_filename}")


if __name__ == "__main__":
    main()
