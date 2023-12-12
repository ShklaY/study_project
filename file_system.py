import os


class FileSystem:
    @staticmethod
    def get_project_root() -> str | bytes:
        CURRENT_FILE_PATH = os.path.abspath(__file__)
        PROJECT_ROOT = os.path.dirname(CURRENT_FILE_PATH)
        return PROJECT_ROOT

    @staticmethod
    def get_absolute_path_for_file(path: str) -> str:
        return os.path.join(FileSystem.get_project_root(), path)

