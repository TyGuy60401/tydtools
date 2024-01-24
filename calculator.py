def calculator(round_num: int = 8):
    prompt = '>> '
    response = input(prompt)
    while 'exit' != response:
        try:
            result = eval(response, globals(), locals())
        except Exception as e:
            print(e)
            response = input(prompt)
            continue
        if isinstance(result, (float, int)):
            print(round(result, round_num))
        else:
            print(eval(response))
        response = input(prompt)
