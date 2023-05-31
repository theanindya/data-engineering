# Execute the data pipeline
python automated_pipeline.py

database_file="dbanindya"

# Check if the output file(s) exist
if [ -f "$database_file" ]; then
    echo "Yes! The database file exists."
else
    echo "No database file found!"
fi
