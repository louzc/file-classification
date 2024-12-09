# -*- coding: utf-8 -*-
"""
This script organizes files in a given directory based on their extensions.
Files are moved into categorized folders such as Music, Video, Compressed, etc.
"""
# @Author  : Louzhichen

import os
import shutil
import msvcrt

# File extensions grouped by category
AUDIO = ['.mp3', '.wma', '.flac']
VIDEO = ['.mp4', '.avi', '.mov', '.mpeg', '.ts', '.flv', '.m4v', '.mkv', '.m3u8']
COMPRESSED = ['.7z', '.zip', '.rar', '.cab', '.jar', '.lzh']
PHOTO = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif']
PROGRAM = ['.exe', '.com', '.bat', '.msi']
DOCUMENTS = ['.doc', '.docx', '.xls', '.xlsx', '.csv', '.ppt', '.pptx', '.pdf', '.txt']
WEB = ['.html', '.htm']
PYTHON_FILE = ['.py']
TORRENT = ['.torrent']
ISO_FILE = ['.iso']
EBOOK = ['.epub', '.mobi']
ANDROID_FILE = ['.apk']

# Mapping file extensions to folder names
FILE_EXTENSIONS = [
    AUDIO, VIDEO, COMPRESSED, PHOTO, PROGRAM, DOCUMENTS, WEB,
    PYTHON_FILE, TORRENT, ISO_FILE, EBOOK, ANDROID_FILE
]
FOLDER_NAMES = [
    "Music", "Video", "Compressed", "Photo", "Program", "Document", "Web",
    "Python", "Torrent", "ISO", "Book", "Android"
]

def move_file(src_path, dest_folder):
    """
    Moves a file to a destination folder. Creates the folder if it doesn't exist.
    
    Args:
        src_path (str): The full path of the file to be moved.
        dest_folder (str): The destination folder.
    """
    dest_path = os.path.join(dest_folder, os.path.basename(src_path))
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    try:
        shutil.move(src_path, dest_path)
        print(f"Successfully moved: {src_path} -> {dest_path}")
    except FileNotFoundError:
        print(f"File not found: {src_path}")
    except PermissionError:
        print(f"Permission denied for: {src_path}")
    except Exception as e:
        print(f"Failed to move {src_path}: {e}")

def organize_files(base_path):
    """
    Organizes files in the given directory into categorized folders.

    Args:
        base_path (str): The directory to organize.
    """
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isfile(item_path):
            ext_name = os.path.splitext(item_path)[-1].lower()
            for extensions, folder_name in zip(FILE_EXTENSIONS, FOLDER_NAMES):
                if ext_name in extensions:
                    dest_folder = os.path.join(base_path, folder_name)
                    move_file(item_path, dest_folder)
                    break  # Stop checking after finding the category
    print("File organization completed.")

if __name__ == "__main__":
    input_path = input("Enter the path to organize files: ").strip()
    if os.path.isdir(input_path):
        organize_files(input_path)
    else:
        print("Invalid path. Please enter a valid directory.")

    print("Press any key to exit.")
    ord(msvcrt.getch())
