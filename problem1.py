### PROBLEM 1
filename= ''
wxdata= {'year':[]'temperature':[]} #
with open(filename, "r") as f: # 

   alist= f.read().splitlines()
for line in alist: #
   wxdata['year'].append(int(line.split()[0]))
   wxdata['temperature'].append(float(line.split()[1]))
print(wxdata)['temperature'] 

years=

print(wantyear, wxdata['temperature'][wxadata ['year'].index(wantyear)]) 

highesttemps = [i for i in wxdata ['temperature']if i >= 0.4] 
print(sorted(highesttemps)) 