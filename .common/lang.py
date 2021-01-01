message = dict()

message['cn作答区域T'] = '⬇︎请在此区域内作答⬇︎'
message['cn作答区域B'] = '⬆︎请在此区域内作答⬆︎'
message['cn坏答卷提示'] = '请不要删除文件中的原有注释，也不要更改答题区域之外的代码！\n可以使用命令\n python judge.py reset\n重置本题 '
message['cn编译错误'] = '编译错误！'
message['cn验证正确'] = '✓✓✓✓✓✓结果验证正确！✓✓✓✓✓✓\n输出：'
message['cn验证错误'] = '✗✗✗✗✗✗结果验证错误！✗✗✗✗✗✗\n\t你的输出：'
message['cn标准答案'] ='\t标准答案：'
message['cn5次验证通过'] = '\n ^_^  通过!'
message['cn5次验证失败'] = '\n T_T  失败!'
message['en重置警告'] = '本题所有源文件将被删除\n请确认已做好备份\n输入Y继续：'
message['cn无效命令'] = '命令参数无效'
message['cn帮助'] = '''
无参数运行此python脚本以判定程序输出是否正确
或使用以下命令参数:
reset\t\t重置题目
check5\t\t连续运行五次判定
help\t\t打印此帮助信息
'''

message['en作答区域T'] = '⬇︎Please answer within this area⬇︎'
message['en作答区域B'] = '⬆︎Please answer within this area⬆︎'
message['en坏答卷提示'] = "Please don't remove the comments in the file. And please type your answer within the answer area.\nYou can use the command\n python judge.py reset\nto reset this question."
message['en编译错误'] = 'Compiling error!'
message['en验证正确'] = '✓✓✓✓✓✓ Correct! ✓✓✓✓✓✓\nOutput:'
message['en验证错误'] = '✗✗✗✗✗✗ Wrong! ✗✗✗✗✗✗\n\tOutput from your code:'
message['en标准答案'] ='\tStandard output:'
message['en5次验证通过'] = '\n ^_^  Passed!'
message['en5次验证失败'] = '\n T_T  Failed!'
message['en重置警告'] = 'The current souce files will be deleted.\nMake sure you have saved everything elsewhere.\nEnter Y to continue:'
message['en无效命令'] = 'Parameter not available!'
message['en帮助'] = '''
Run this script to judge your code according to the standard.
Or you can use the following parameter
reset\t\tReset the question
check5\t\tRun the test for five times
help\t\tPrint this help message
'''