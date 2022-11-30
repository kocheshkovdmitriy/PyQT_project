import shlex
import subprocess

def run(code:str, data: str):
    with open('test.txt', 'w', encoding='UTF-8') as in_data:
        in_data.write(data)
    command = f'python -c "{code}"'
    command = shlex.split(command)
    process = subprocess.Popen(
        command,
        stdin=open('test.txt', 'r', encoding='UTF-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    outs, errs = process.communicate(timeout=1)
    return outs, errs

def testing(code: str, tests: str):
    tests = tests.split('@$@')
    data_tests = {index + 1: test.split('@_@') for index, test in enumerate(tests)}
    print(data_tests)
    result = ''
    flag_done = True
    for num_test in data_tests.keys():
        result += f'Тест{num_test}: '
        outs, errs = run(code, data_tests[num_test][0])
        if outs.decode().strip() == data_tests[num_test][1]:
            result += 'Ok\n'
        else:
            flag_done = False
            result += 'No\n'
            if errs:
                result += f'{errs.decode()}\n'
            else:
                result += f'Входные данные: {data_tests[num_test][0]}\n' \
                          f'Ожидаемый результат: {data_tests[num_test][1]}\n' \
                          f'Вывод: {outs.decode()}\n'
    print(result)
    return result, flag_done



