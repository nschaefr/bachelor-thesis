prompt = prompt_templates[config.prompt_type].format(
    method_name,
    package,
    ", ".join(imports),
    class_name,
    constructor,
    method,
    test_class_name,
)
