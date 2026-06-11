import random
import string
from pathlib import Path

def create_random_files(directory_name: str = "random_files") -> None:
    dir_path = Path(directory_name)
    dir_path.mkdir(exist_ok=True)
    
    chars = string.ascii_lowercase + string.digits
    
    for _ in range(10):
        filename = "".join(random.choices(chars, k=8)) + ".txt"
        file_path = dir_path / filename
        file_path.touch()
        print(file_path.resolve())

create_random_files()