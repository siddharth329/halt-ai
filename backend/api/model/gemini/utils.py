def fine_tuning_prompt_generator(user_query, rules):
    rules = f"""
    {rules}
    """

    prompt = f"""
    I am using this model in a machine which defines whether a person is revealing any information to the other person in their chat.
    I will provide you with some rules and the text of the chat to check whether the chat is within the organizations policy boundations.
    The chat of the user here is with any large language model available in the market.
    Note: if the information contains dummy parameters enclosed in <> then allow the request as the real data is replaced with placeholder.

    Output format should be a json object and should have three parameters.
    First parameter is 'flag' which is 0 if request is safe and within bounds of the rules otherwise is 1
    Second parameter is an 'errors' which is blank if request is safe and if the request is not safe then it is the reason for blocking the request.
    Third parameter should be 'critical' which is 1 if the query shows some data leak of the organization otherwise it should be 0.  
    Strictly Do no include markdowns for json at start and end
    Remember the two parameters should be named as flag and errors respectively

    Rules:
    {rules}

    Text to check:
    {user_query}
    """
    return prompt


def rules_extraction_prompt_generator(text):
    prompt = f"""
    I am giving you the contents of a policy file of an organization as it is.
    You will now have to extract the rules from it and create pointers for it which should be easily understood by you.
    Remember to not miss out on any of the critical rules.
    Extract each rule very briefly so that there is no confusion when reading them.   
    
    File Contents:
    {text}
    """
    return prompt


def fine_tuning_content_prompt_generator(text, fine_tuning_prompt):
    prompt = f"""
    I am providing you with some rules and with a text to modify the given rules accordingly
    
    Rules:
    {text}
    
    Fine Tuning Prompt:
    {fine_tuning_prompt}
    """
    return prompt
