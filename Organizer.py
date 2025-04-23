import os
import shutil

def organize_downloads():
    # Define paths
    downloads_folder = os.path.expanduser("~/Downloads")
    documents_folder = os.path.expanduser("~/Documents/Organized_Data")
    
    # Define file type categories and their target folders
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".ico"],
        "Documents": [".pdf", ".doc", ".docx"],
        "Presentations": [".ppt", ".pptx", ".key", ".odp"],
        "Tables": [".csv", ".xlsx", ".xlsm"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"], 
        "3D_Files": [".stl", ".obj", ".fbx", ".blend", ".cad", ".sldprt", ".sldasm", ".gcode"],
        "Code": [".py", ".js", ".java", ".cpp", ".c", ".ipynb", ".r", ".go", ".vb", ".mlx"],
        "Text_based": [".html", ".xml", ".css", ".json", ".md", ".txt"],
        "Executables": [".exe", ".msi", ".bat", ".sh"],
        "Scripts": [".ps1", ".r", ".pl", ".cmd"],
        "Design_Files": [".psd", ".ai", ".xd", ".sketch"],
        "Database_Files": [".sql", ".db", ".sqlite"],
        "Others": []
    }
    
    # Create target folders if they don't exist
    for category in file_categories:
        category_path = os.path.join(documents_folder, category)
        os.makedirs(category_path, exist_ok=True)
    
    # Organize files
    for file_name in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, file_name)
        
        if os.path.isfile(file_path):
            # Determine the file's category
            file_extension = os.path.splitext(file_name)[1].lower()
            moved = False
            
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    target_folder = os.path.join(documents_folder, category)
                    shutil.move(file_path, os.path.join(target_folder, file_name))
                    moved = True
                    break
            
            # If no category matches, move to "Others"
            if not moved:
                others_folder = os.path.join(documents_folder, "Others")
                shutil.move(file_path, os.path.join(others_folder, file_name))

if __name__ == "__main__":
    organize_downloads()