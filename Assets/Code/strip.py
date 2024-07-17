def remove_format(test_code):
    pattern = r"```java(.*?)```"
    match = re.search(pattern, test_code, re.DOTALL)
    if match:
        return match.group(1).strip()
    return test_code.strip()
