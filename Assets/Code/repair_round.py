logger.info(f"REPAIR ROUND {attempt}/2")
prompt_error = PROMPT_REPAIR.format(err, test_code)
corr_class = prompt_openai(prompt_error, temperature, system_text_repair)

update_test_file(test_path, corr_class)
return validate_test(corr_class, test_path, temperature, attempt + 1)
