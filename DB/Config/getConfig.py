#!/usr/bin/env python

def mysqlConfig():
    cfg = {'host':'', 'user':'', 'passwd':'', 'port':'', 'database':''}
    
    cfgPath = 'config/mysql.cfg'
    infile = open(cfgPath, 'r')

    while 1:
        line = infile.readline()
        if not line:
            break
        elif line == '\n':
            continue
        elif line[0] == '#':
            continue
        else:
            c = line.rstrip('\n').split('\t')
            if c[0] == 'host':
                cfg['host'] = c[1]
            elif c[0] == 'user':
                cfg['user'] = c[1]
            elif c[0]  == 'passwd':
                cfg['user'] = c[1]
            elif c[0] == 'database':
                cfg['database'] = c[1]
            elif c[0] == 'port':
                cfg['port'] = c[1]
            else:
                continue
    infile.close()
    return cfg
if __name__ == '__main__':
    print 'Function: mysqlConfig()'
    print '\tRead config/mysql.cfg file, return a dictionary contains:'
    print '\t\t"host", "user", "passwd", "port", "database"'
