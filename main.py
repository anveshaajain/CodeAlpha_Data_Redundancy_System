# Import functions from our other files
from database import init_database, check_duplicate, save_data
from filters import is_valid_data, generate_fingerprint

def process_new_entry(content):
    # 1. Check for false positives / garbage
    if not is_valid_data(content):
        print(f"❌ Rejected: '{content}' is flagged as a False Positive.")
        return
        
    # 2. Generate unique hash
    fingerprint = generate_fingerprint(content)
    
    # 3. Check database file for redundancy
    if check_duplicate(fingerprint):
        print(f"⚠️  Rejected: '{content.strip()}' is a duplicate entry.")
    else:
        # 4. Save unique data
        save_data(content.strip(), fingerprint)
        print(f"✅ Success: '{content.strip()}' has been saved.")

# Test execution
if __name__ == "__main__":
    init_database()
    print("--- Multi-File System Ready --- \n")
    
    incoming_batch = [
        "Cloud Computing Lecture Notes",
        "test",
        "Cloud Computing Lecture Notes",
        "Computer Networks Assignment",
        "computer networks assignment"
    ]
    
    for data_item in incoming_batch:
        process_new_entry(data_item)