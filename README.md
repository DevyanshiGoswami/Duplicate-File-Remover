Duplicate File Remover
# Duplicate File Remover

## Overview

Duplicate File Remover is a Python-based utility that detects and removes duplicate files from a directory. The system identifies duplicate files using hashing techniques and supports multiple file formats, helping users optimize storage usage and improve file management.

## Features

* Detects duplicate files automatically
* Supports multiple file formats (TXT, CSV, DOCX, Images, etc.)
* Uses MD5/SHA-based hashing for accurate file comparison
* Detects both exact and similar duplicates
* Safe deletion by moving files to a trash folder
* Multithreaded processing for improved performance
* Generates logs and storage-saving statistics

## Technologies Used

* Python
* hashlib
* os
* pandas
* python-docx
* Pillow
* imagehash
* concurrent.futures
* tqdm

## How It Works

1. Scan all files in the selected directory.
2. Group files based on size.
3. Generate a hash for each file.
4. Compare hash values to identify duplicates.
5. Apply content-based similarity checks for text files and images.
6. Move duplicate files to a trash folder or remove them safely.

## Installation

```bash
pip install pandas python-docx pillow imagehash tqdm
```

## Usage

```bash
python dedupe.py --folder input_files
```

To perform actual deletion:

```bash
python dedupe.py --folder input_files --delete
```

## Results

The system successfully identifies duplicate files across multiple formats and reduces storage redundancy. Performance is improved through size-based filtering and multithreading, while safe deletion mechanisms help prevent accidental data loss.

## Future Enhancements

* Database-backed hash storage
* Incremental scanning
* REST API integration
* Cloud storage support
* Distributed duplicate detection  
<img width="532" height="309" alt="figure3" src="https://github.com/user-attachments/assets/13af6335-ff45-4eed-8271-f45bc21af117" />\
Image of duplicate files.  
<img width="525" height="185" alt="figure4" src="https://github.com/user-attachments/assets/bfbfbb1d-618c-4f66-a906-63ddae4518b1" />\  
After we run the code all Duplicates Files are removed.
