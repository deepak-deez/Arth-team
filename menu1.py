import os
import subprocess as sp
def main():
	while True:
		os.system("tput setaf 3")
		menu="""\tPress 1: For machine Learning and Artificial Intelligence
		Press 2: For Docker
		Press 3: For basic linux operations
		Press 4: For hadoop
		Press 0: To exit"""
		print(menu)
		k=input("Enter your choice: ")
		if(k=='1'):
			ML()
		elif(k=='2'):
			dock()
		elif(k=='3'):
			lin()
		elif(k=='4'):
			had()
		elif(k=='0'):
			break
		else:
			print("invalid input!")
			os.system("sleep 5")
			continue

def ML():
	ch=int(input('''\n 			--|-- Welcome to M.L. --|--\n\n
	Press 1 -: To Train the Machine or create the Model and do Further stuffs
	Press 2 -: To do stuffs with your data (like see your data in a graph,know the Dimensions etc.)\n\n
	Enter your choice :'''))

	inp=int(input('''\nHow you want to provide your data?\n
		Press 1 :- from 'csv' File
		Press 2 :- Manually\n
		Enter your choice...'''))

	
	
	if inp==1:
		name=input('\nwrite csv file name (eg. abc.csv) : ')
		import pandas
		Dataset=pandas.read_csv(name)
		col=Dataset.columns
		x=Dataset[col[0]]
		x=x.values
		y=Dataset[col[1]]
		y=y.values
	elif inp==2:
		x=[int(i) for i in input('\nenter predictor values : ').split()]
		y=[int(i) for i in input('enter finalOutcome values : ').split()]
		x=numpy.array(x)
		y=numpy.array(y)
	else:
		print('\nwrong choice')
		exit()

	if ch==1:
		y=y.reshape(-1,1)
		x=x.reshape(-1,1)
		model=LinearRegression()
		model.fit(x,y)
		dt=x.dtype
	
		op=int(input('''\n	Press 1 -: To predict outcome
		Press 2 -: To Get the BIAS
		Press 3 -: To Get the Coefficient/Pattern
		Press 4 -: To Get the model created in a file\n
		Enter your choice...'''))
	
		if op==1:	
			if dt=='int32':
				pre=int(input('\nEnter your Predictor value :\n '))
				print(model.predict([[pre]]))
			elif dt=='float64':
				pre=float(input('\nEnter your Predictor value :\n '))
				print(model.predict([[pre]]))
		elif op==2:
			print(model.intercept_)
		elif op==3:
			print(model.coef_)
		elif op==4:
			import joblib
			file=input('\nEnter file name in which you want your model (eg. abc.pk1) :\n')
			joblib.dump(model,file)
			print(file)
		else:
			print('\nwrong choice')
	elif ch==2:
		data=int(input('''
		Press 1 -: To check the Dimensions of Array
		Press 2 -: To check the Datatype of values inside your Data
		Press 3 -: To see the Field Names
		Press 4 -: To retrieve any Column/Field data
		Press 5 -: To retrieve any row data
		Press 6 -: To retrieve any particular data\n\n
		Enter your choice...\n'''))

		if data==1:
			print(x.shape)
			print(y.shape)
		elif data==2:
			print(x.dtype)
			print(y.dtype)
		if inp==1:
			if data==3:
				print(Dataset.columns)
			elif data==4:
				f=input('\nenter Field Name :\n')
				print(Dataset[f])
			elif data==5:
				r=int(input('\nenter row number :\n'))
				print(Dataset.iloc[r])
			elif data==6:
				r,c=[int(i) for i in input('\nenter row and column number :\n').split()]
				print(Dataset.iloc[r,c])
			else:
				print('\nwrong choice')
		else:
			print('\nwrong choice')
			print('\ Because Maybe you provided data manually')
	else:
		print('\nwrong choice')


		
def dock():
	
	action=int(input("""What would you like to do in Docker ? :
		1.Install Docker.
		2.Start docker.
		3.Know the status of Docker.
		4.Download Docker Image.
		5.List of Docker Images installed in the system.
		6.Install Docker Image in the system.
		7.Terminate Docker Image."""))
	if action == 1:
		os.system("dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")		
		os.system("dnf install docker-ce --nobest")
		input("Press Enter  ")
	elif action == 2:
		os.system("systemctl start docker")
		input("Press Enter  ")
	elif action == 3:
		os.system("systemctl status docker")
		input("Press Enter  ")
	elif action == 4:
		sp.getoutput("systemctl start docker")
		img = input("Enter the name of the image that you want to download : ")
		os.system("docker pull {}".format(img))
		os.system("docker images")
		input("Press Enter  ")
	elif action == 5:
		os.system("docker images")
		input("Press Enter  ")
	elif action == 6:
		os.system("docker image")
		img = input("Enter the name of the Docker Image: ")	
		osname = input("Enter the Image name: ")
		os.system("docker run -it -name {} {}".format(osname,img))
		input("Press Enter  ")
	elif action == 7:
		os.system("docker ps")
		sp.getoutput("systemctl start docker")
		dockerid = input("Enter any OS name to remove Docker Image: ")
		os.system("docker rm {}".format(dockerid))
		input("Press Enter  ")

