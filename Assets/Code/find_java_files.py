def find_java_files():
    java_files = []
    main_java_dir = os.path.join(working_dir, "src", "main")
    for root, dirs, files in os.walk(main_java_dir):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
    return java_files
