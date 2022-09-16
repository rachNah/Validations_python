import os 
      
# Get the current working  
cwd = os.getcwd()    
print("Current working directory:", cwd)

# Get the process id of execution
prid = os.getpid()
print(" process id of execution:", prid)

# creating dir
# Directory 
dir = "ospyth" 
# Parent Directory path 
parentd = "C:\\Users\\p_m_rachana@lilly.com\OneDrive - Eli Lilly and Company\\lilly_python"  
# Path 
path = os.path.join(parentd, dir)   
os.mkdir(path) 
print("Directory '% s' created" % dir)


# Remove the file
       
file = 'fstri.txt'
location = "C:\\Users\\p_m_rachana@lilly.com\\OneDrive - Eli Lilly and Company\\lilly_python" 
# loc="C:\Users\p_m_rachana@lilly.com\OneDrive - Eli Lilly and Company\lilly_python"
path = os.path.join(location, file) 
os.remove(path)

# Rename the file

fd = "dbb.txt"
os.rename(fd,'New.txt')
#to check
os.rename(fd,'New.txt')

#list all directories
a=os.listdir()
print(a)

# to get virtual environment

b=os.getenv(key="JAVA_HOME")
print(b)


