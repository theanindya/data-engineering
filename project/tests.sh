# Execute the data pipeline
python3 automated_pipeline.py

database_file="dbanindya"

# Check if the output file(s) exist
if [ -f database_file ]; then
    echo "Ya! Its there!!"
else
    echo "No database file!"
fi
