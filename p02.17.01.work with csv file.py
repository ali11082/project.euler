#نمرات افراد را از یک فایل
#csv
#بخواند و
# معدل هر فرد را محاسبه کند و همراه با نام وی ذخیره کند(ترتیب خروجی=ورودی)

import csv
from statistics import mean
#برای گرفتن میانگین استفاده می شود
from collections import OrderedDict
#کتابخانه اخر به دلیل حفظ ترتیب است

def calculate_averages(input_file_name, output_file_name):
    averages = OrderedDict()
    with open(input_file_name,"r") as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append (float(row[i]))
            avg = mean(scores)
            averages [row[0]] = avg
  #  print(avg)               
    with open (output_file_name, 'w') as out:
        count = 0
        for person in averages:
            count += 1
            if count == 1:
                out.write(person+ ","+ str(averages[person]))
            else:
                out.write("\n"+ person+ ","+ str(averages[person]))
            
# معدل ها را به ترتیب صعودی همراه با نام هر فرد ذخیره کند

def calculate_sorted_averages(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name,"r") as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append (float(row[i]))
            avg = mean(scores)
            averages [row[0]] = avg

    averages_ord = OrderedDict (sorted (averages.items(), key=lambda x:(x[1], x[0])))

    with open (output_file_name, 'w') as out:
        count = 0
        for person in averages_ord:
            count += 1
            if count == 1:
                out.write(person+ ","+ str(averages_ord[person]))
            else:
                out.write("\n"+ person+ ","+ str(averages_ord[person]))    
        
# سه معدل برتر را با نام هر فرد ذخیره کند

def calculate_three_best(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name,"r") as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append (float(row[i]))
            avg = mean(scores)
            averages [row[0]] = avg

    averages_ord = OrderedDict (sorted (averages.items(), key=lambda x:(-x[1], x[0])))
    
    with open (output_file_name, 'w') as out:
        best = []
        for i in range (3):
            best_avg = averages_ord.popitem (last=False)
            best.append (best_avg)

        out.write (best[0][0]+","+str(best[0][1])+"\n")
        out.write (best[1][0]+","+str(best[1][1])+"\n")
        out.write (best[2][0]+","+str(best[2][1]))

# سه معدل پایین را بدون نام ذخیره کند


def calculate_three_worst(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name,"r") as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append (float(row[i]))
            avg = mean(scores)
            averages [row[0]] = avg

    averages_ord = OrderedDict (sorted (averages.items(), key=lambda x:(x[1], x[0])))
    
    with open (output_file_name, 'w') as out:
        worst = []
        for i in range (3):
            worst_avg = averages_ord.popitem (last=False)
            worst.append (worst_avg)
            
        out.write (str(worst[0][1])+"\n")
        out.write (str(worst[1][1])+"\n")
        out.write (str(worst[2][1]))

# میانگین معدل ها را محاسبه کند


def calculate_average_of_averages(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name,"r") as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        for row in csvfile:
            scores = []
            for i in range(1, len(row)):
                scores.append (float(row[i]))
            avg = mean(scores)
            averages [row[0]] = avg

    averages_ord = OrderedDict (sorted (averages.items(), key=lambda x:(x[1], x[0])))

    SUM = 0
    count = 0
    for average in averages_ord:
        count += 1
        SUM += float(averages_ord[average])

    avg_avg = SUM/count
    with open (output_file_name, 'w') as out:
        out.write(str(avg_avg))



a=calculate_averages("p02.17.02.scores.csv","p02.17.03.scores.csv")
b=calculate_sorted_averages("p02.17.02.scores.csv","p02.17.04.scores.csv")
c=calculate_three_best("p02.17.02.scores.csv","p02.17.05.scores.csv")
d=calculate_three_worst("p02.17.02.scores.csv","p02.17.06.scores.csv")
e=calculate_average_of_averages("p02.17.02.scores.csv","p02.17.07.scores.csv")

print(a,b,c,d,e) 