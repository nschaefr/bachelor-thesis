if attempt > 2:
    if attempt > 3:
        logger.error("Test class still not compilable and will be deleted.")
        delete_java_file(test_path)
        return 0

    prompt_del = PROMPT_DEL.format(err, test_code)
    logger.error("Deleting tests that causing compilation error...")
    corr_class = prompt_openai(prompt_del, temperature, system_text_repair)
    if not extract_tests(corr_class):
        delete_java_file(test_path)
    update_test_file(test_path, corr_class)
    return validate_test(corr_class, test_path, temperature, attempt + 1)
