def logthis(message) :
        """Writes message to SYSLOG and prints it to STDOUT.
        """
        syslog.syslog(syslog.LOG_INFO, '%s' % message )
        print "%s" % message


def random_wait() :
	"""Random wait (ms).
	"""
	random.seed()
	n = random.random()
	time.sleep(n)


def check_running_ps():
	"""Checks how many processes are running for a given server_name.
	   Returns max_ps_reached (int. binary)
	"""
        db=MySQLdb.connect(host=db_host, user=db_user, passwd=db_pass, db=db_database )
        cursor=db.cursor()
        cursor.execute("select servers_id, name, role, enabled, handicap, running_ps, max_ps from servers where name='%s';" % server_name )
        results=cursor.fetchall()
        cursor.close ()
        db.close ()
	for registry in results:
                servers_id=registry[0]
                name=registry[1]
                role=registry[2]
                enabled=registry[3]
                handicap=registry[4]
                running_ps=registry[5]
                max_ps=registry[6]
        if running_ps>=max_ps :
                max_ps_reached=1
        else :
                max_ps_reached=0
	return max_ps_reached


def update_running_ps(operation):
        """Adds/Substracts 1 to/from running_ps for the given server_name.
        """
        db=MySQLdb.connect(host=db_host, user=db_user, passwd=db_pass, db=db_database )
        cursor=db.cursor()
	if operation == "add" :
        	cursor.execute("update servers set running_ps=running_ps+1 where name='%s';" % server_name )
        elif operation == "substract" :
		cursor.execute("update servers set running_ps=running_ps-1 where name='%s';" % server_name )
	cursor.close ()
        db.commit ()
        db.close ()



def spawn_process(process) :
	"""Spawns a process like encode.py or ftp.py. It does not wait for the spawned process to finish.
	"""
	if process=="encode":
		pid = subprocess.Popen(["%s/ufe-encode.py" % core_root]).pid		
		logthis('Spawned %s with PID %i' % (process, pid))
	elif process=="ftp":
		pid = subprocess.Popen(["%s/ufe-ftp.py" % core_root]).pid
		logthis('Spawned %s with PID %i' % (process, pid))
	else:
		logthis('No process named %s !' % process)