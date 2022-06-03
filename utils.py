def try_parse_int(prompt):
    try:
        return int(input(prompt))
    except:
        try_parse_int(prompt)