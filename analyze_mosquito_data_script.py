import sys
import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib


filename = sys.argv[1]

print "analyzing", filename

#read the data
data=pd.read_csv(filename)

data['temperature']=mosquito_lib.fahr_to_celsius(data['temperature'])

print "Running Analyze"

parameters=mosquito_lib.analyze(data, filename.replace("csv","png"))

#writes parameters to file
print "Saving parameters"
parameters.to_csv(filename.replace("data","parameters"))


