import csv
reader = csv.DictReader(open('source_files/IT_motives_2013.csv'))

result = {}
keys = ['Total', 'Greed/ Money', 'Revenge /Settling scores', 'Others', 'Cause Disrepute', 'Prank/ Satisfaction of Gaining Control ', 'Eve teasing/ Harassment', 'Extortion', 'Fraud/ Illegal Gain']
for key in keys:
    result[key] = {}
for row in reader:
    for key in keys:
        result[key][row.get('State/UTs')] = row.get(key)

for motive, motive_dict in result.iteritems():
    print "{motive},{count}".format(motive=motive, count=motive_dict.get('Total (All India)'))
