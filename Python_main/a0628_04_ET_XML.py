import xml.etree.ElementTree as et
rq = et.ElementTree(file="./data/jobs.xml")
data = rq.getroot()
print(data.tag)


for i in data.findall("Job"):
    if i.find("job_Kind_Name").text != "無":
        print(i.find("job_Kind_Name").text)
    print(i.find("dept_name").text)
    
    
