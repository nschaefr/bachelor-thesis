result = subprocess.run(
    [
        "mvn",
        "--quiet",
        "-Dtest=" + file_name,
        "-Dmaven.test.failure.ignore=true",
        "test",
    ],
    capture_output=True,
    text=True,
)
if result.returncode == 0:
    logger.info("TEST COMPILATION SUCCESSFUL")
    return True, None
else:
    err = result.stdout.strip()
    return False, err
