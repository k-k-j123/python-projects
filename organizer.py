import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt','.docx'],
    "AUDIOS": ['.m4a','.m4b','.mp3','.wav'],
    "VIDEOS": ['.mov','.avi','.mp4','.mkv'],
    "IMAGES": ['.jpg','.jpeg','.png'],
    "COMPRESSED":['.zip','.7zip','.rar'],
    "EXEC":['.exe','.apk']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    return "MISC"


def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()