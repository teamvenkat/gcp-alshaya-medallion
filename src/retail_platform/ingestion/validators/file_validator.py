from pathlib import Path


class FileValidator:
    """
    Performs validation checks on source files before ingestion.
    """

    @staticmethod
    def validate(file_path: Path) -> None:
        """
        Validate the source file.

        Raises:
            FileNotFoundError
            ValueError
        """

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if not file_path.is_file():
            raise ValueError(f"Not a file: {file_path}")

        if file_path.suffix.lower() != ".csv":
            raise ValueError(f"Unsupported file type: {file_path.name}")

        if file_path.stat().st_size == 0:
            raise ValueError(f"File is empty: {file_path.name}")