def lin():
	print("\t\t\ Hello! Welcome to linux basic menu.... \n")
	menu="""\n Press 1: date and calendar
	Press 2: ram(memory) / ip / network connectivity
	Press 3: Install / Uninstall
	Press 4: Configure yum
	Press 5: Services
	Press 6: File Management
	Press 0: To exit \n"""
	print(menu)
	print("Please configure yum before installing or uninstalling a software -->press 4 \n")
	x=input("Enter your choice:")
	if(x=='1'):
		os.system("clear")
		m1="""Press 1: To see current date and time
		Press 2: To see the calendar."""
		print(m1)
		x1=input("Enter your choice:")
		if(x1=='1'):
			op=sp.getstatusoutput("date")
		elif(x1 == '2'):
			op=sp.getstatusoutput("cal")
		else:
			op="Invalid choice!"
			os.system("sleep 3")
		print(op)
	elif(x=='2'):
		os.system("clear")
		m2="""Press 1: To see RAM info.
		Press 2: To see the IP address
		Press 3: To check ping
		Press 4: To check connectivity with a specific IP."""
		print(m2)
		x2=input("Enter your choice:")
		if(x2=='1'):
			op=sp.getstatusoutput("free -m")
		elif(x2=='2'):
			op=sp.getstatusoutput("ifconfig")
		elif(x2=='3'):
			op=sp.getstatusoutput("ping")
		elif(x2=='4'):
			ip=("Enter the IP:")
			op=sp.getstatusoutput("ping -c 5".format(ip))
		else:
			op="Invalid choice!"
			os.system("sleep 3")
		print(op)
	elif(x=='3'):
		os.system("clear")
		m3="""Press 1: To query about a software
		Press 2: To install a software from a download link
		Press 3: To install a software / package
		Press 4: To uninstall a software"""
		print(m3)
		x3=input("Enter your choice")
		if(x3=='1'):
			s=input("Enter the name of software/package you want to query about")
			op=sp.getstatusoutput("rpm -q {}".format(s))
		elif(x3=='2'):
			link=input("Enter the link")
			op=os.system("yum install {}".format(link))
		elif(x3=='3'):
			s=input("Enter the name of software/package you want to install")
			op=os.system("yum install {}".format(s))
		elif(x3=='4'):
			s=input("Enter the name of software/package you want to remove")
			op=os.system("yum remove {}".format(s))
		else:
			op="Invalid choice!"
			os.system("sleep 3")
		print(op)
	elif(x=='4'):
		os.system("clear")
		op=sp.getstatusoutput("yum install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
		os.system("yum repolist")
	elif(x=='5'):
		os.system("clear")
		m5="""Press 1: To start a service
		Press 2: To stop a service
		Press 3: To enable a service
		Press 4: To check status of a service"""
		print(m5)
		x5=input("Enter your choice")
		if(x5=='1'):
			st=input("Enter the name of the service")
			op=sp.getstatusoutput("systemctl start {}".format(st))
			os.system("systemctl status {}".format(st))
		elif(x5=='2'):
			st=input("Enter the name of the service")
			op=os.system("systemctl stop {}".format(st))
			os.system("systemctl status {}".format(st))
		elif(x5=='3'):
			st=input("Enter the name of the service")
			op=os.system("systemctl enable {}".format(st))
			os.system("systemctl status {}".format(st))
		elif(x5=='4'):
			st=input("Enter the name of the service")
			op=os.system("systemctl disable {}".format(st))
			os.system("systemctl status {}".format(st))
		elif(x5=='5'):
			st=input("Enter the name of the service")
			op=os.system("systemctl status {}".format(st))
		else:
			op="Invalid choice!"
			os.system("sleep 3")
		print(op)
			
	elif(x=='6'):
		os.system("clear")
		m6="""Press 1: To check present directory
		Press 2: To change directory
		Press 3: To see the present directory contents
		Press 4: To create a folder
		Press 5: To create a text file
		Press 6: To read the file
		Press 7: To remove the file"""
		print(m6)
		x6=input("Enter your choice")
		if(x6=='1'):
			print("Present directory is:")
			op=os.system("pwd")
		elif(x6=='2'):
			p=input("Enter folder/path:") 
			op=sp.getstatusoutput("cd {}".format(p))
		elif(x6=='3'):
			op=sp.getstatusoutput("ls")
		elif(x6=='4'):
			n=input("Enter the name of the folder")
			op=sp.getstatusoutput("mkdir {}".format(n))
		elif(x6=='5'):
			n=input("Enter the name of the file with .txt extension")
			sp.getstatusoutput("gedit {}".format(n))
		elif(x6=='6'):
			n=input("Enter the name of the file")
			op=sp.getstatusoutput("gedit {}".format(n))
		elif(x6=='7'):
			n=input("Enter the name of the file")
			op=sp.getstatusoutput("rm {}".format(n))
			print("file removed")
		else:
			op="Invalid choice!"
			os.system("sleep 3")
		print(op)
		
	elif(x=='0'):
		os.system("clear")
		exit()	
	else:
		op="Invalid choice!"
		os.system("sleep 3")
	print(op)

def had():
	from jinja2 import Environment, FileSystemLoader

	action=int(input("""What would you like to do in Hadoop ? :
		1.Install hadoop services.
		2.configure hdfs-site.xml.
		3.configure core-site.xml.
		4.Download Docker Image.
		5.configure namenode.
		6.configure datyanode.
		7.to start the hadoop services.\n"""))

	if action == 1:    
		def installtionScript(nodeType,directoryPath):
			file_loader = FileSystemLoader('./hadoopCluster/templates')
			env = Environment(loader=file_loader)
			template = env.get_template('installationScript.sh.j2')
			output = template.render(nodeType = nodeType , directoryPath = directoryPath)
			file = open("./hadoopCluster/temp/installationScript.sh", "w")
			file.write("%s" %(output))
			file.close()

	if action == 2:	
		def hdfsSite(nodeType,directoryPath):
			file_loader = FileSystemLoader('./hadoopCluster/templates')
			env = Environment(loader=file_loader)
			template = env.get_template('hdfs-site.xml.j2')
			output = template.render(nodeType = nodeType , directoryPath = directoryPath)
			file = open("./hadoopCluster/temp/hdfs-site.xml", "w")
			file.write("%s" %(output))
			file.close()

	if action == 3:
		def coreSite(nodeIp,nodePort):
			file_loader = FileSystemLoader('./hadoopCluster/templates')
			env = Environment(loader=file_loader)
			template = env.get_template('core-site.xml.j2')
			output = template.render(IP = nodeIp , port = nodePort)
			file = open("./hadoopCluster/temp/core-site.xml", "w")
			file.write("%s" %(output))
			file.close()
		
	if action == 4:
		def copyTemplate(nodeIP):
			sp.run(f'scp ./hadoopCluster/temp/hdfs-site.xml root@{nodeIP}:/root/hdfs-site.xml',shell=True)
			sp.run(f'scp ./hadoopCluster/temp/core-site.xml root@{nodeIP}:/root/core-site.xml',shell=True)
		
	if action == 5:
		def nameNode(nameNodeIP):
			nameNodeDirectory = input('Enter Name Node Directory Name : ')
			nameNodePort = input('Enter Name Node port : ')
			hdfsSite('name',f'/root/{nameNodeDirectory}')
			coreSite(nameNodeIP,nameNodePort)
			copyTemplate(nameNodeIP)
			installtionScript('name',nameNodeDirectory)
			sp.run(f"ssh root@{nameNodeIP} 'bash -s' < ./hadoopCluster/temp/installationScript.sh",shell=True)
			return nameNodePort


	if action == 6:
		def dataNode(dataNodeIP,nameNodeIP,nameNodePort):
			dataNodeDirectory = input('Enter Data Node Directory Name : ')
			hdfsSite('data',f'/root/{dataNodeDirectory}')
			coreSite(nameNodeIP,nameNodePort)
			copyTemplate(dataNodeIP)
			installtionScript('data',dataNodeDirectory)
			sp.run(f"ssh root@{dataNodeIP} 'bash -s' < ./hadoopCluster/temp/installationScript.sh",shell=True)

	if action == 7:
		def configure():
			nameNodeIP = input('Enter Name Node IP : ')
			dataNodeIP = input('Enter Data Node IP : ')
			nameNodePort = nameNode(nameNodeIP)
			dataNode(dataNodeIP,nameNodeIP,nameNodePort)
	else:
		print("Invalid choice!")
		os.system("sleep 3")

main()
	
		
		

		

			
		
	
