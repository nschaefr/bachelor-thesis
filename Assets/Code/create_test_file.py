def create_test_file(file_path, file_name, response):
    try:
        os.makedirs(os.path.join(working_dir, "src", "test"), exist_ok=True)
        test_file_dir = os.path.join(working_dir, "src", "test")
        relative_path = os.path.relpath(
            os.path.dirname(file_path), os.path.join(working_dir, "src", "main")
        )
        relative_path = relative_path.replace("..", "").lstrip(os.sep)
        target_dir = os.path.join(test_file_dir, relative_path)
        os.makedirs(target_dir, exist_ok=True)
        test_file_path = os.path.join(target_dir, file_name)
        with open(test_file_path, "w") as file:
            file.write(response)
        return test_file_path
    except Exception as e:
        logger.error(f"Error while creating test file: {e}")
        return None
