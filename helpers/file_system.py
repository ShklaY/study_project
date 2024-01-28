from pathlib import Path


class FileSystem:
    @staticmethod
    def get_project_root() -> Path:
        return Path(__file__).parent.parent

    @staticmethod
    def make_dir(*path: str) -> Path:
        # create directory if not exists
        directory_path = FileSystem.get_project_root().joinpath(*path)
        if not directory_path.is_dir():
            directory_path.mkdir()
        return directory_path

