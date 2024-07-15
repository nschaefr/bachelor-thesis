questions = [
    inquirer.List(
        "prompt",
        message="Select the type of prompt to use",
        choices=["ZERO_SHOT", "ONE_SHOT"],
    ),
    inquirer.List(
        "temperature",
        message="Select the temperature to use",
        choices=[0, 0.25, 0.5],
    ),
]

answers = inquirer.prompt(questions)
prompt_type = answers["prompt"]
temperature = answers["temperature"]
