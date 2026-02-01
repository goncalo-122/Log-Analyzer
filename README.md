# Log Analyzer

A simple tool for analyzing log files in JSON format.  
It automatically reads all `.json` files inside the **Input** folder, processes them, and generates a summary for each file in the **Output** folder.

## Features
- Counts log entries by level (INFO, WARNING, ERROR)
- Identifies the last error found in the file
- Generates a structured summary in JSON format
- Automatically processes multiple input files
- Easy to adapt to other log formats

## How to use
1. Place one or more `.json` log files inside the **Input** folder  
2. Run the script:  
