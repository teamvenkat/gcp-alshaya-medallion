from pathlib import Path

REPO_ROOT = Path(__file__).parent

DIRECTORIES = [
    "config",
    "data/sample",
    "data/schemas",
    "docs",
    "src/common",
    "src/ingestion",
    "src/bronze",
    "src/silver",
    "src/gold",
    "airflow",
    "sql",
    "tests",
]

FILES = [
    "requirements.txt",
    ".gitignore",
    "LICENSE",
]


def create_directories():
    print("Creating directory structure...\n")

    for directory in DIRECTORIES:
        path = REPO_ROOT / directory
        path.mkdir(parents=True, exist_ok=True)

        gitkeep = path / ".gitkeep"
        gitkeep.touch(exist_ok=True)

        print(f"✔ {directory}")


def create_files():
    print("\nCreating project files...\n")

    for file in FILES:
        path = REPO_ROOT / file
        path.touch(exist_ok=True)
        print(f"✔ {file}")


def main():
    create_directories()
    create_files()

    print("\nRepository initialized successfully.")


if __name__ == "__main__":
    main()