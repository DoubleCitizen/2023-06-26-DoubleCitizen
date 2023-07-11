from classes.reader_json import ReaderJSON
from classes.reader_txt import ReaderTxt
from datetime import datetime

path_txt_file = 'results_RUN.txt'
path_json_file = 'competitors2.json'

reader_txt = ReaderTxt(path_txt_file)
lines_txt = reader_txt.read_all(encod='utf-8-sig')

reader_json = ReaderJSON(path_json_file)
competitors_dict = reader_json.read_all(encod='utf-8-sig')

results_run = {}
for line in lines_txt:
    line_split = line.split()
    key = line_split[0]
    values = {line_split[1], line_split[2]}
    if key in results_run.keys():
        results_run[line_split[0]].update({line_split[1]: line_split[2]})
    else:
        results_run[line_split[0]] = {line_split[1]: line_split[2]}

for key, value in competitors_dict.items():
    if key in results_run.keys():
        results_run[key].update(value)

for key, value in results_run.items():
    start_time = datetime.strptime(value['start'], '%H:%M:%S,%f')
    finish_time = datetime.strptime(value['finish'], '%H:%M:%S,%f')
    race_time = finish_time - start_time
    race_time_sec = float(race_time.seconds)
    race_time = str(race_time)
    race_time = race_time[2:race_time.find('.') + 3]
    race_time = race_time.replace('.', ',')
    results_run[key].update({'race_time': race_time, 'race_time_sec': race_time_sec})

sorted_results_run = dict(sorted(results_run.items(), key=lambda kv: kv[1]['race_time_sec'], reverse=False))

i = 0
print('1. Результат')
print('Занятое место\t\tНагрудный номер\t\t\tИмя\t\tФамилия\t\tРезультат')
for key, value in sorted_results_run.items():
    i += 1
    print(f'{i}\t\t{key}\t\t{value["Name"]}\t\t\t{value["Surname"]}\t\t{value["race_time"]}')
