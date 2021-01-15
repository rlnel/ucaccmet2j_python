#-----------PART 1----------------

import json 

with open('precipitation.json') as precipitation_file: 
    precipitation_data = json.load(precipitation_file)

total_per_month = [0]*12

for measurement in precipitation_data:
    if 'GHCND:US1WAKG0038' == measurement['station']: 
        seattle_rain = measurement['station'], measurement['value'], measurement['date']
        #print(seattle_rain)
        month = int(measurement['date'].split('-')[1])
        total_per_month[month - 1] += measurement['value'] #0 is jan in the list 
        
#print(total_per_month) #Jan 1693mmm
list_month = ['Jan', 'Feb', 'March', 'April', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

#making json file 
dict_total_per_month = []
for i in range(12):
    dict_total_per_month.append([{'Month': list_month[i], 'Value': total_per_month[i]}])

import json
with open('dict_total_per_month.json', 'w') as monthly_rain_seattle: 
    json.dump(dict_total_per_month, monthly_rain_seattle)

#-----------PART 2------------------

year_precipitation = sum(total_per_month)
print(year_precipitation)

monthly_relative_precipitation = []
for i in range(12): 
    monthly_relative_precipitation.append(100*total_per_month[i] / year_precipitation)
print(monthly_relative_precipitation)

result = {'Total per month': total_per_month, 'Relative total per month': monthly_relative_precipitation}

with open('result.json', 'w') as precipitation_info_per_month_seattle:
    json.dump(result, precipitation_info_per_month_seattle, indent=4)
