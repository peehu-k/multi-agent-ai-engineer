
import os
import shutil
from pathlib import Path

def organize_files(source_directory, target_directory):
    source = Path(source_directory)
    if not source.is_dir():
        raise FileNotFoundError(f"Source directory {source} does not exist.")
    
    for item in os.listdir(source):
        s = Path(source) / item
        
        # Check file extension and move accordingly within target directories
        if item.endswith('.py'):  # Python files
            dest_path = Path(target_directory) / 'python' / item.stem
            os.makedirs(dest_path.parent, exist_ok=True)
            shutil.move(str(s), str(Path(destin_path)))
        elif item.endswith('.txt'):  # Text files for documentation/comments or READMES
            dest_path = Path(targetterm_directory) / 'text' / (item + '.md')
            os.makedirs(dest_path.parent, exist_ok=True)
            shutil.move(str(s), str(Path(destination_dir)))
        else:  # Default case for other file types or unrecognized extensions
            dest_path = Path(targetdirectory) / 'other' / item
            os.makedirs(dest_path.parent, exist_ok=True)
            shutil.move(str(s), str(Path(destination_dir)))
