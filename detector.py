import os
import hashlib
import pandas as pd
from docx import Document
from PIL import Image
import imagehash

FOLDER_PATH = "input_files"

# ------------------ HASH (Exact match) ------------------
def get_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# ------------------ TEXT EXTRACTION ------------------
def extract_text(file_path):
    ext = file_path.lower()

    try:
        if ext.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

        elif ext.endswith(".csv"):
            df = pd.read_csv(file_path)
            return df.to_string()

        elif ext.endswith(".docx"):
            doc = Document(file_path)
            return "\n".join([p.text for p in doc.paragraphs])

    except:
        return ""

    return ""


# ------------------ TEXT SIMILARITY ------------------
def text_similarity(text1, text2):
    set1 = set(text1.split())
    set2 = set(text2.split())

    if not set1 or not set2:
        return 0

    return len(set1 & set2) / len(set1 | set2)


# ------------------ IMAGE HASH ------------------
def get_image_hash(file_path):
    try:
        img = Image.open(file_path)
        return imagehash.phash(img)
    except:
        return None


# ------------------ MAIN LOGIC ------------------
def smart_deduplicate(folder):
    files = []
    
    for root, dirs, filenames in os.walk(folder):
        for f in filenames:
            files.append(os.path.join(root, f))

    seen_hashes = {}
    text_data = {}
    image_hashes = {}

    for file in files:
        print(f"Checking: {file}")

        # 1. Exact duplicate (MD5)
        file_hash = get_md5(file)

        if file_hash in seen_hashes:
            print(f" Exact duplicate deleted: {file}")
            os.remove(file)
            continue
        else:
            seen_hashes[file_hash] = file

        # 2. Text-based similarity
        text = extract_text(file)
        if text:
            for other_file, other_text in text_data.items():
                sim = text_similarity(text, other_text)

                if sim > 0.9:  # threshold
                    print(f"Similar TEXT file deleted: {file}")
                    os.remove(file)
                    break
            else:
                text_data[file] = text

        # 3. Image similarity
        img_hash = get_image_hash(file)
        if img_hash:
            for other_file, other_hash in image_hashes.items():
                if abs(img_hash - other_hash) < 5:  # similarity threshold
                    print(f"Similar IMAGE deleted: {file}")
                    os.remove(file)
                    break
            else:
                image_hashes[file] = img_hash

    print("\nSmart deduplication complete!")


if __name__ == "__main__":
    if not os.path.exists(FOLDER_PATH):
        print("input_files folder not found")
    else:
        smart_deduplicate(FOLDER_PATH)