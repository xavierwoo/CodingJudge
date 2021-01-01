import os
import sys
import re
import shutil
import lzma
from lang import message


def main(path, argv):
    with lzma.open(path+"/.core/data.dat", "r") as compressed:
        with open(path+"/.core/data.py", 'wb') as destination:
            shutil.copyfileobj(compressed, destination)
    sys.path.append(".core")
    from data import prepare_answer_sheets, compiler, standard_answer, language
    os.remove(".core/data.py")
    parse(argv, prepare_answer_sheets, standard_answer, compiler, language)

def parse(para, prepare_answer_sheets, standard_answer, compiler, language):
    if len(para) > 1:
        if para[1] == 'reset':
            reset(prepare_answer_sheets())
        elif para[1] == 'check5':
            pattern = re.compile(r'/\*' + message[language+'作答区域T'] + '\*/([\s|\S|\n]+)/\*' + message[language+'作答区域B'] + '\*/')
            fail_flag = False;
            for i in range(5):
                print("$$$$$$$$$$$ Test {0}/5 $$$$$$$$$$$".format(i+1))
                res = check(compiler, prepare_answer_sheets(), standard_answer, language, pattern)
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
        check(compiler, prepare_answer_sheets(), standard_answer, language, pattern)

def reset(answer_sheet_files):
    for file in answer_sheet_files:
        if(os.path.exists(file)):
            os.remove(file)
        f = open(file, "w")
        f.write(answer_sheet_files[file])
        f.close()

def get_user_answer(answer_sheet_names, language, pattern):

    answer = dict()
    for file_name in answer_sheet_names:
        file = open(file_name, "r")
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

def compile_run_files(compiler, code_files, language):
    if os.path.exists('.tmp') :
        shutil.rmtree('.tmp')
    os.mkdir('.tmp', 0o0777)
    for file_name in code_files:
        file = open('.tmp/' + file_name, 'w')
        file.write(code_files[file_name])
        file.close()
    command_list = [compiler]

    for file_name in code_files:
        if is_source_file(compiler, file_name):
            command_list.append('.tmp/'+file_name)

    command_list.append('-o .tmp/main')
    command = ' '.join(command_list)
    res = os.popen(command).read()
    os.wait()
    if not os.path.exists('.tmp/main'):
        print(message[language + '编译错误'])
        return None
    else:
        command = ".tmp/main"
        res = os.popen(command).read()
        os.wait()
        shutil.rmtree('.tmp')
        return res
        

def check(compiler, answer_sheets, standard_answer, language, pattern):
    user_code = get_compile_user_code(answer_sheets, language, pattern)
    if user_code is None:
        return
    user_run_output = compile_run_files(compiler, user_code, language)
    if user_run_output is None:
        return
    standard_code = merge_answers_and_answer_sheets(standard_answer, answer_sheets, language, pattern)
    standard_run_output = compile_run_files(compiler, standard_code, language)
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
