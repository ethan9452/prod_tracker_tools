import csv
import pprint

def get_csv(filename):
    sch = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            tmp = []
            for d in row:
                tmp.append(d.lower())
            sch.append(tmp)
        return sch

def get_task_freq_helper(cur_task, task_freq):
    if cur_task in task_freq:
        task_freq[cur_task] += 1
    else:
        task_freq[cur_task] = 1

def get_task_freq(data):
    task_freq = {}
    for row in data:
        for d in row:
            get_task_freq_helper(d, task_freq)
    return task_freq

def from_freq_get_hr(task_freq):
    hrs = {task : float(freq)/2 for task, freq in task_freq.items()}
    return hrs

def from_hr_get_dat_avg(hrs, days):
    hrs = {task : float(hr)/days for task, hr in hrs.items()}
    return hrs


if __name__ == '__main__':
    filename = 'data/weekday2week08202018.csv'
    pp = pprint.PrettyPrinter()
    data = get_csv(filename)


    days = len(data[0])

    freqs = get_task_freq(data)
    hrs = from_freq_get_hr(freqs)
    hr_avg = from_hr_get_dat_avg(hrs, days)

    hr_avg_sorted = sorted(hr_avg.items(), reverse=True, key=lambda x:x[1])

    pp.pprint(hr_avg_sorted)
