# 🗂️ Auto File Classifier

This Python script automatically classifies and moves files (e.g., PDFs, Word documents, etc.) from your Downloads folder to specific folders (e.g., `PDFs`, `Words`) on your desktop. It also renames files based on their last modified date.

---

## 📌 Description

The `Auto File Classifier` project was designed to keep your Downloads folder clean and organized. It scans files, determines their type, renames them using their last modification date, and moves them to predefined directories.

Example:
```
From: C:\Users\Username\Downloads\document.pdf  
To:   C:\Users\Username\Desktop\PDFs\2025-06-01_document.pdf
```

---

## ⚙️ Features

- Detects and organizes PDF and Word documents.
- Renames files using their last modified date.
- Moves files to user-defined folders.
- Easy to configure and extend to other file types.

---

## ✅ Prerequisites

Before running the script, make sure you have:

- Python 3.8 or higher installed
- Basic understanding of file paths
- [Git](https://git-scm.com/) for version control (optional)

---

## 🚀 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aduraan03/auto_file_classify.git
   cd auto_file_classify
   ```

2. **Edit the paths** in `automatizacion_archivos.py` and `folders_archivos.py`:
   - Replace `download_folder`, `pdf_folder`, and `word_folder` with your actual paths.

3. **Run the script**
   ```bash
   python automatizacion_archivos.py
   ```

---

## 🧰 Tools & Technologies

- **Python** – scripting language used
- **shutil** – for file operations
- **os** – for directory and file handling
- **datetime** – to rename files by date

---

## 📂 Project Structure

```
auto_file_classify/
│
├── automatizacion_archivos.py     # Main script for processing files
├── folders_archivos.py            # File and folder configuration
├── README.md                      # Project documentation
└── .gitignore                     # Git ignore rules
```

---

## 📌 To Do / Ideas for Improvement

- Add GUI interface for easier configuration
- Support classification by extension, size or content
- Logging with timestamps
- Unit tests and error handling improvements

---

## 👤 Author

**Alejandro Duran**  
Mechatronics Engineer | Systems Analyst | QA Engineer  
📧 adhm_03@hotmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/alejandro-duran-de-huerta)  
🔗 [GitHub](https://github.com/Aduraan03)

---

## 📄 License

This project is licensed under the MIT License.
