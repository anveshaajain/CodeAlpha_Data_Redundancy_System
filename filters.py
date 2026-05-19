import hashlib

def is_valid_data(content):
    cleaned_content = content.strip()
    
    if not cleaned_content:
        return False
        
    if cleaned_content.lower() in ["test", "abc", "xyz", "none", "null"]:
        return False
        
    if len(cleaned_content) < 3:
        return False
        
    return True

def generate_fingerprint(content):
    standardized = content.strip().lower()
    return hashlib.sha256(standardized.encode('utf-8')).hexdigest()