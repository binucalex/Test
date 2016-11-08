# ------------------------------------------------------
# get line separator
import  java.lang.System  as  sys
lineSeparator = sys.getProperty('line.separator')
def wsadminToList(inStr):
        outList=[]
        if (len(inStr)>0 and inStr[0]=='[' and inStr[-1]==']'):
                tmpList = inStr[1:-1].split() #splits space-separated lists,
        else:
                tmpList = inStr.split("\n")   #splits for Windows or Linux
        for item in tmpList:
                item = item.rstrip();         #removes any Windows "\r"
                if (len(item)>0):
                        outList.append(item)
        return outList
#endDef
def status():
	cells = AdminConfig.list('Cell').split()
	for cell in cells:
    #----------------------------------------------------------------
    # lines 13 and 14 find all the nodes belonging to the cell and
    # process them at a time
    #-----------------------------------------------------------------
   	 nodes = AdminConfig.list('Node', cell).split()
   	 for node in nodes:
        #--------------------------------------------------------------
        # lines 19-23 find all the running servers belonging to the cell
        # and node, and process them one at a time
    #--------------------------------------------------------------
    		cname = AdminConfig.showAttribute(cell, 'name')
   		nname = AdminConfig.showAttribute(node, 'name')
    		servs = AdminControl.queryNames('type=Server,cell=' + cname +',node=' + nname + ',*').split()
    		print "Number of JVM's " + nname + ": %s \n" %(len(servs))
    		for server in servs:
        #---------------------------------------------------------
        #lines 28-34 get some attributes from the server to display;
        # invoke an operation on the server JVM to display a property.
        #---------------------------------------------------------
        		sname = AdminControl.getAttribute(server, 'name')
        		ptype = AdminControl.getAttribute(server, 'processType')
       	 		pid   = AdminControl.getAttribute(server, 'pid')
        		state = AdminControl.getAttribute(server, 'state')
        		jvm = AdminControl.queryNames('type=JVM,cell=' + cname +',node=' + nname + ',process=' + sname + ',*')
       			osname = AdminControl.invoke(jvm, 'getProperty', 'os.name')
       			print "--------------------------------------------------------------------------------------------"
        		print " " + sname + " " +  ptype + " has pid " + pid + ";Status is : " + state + "; on " + osname + "\n"
        		print "--------------------------------------------------------------------------------------------"
 
        #---------------------------------------------------------
        # line 40-45 find the applications running on this server and
        # display the application name.
        #---------------------------------------------------------
        		apps = AdminControl.queryNames('type=Application,cell=' + cname+ ',node=' + nname + ',process=' + sname + ',*').splitlines()
       			print "Number of applications running on " + sname + ": %s \n"% (len(apps))
        		for app in apps:
        			aname = AdminControl.getAttribute(app, 'name')
        			print aname + "\n"
       				#print "----------------------------------------------------"
       				#print "\n"
def processInstanceID():
	cells = AdminConfig.list('Cell').split()
	for cell in cells:
    #----------------------------------------------------------------
    # lines 13 and 14 find all the nodes belonging to the cell and
    # process them at a time
    #-----------------------------------------------------------------
   	 nodes = AdminConfig.list('Node', cell).split()
   	 for node in nodes:
        #--------------------------------------------------------------
        # lines 19-23 find all the running servers belonging to the cell
        # and node, and process them one at a time
    #--------------------------------------------------------------
    		cname = AdminConfig.showAttribute(cell, 'name')
   		nname = AdminConfig.showAttribute(node, 'name')
    		servs = AdminControl.queryNames('type=Server,cell=' + cname +',node=' + nname + ',*').split()
    		#print "Number of JVM's on node " + nname + ": %s \n" %(len(servs))
    		for server in servs:
        #---------------------------------------------------------
        #lines 28-34 get some attributes from the server to display;
        # invoke an operation on the server JVM to display a property.
        #---------------------------------------------------------
        		sname = AdminControl.getAttribute(server, 'name')
        		ptype = AdminControl.getAttribute(server, 'processType')
       	 		pid   = AdminControl.getAttribute(server, 'pid')
        		state = AdminControl.getAttribute(server, 'state')
        		jvm = AdminControl.queryNames('type=JVM,cell=' + cname +',node=' + nname + ',process=' + sname + ',*')
       			osname = AdminControl.invoke(jvm, 'getProperty', 'os.name')
       			print "--------------------------------------------------------------------------------------------"
        		print " " + sname + " " +  ptype + " has pid " + pid + ";Status is : " + state + "; on " + osname + "\n"
        		print "--------------------------------------------------------------------------------------------"
        		



def clusterInfo():
	cells = AdminConfig.list('Cell').split()
	for cell in cells:
		cluster_ids = AdminConfig.list( 'ServerCluster' ).split()
                for cluster in cluster_ids:
                	clusname = AdminConfig.showAttribute(cluster, 'name' )
               	   	print "ClusterName :: "+clusname
                	
                	
    
def ServerControl():
	print """ Server Information Menu
 	1. Show Server info & Status
 	2. Process Instance ID & Status
 	3. ClusterInfo
 	4. Exit Menu
 	"""
	choice=input("Select choice: ")
 	return choice
while 1:
	ch=ServerControl()
	if ch == 1:
  		status()
  		print "Server Detail Status is Displayed above ... Return to MainMenu : \n",ServerControl()
  		
	elif ch == 2:
  		processInstanceID()
  		print "PID information is Displayed above ... Return to MainMenu : \n",ServerControl()
  		
	elif ch==3:
  		clusterInfo()
  		print "Cluster Names are Listed above ... Return to MainMenu :\n",ServerControl()
	elif ch==4: 
 		print "Exit from menu..."
	break
      			