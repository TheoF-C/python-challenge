import csv


def net_profits(data_lst):
    return sum(data[1] for data in data_lst)


def average_change(data_lst):
    return (data_lst[len(data_lst) - 1][1] - data_lst[0][1]) / (len(data_lst) - 1)


def greatest_increase(data_lst):
    return max([data_lst[i][1] - data_lst[i - 1][1], data_lst[i][0]] for i in range(len(data_lst)))


def greatest_decrease(data_lst):
    return min([data_lst[i][1] - data_lst[i - 1][1], data_lst[i][0]] for i in range(len(data_lst)))


with open('budget_data.csv', mode='r') as inp:
    next(inp)
    budget_list = [[v[0], int(v[1])] for v in csv.reader(inp)]
    inp.close()

with open('budget_analysis.txt', mode='w') as out:
    out.write(f'Total Months: {len(budget_list)}\n')
    out.write(f'Total: ${net_profits(budget_list)}\n')
    out.write(f'Average Change: ${round(average_change(budget_list), 2)}\n')

    gi = greatest_increase(budget_list)
    out.write(f'Greatest Increase in Profits: {gi[1][:4]}20{gi[1][4:]} (${gi[0]})\n')

    gd = greatest_decrease(budget_list)
    out.write(f'Greatest Decrease in Profits: {gd[1][:4]}20{gd[1][4:]} (${gd[0]})')

with open('budget_analysis.txt', mode='r') as read:
    for line in read:
        line = line.strip()
        print(line)
    read.close()

