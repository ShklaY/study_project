from pathlib import Path


class FileSystem:
    @staticmethod
    def get_project_root() -> Path:
        return Path(__file__).parent.parent

    @staticmethod
    def get_absolute_path_for_file(*path_parts: str) -> str:
        return FileSystem.get_project_root().joinpath(*path_parts).__str__()

