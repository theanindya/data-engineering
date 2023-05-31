# Execute the data pipeline
python3 automated_pipeline.py

# Check if the output file(s) exist
if [ -f output_file.txt ]; then
    echo "Output file exists."
else
    echo "Output file does not exist."
fi
