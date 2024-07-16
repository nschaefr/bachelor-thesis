package_pattern = r"package\s+([a-zA-Z0-9_.]+);"
imports_pattern = r"import\s+([a-zA-Z0-9_.]+);"
class_name_pattern = r"\b(class|interface)\s+([a-zA-Z_$][a-zA-Z\d_$]*)"
method_pattern = (
    r"(public|private|protected|static|final|synchronized|abstract|native|strictfp|transient|volatile|\w+)"
    r"\s+[\w<>,\s]+\s+"
    r"[a-zA-Z_]\w*"
    r"\s*\([^)]*\)"
    r"\s*(?:throws\s+[a-zA-Z0-9_,\s]+)?"
    r"\s*\{"
)
constructor_pattern = (
    r"public\s+" + re.escape(class_name) + r"\s*\(([^)]*)\)\s*\{" r"(.*?)}"
)
