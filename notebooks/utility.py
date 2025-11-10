import os
import shutil

print("="*50)
print("📦 ARTIFACT CLEANUP UTILITY")
print("="*50)

# Define the directories that contain generated artifacts
# These paths will be deleted recursively if they exist.
DIRECTORIES_TO_CLEAN = [
    'reports/figures',
    'models/trained',
    'data/features',
    'data/processed',
    'data/raw'
]

def clean_directory(path):
    """
    Removes a directory and all its contents recursively if it exists.
    """
    # Check if the path exists to avoid errors
    if os.path.exists(path):
        try:
            # shutil.rmtree is the function for recursive directory removal
            shutil.rmtree(path)
            print(f"✅ Removed directory and contents: {path}")
        except Exception as e:
            # Provide an error message if deletion fails (e.g., permissions)
            print(f"❌ Error deleting {path}: {e}")
    else:
        print(f"⭐ Directory not found: {path} (Skipped)")

def run_cleanup():
    """
    Executes the cleanup process for all defined artifact and data directories.
    """
    print("\nStarting comprehensive artifact cleanup...")
    for dir_path in DIRECTORIES_TO_CLEAN:
        clean_directory(dir_path)
    
    print("\nCleanup complete! Your environment is fully reset for a fresh model run.")
    print("="*50)


if __name__ == "__main__":
    run_cleanup()