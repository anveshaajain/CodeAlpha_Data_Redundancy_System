import streamlit as st
from database import init_database, check_duplicate, save_data
from filters import is_valid_data, generate_fingerprint

# Initialize the database when the web app loads
init_database()

# Set up the title and description on the web page
st.title("🛡️ Data Redundancy & Leak Prevention System")
st.write("Enter data below to run it through the validation and deduplication layers.")

# Create a text input box for the user
user_input = st.text_input("Enter New Data Entry:", placeholder="Type something here...")

# Create a submit button
if st.button("Process Entry"):
    if user_input:
        # 1. Validation Check (False Positives)
        if not is_valid_data(user_input):
            st.error(f"❌ Rejected: '{user_input}' is flagged as a False Positive (invalid/garbage data).")
            
        else:
            # 2. Generate Hash Fingerprint
            fingerprint = generate_fingerprint(user_input)
            
            # 3. Check for Duplicates in Database
            if check_duplicate(fingerprint):
                st.warning(f"⚠️ Rejected: '{user_input.strip()}' already exists in the database (Redundant).")
            else:
                # 4. Save to Database
                save_data(user_input.strip(), fingerprint)
                st.success(f"✅ Success: '{user_input.strip()}' is unique and has been safely stored!")
    else:
        st.info("Please type something in the box first.")