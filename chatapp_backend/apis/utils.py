import re
from .models import RegexRule


def check_and_redirect(prompt, provider, model):
    # Get regex rules for the model
    regex_rules = RegexRule.objects.filter(original_model=model)

    print(regex_rules)

    # Check if any regex pattern matches the prompt
    for rule in regex_rules:
        if re.search(rule.regex_pattern, prompt, re.IGNORECASE):
            # print(f"Matched: {rule}")
            return rule.redirect_model  # Return the redirected model object
        print(f"No match for rule: {rule}")

    # If no regex matches, return the original model object
    return model