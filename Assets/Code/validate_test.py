def validate_test(test_code, test_path, temperature, attempt=1):
    tests = extract_tests(test_code)
    file_name = os.path.basename(test_path)
    logger.info(f"Generated {file_name} with {len(tests)} tests.")
    success, err = run_maven_test(file_name)
    if not success:
        logger.error("TEST COMPILATION FAILED")
        handle_error(err, test_code, test_path, attempt, temperature)
