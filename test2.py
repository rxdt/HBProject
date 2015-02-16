cmd = "update people set name=%s where id=%s"
curs.execute(cmd, (name, id))