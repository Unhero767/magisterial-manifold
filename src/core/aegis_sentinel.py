import ast
import sys

def verify_integrity(filename):
    try:
        with open(filename, "r") as f:
            ast.parse(f.read())
        return True
    except Exception as e:
        print(f"☣️  [METALOGICAL BURN] {filename}: {e}")
        return False

if __name__ == "__main__":
    files = sys.argv[1:]
    if not all(verify_integrity(f) for f in files):
        sys.exit(1)  # Abort the commit

