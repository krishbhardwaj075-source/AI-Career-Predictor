def extract(text):
   skills = [

# Programming Languages
"python","java","c","c++","c#","javascript","typescript","go","rust","kotlin","swift",
"php","ruby","scala","r","matlab","perl","dart","objective-c",

# Web Development
"html","css","sass","bootstrap","tailwind","jquery",
"react","angular","vue","nextjs","nuxtjs",
"node","nodejs","express","django","flask","spring","laravel",

# AI / Machine Learning / Data Science
"machine learning","deep learning","artificial intelligence","data science",
"nlp","computer vision","opencv","tensorflow","keras","pytorch",
"scikit-learn","pandas","numpy","matplotlib","seaborn",
"xgboost","lightgbm","catboost","data analysis",

# Databases
"mysql","postgresql","mongodb","sqlite","oracle","mariadb",
"redis","cassandra","firebase","dynamodb","neo4j","elasticsearch",

# Big Data
"hadoop","spark","pyspark","hive","pig","kafka","flink",

# Cloud Computing
"aws","amazon web services","azure","google cloud","gcp",
"cloud computing","serverless","lambda",

# DevOps
"docker","kubernetes","jenkins","git","github","gitlab",
"ci/cd","terraform","ansible","vagrant","devops",

# Mobile Development
"android","ios","react native","flutter","xamarin","swiftui",

# Cybersecurity
"ethical hacking","penetration testing","cyber security",
"network security","cryptography","kali linux",

# Networking
"tcp/ip","dns","dhcp","http","https","ftp","smtp","networking",

# Operating Systems
"linux","unix","windows","ubuntu","centos","redhat",

# Software Tools
"visual studio","vscode","intellij","eclipse","postman",
"jira","notion","figma","tableau","power bi"
]
   text=text.lower()
   detect=[]
   for skill in skills:
      if skill in text:
         detect.append(skill)
   return detect