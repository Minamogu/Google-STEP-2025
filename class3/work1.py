#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def read_times(line, index):
    token = {'type': 'TIMES'}
    return token, index + 1

def read_divided(line, index):
    token = {'type': 'DIVIDED'}
    return token, index + 1 


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_times(line, index)
        elif line[index] == '/':
            (token, index) = read_divided(line, index)            
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def evaluate_timesdivided(tokens):
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'TIMES':
            if tokens[index - 1]['type'] == 'NUMBER':
                times_number = tokens[index + 1]['number']
                tokens.pop(index + 1)
                tokens.pop(index)
                tokens[index - 1]['number'] *= times_number
            else:
                print('Invalid syntax')  # 符号の前が数字ではない場合
                exit(1)
        elif tokens[index]['type'] == 'DIVIDED':
            if tokens[index - 1]['type'] == 'NUMBER':
                if tokens[index + 1]['number'] == 0:  # 0で割ろうとしたとき
                    print('Division by zero')
                    exit(1)
                divided_number = tokens[index + 1]['number']
                tokens.pop(index + 1)
                tokens.pop(index)
                tokens[index - 1]['number'] /= divided_number
            else:
                print('Invalid syntax')   
                exit(1)
        index += 1
    return tokens

def evaluate_plusminus(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer

def evaluate(tokens): 
    tokens = evaluate_timesdivided(tokens)

    if len(tokens) == 1:  # 積と商のみの計算だった場合
        return tokens[0]['number']
    answer = evaluate_plusminus(tokens)
    return answer


def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("10/2")
    test("0*2")
    test("0/0")
    test("")
    test("aaa+2")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
