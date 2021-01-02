import os
import sys
import subprocess
import re
import shutil
import lzma
import random
from lang import message


def main(path, argv):
    with lzma.open(path+"/.core/data.dat", "r") as compressed:
        with open(path+"/.core/data.py", 'wb') as destination:
            shutil.copyfileobj(compressed, destination)
    sys.path.append(".core")
    from data import prepare_answer_sheets, compiler, standard_answer, language
    os.remove(".core/data.py")
    parse(path, argv, prepare_answer_sheets, standard_answer, compiler, language)

def parse(path, para, prepare_answer_sheets, standard_answer, compiler, language):
    if len(para) > 1:
        if para[1] == 'reset':
            user_input = input(message[language+'重置警告'])
            reset(prepare_answer_sheets()) if user_input == "Y" else None
        elif para[1] == 'check5':
            pattern = re.compile(r'/\*' + message[language+'作答区域T'] + '\*/([\s|\S|\n]+)/\*' + message[language+'作答区域B'] + '\*/')
            fail_flag = False
            for i in range(5):
                print("$$$$$$$$$$$ Test {0}/5 $$$$$$$$$$$".format(i+1))
                answer_sheets = prepare_answer_sheets()
                res = check(path, compiler, answer_sheets, standard_answer, language, pattern)
                if res == False:
                    fail_flag = True
            print(message[language+'5次验证通过']) if res else print(message[language+'5次验证失败'])
        elif para[1] == 'help':
            help(language)
        else:
            print(message[language+'无效命令'])
            help(language)
    else:
        pattern = re.compile(r'/\*' + message[language+'作答区域T'] + '\*/([\s|\S|\n]+)/\*' + message[language+'作答区域B'] + '\*/')
        check(path, compiler, prepare_answer_sheets(), standard_answer, language, pattern)

def reset(answer_sheet_files):
    for file in answer_sheet_files:
        if(os.path.exists(file)):
            os.remove(file)
        f = open(file, "w", encoding='utf-8')
        f.write(answer_sheet_files[file])
        f.close()

def get_user_answer(answer_sheet_names, language, pattern):

    answer = dict()
    for file_name in answer_sheet_names:
        file = open(file_name, "r", encoding='utf-8')
        answer_content = file.read()
        
        file.close()
        
        m = pattern.findall(answer_content, re.DOTALL)
        if m:
            answer[file_name] = m[0]
        else:
            print(message[language+'坏答卷提示'])
            return
    return answer

def get_compile_user_code(answer_sheets, language, pattern):
    answer = get_user_answer(answer_sheets, language, pattern)
    if answer is None:
        return
    return merge_answers_and_answer_sheets(answer, answer_sheets, language, pattern)

def merge_answers_and_answer_sheets(answer, answer_sheets, language, pattern):
    code_files = dict(answer_sheets)

    for key in answer:
        file = code_files[key]
        code_files[key] = pattern.sub('/*' + message[language+'作答区域T'] +'*/' + answer[key] + '/*' + message[language+'作答区域B'] + '*/', file)
    
    return code_files


def is_source_file(compiler, file_name):
    if compiler == 'g++' and file_name[-4:] == '.cpp':
        return True
    elif compiler == 'gcc' and file_name[-2:] == '.c':
        return True
    else:
        return False

def compile_run_files(path, compiler, code_files, language):
    if os.path.exists('.tmp') :
        shutil.rmtree('.tmp')
    os.mkdir('.tmp', 0o0777)
    for file_name in code_files:
        file = open('.tmp/' + file_name, 'w', encoding='utf-8')
        file.write(code_files[file_name])
        file.close()
    command_list = [compiler]

    for file_name in code_files:
        if is_source_file(compiler, file_name):
            command_list.append('.tmp/'+file_name)

    command_list.append('-o .tmp/main')
    command = ' '.join(command_list)
    p1 = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE)
    res = ''.join([line.decode(encoding="utf-8", errors="ignore") for line in p1.stdout])

    if os.path.exists('.tmp/main.exe'):
        command = path+"/.tmp/main.exe"
    elif os.path.exists('.tmp/main'):
        command = path+"/.tmp/main"
    else:
        print(message[language + '编译错误'])
        return None
    
    p1 = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE)
    res = ''.join([line.decode(encoding="utf-8", errors="ignore") for line in p1.stdout])
    p1.wait()
    shutil.rmtree('.tmp')
    return res
        

def check(path, compiler, answer_sheets, standard_answer, language, pattern):
    user_code = get_compile_user_code(answer_sheets, language, pattern)
    if user_code is None:
        return
    user_run_output = compile_run_files(path, compiler, user_code, language)
    if user_run_output is None:
        return
    standard_code = merge_answers_and_answer_sheets(standard_answer, answer_sheets, language, pattern)
    standard_run_output = compile_run_files(path, compiler, standard_code, language)
    if user_run_output == standard_run_output :
        print(message[language+'验证正确'])
        print(user_run_output)
        return True
    else:
        print(message[language+'验证错误'])
        print(user_run_output)
        print(message[language+'标准答案'])
        print(standard_run_output)
        return False
    

def help(language):
    print(message[language + '帮助'])
