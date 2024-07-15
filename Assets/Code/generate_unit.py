def generate_unit_tests(prompt_type, temperature):
    java_files = find_java_files()
    config = TestConfiguration()
    config.temperature = temperature
    config.prompt_type = prompt_type

    if java_files:
        for java_file in java_files:
            java_class = read_java_file(java_file)
            generate_test_code(java_file, java_class, config)
    else:
        logger.warning("No java files found.")
