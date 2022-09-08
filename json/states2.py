
import json

india ={
            "name":"rajsthan",
            "code":"47",
            "language":["115","457","117"],
            "population":"18415"
        }

#dumps example this only convert data in to string
# with open('states2.json','w')as f:
    # resultJSON = json.dumps(india)
    # print(resultJSON)


#dump example this make a new file 
with open('states2.json','w')as f:
    json.dump(india,f,indent=2)

