import re
import subprocess
from pynginxconfig import NginxConfig
# from subprocess import Popen,PIPE
import json

# upstreamList = list()
upstreams = dict()
upstreams['main'] = dict()
upstreams['main']['http'] = dict()
upstreams['main']['tcp'] = dict()
upstreams['main']['tcp']['proxy_pass']= dict()
upstreams['main']['http']['proxy_pass']= dict()
upstreams['include'] = dict()
upstreams['include']['http'] = dict()
upstreams['include']['tcp'] = dict()
upstreams['include']['tcp']['proxy_pass'] = dict()
tmpList1 = list()
mainConf="/apps/nginx/conf/nginx.conf"
confDir="/apps/nginx/conf/"
nc = NginxConfig()

def runcmd(command):
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
    return ret.stdout
dirs = runcmd("cat {} |grep -i include |grep -v {} |grep -v '{}'".format(mainConf,"mime.types","#"))

if dirs:
    conf_dir = re.findall(r'(?<=include)[\s]+(.+);',str(dirs))
else:
    conf_dir=list()
    upstreamL=list()

for conf in conf_dir:
    conf = confDir + conf
    files = runcmd("ls {}".format(conf))
    fileList=files.split('\n')
    for f in fileList:
        if f:
            nc.loadf(f)
            block = nc.get(('stream',))
            if block:
                for upstream in block.get("value",[]):
                    up = upstream['param']
                    upstreamList = list()
                    tmpList = list()
                    srvs = upstream.get("value",[])
                    for item in srvs:
                        if len(item) == 2 and item[0] == 'server':
                            upstreamList.append(item[1])
                            upstreams['include']['tcp'][up] = upstreamList
                        if len(item) == 2 and item[0] == 'proxy_pass':
                            socketList = re.findall('\d+.\d+.\d+.\d+:\d+', item[1])
                            for socket in socketList:
                                tmpList.append(item[1])
                                upstreams['include']['tcp']['proxy_pass'] = tmpList

            upstream_all = runcmd("cat {} |grep upstream |grep -v -w {}|grep -v '{}'".format(f,'stream','#'))
            upstream = re.findall(r'[\s]*upstream\s+(\w*).*{.*',upstream_all)
            proxypass_all = runcmd("cat {} |grep proxy_pass|grep {}|grep -v '{}'".format(f,'http://','#'))
            proxypass = re.findall(r'\d+.\d+.\d+.\d+:\d+',proxypass_all)
            if proxypass:
                for pro in proxypass:
                    # print("pro:",pro)
                    tmpList1.append(pro)
                    upstreams['include']['http']['proxy_pass'] = tmpList1
            upstreamList=list()
            tmpList = list()
            if upstream:
                for up in upstream:
                    srvs = nc.get(('upstream',up)) if nc.get(('upstream',up)) else {"value":[]}
                    for item in srvs.get("value",[]):
                        if len(item) == 2 and item[0] == 'server':
                            upstreamList.append(item[1])
                            upstreams['include']['http'][up] = upstreamList
nc.loadf(mainConf)
block = nc.get(('stream',))
blockh = nc.get(('http',))
if block:
    for upstream in block.get("value",[]):
        up = upstream['param']
        upstreamList=list()
        if up != 'server':
            srvs = upstream.get("value",[])
            for item in srvs:
                if len(item) == 2 and item[0] == 'server':
                    upstreamList.append(item[1])
                    upstreams['main']['tcp'][up] = upstreamList
        else:
            srvs = upstream.get("value", [])
            for item in srvs:
                if len(item) == 2 and item[0] == 'proxy_pass':
                    socketList=re.findall('\d+.\d+.\d+.\d+:\d+',item[1])
                    for socket in socketList:
                        upstreamList.append(item[1])
                        upstreams['main']['tcp']['proxy_pass'] = upstreamList

if blockh:
    for upstream in blockh.get("value",[]):
        upstreamList=list()
        if isinstance(upstream,dict) and upstream.get("name") == "upstream":
            up = upstream['param']
            srvs = upstream.get("value",[])
            for item in srvs:
                if len(item) == 2 and item[0] == 'server':
                    upstreamList.append(item[1])
                    upstreams['main']['http'][up] = upstreamList
        if  isinstance(upstream,dict) and upstream.get("name") == 'server':
            srvs = upstream.get("value", [])
            for item in srvs:
                if isinstance(item, dict) and item.get("name") == 'location':
                    up = item.get("param", '')
                    contents = item.get("value", [])
                    for item in contents:
                        if len(item) == 2 and item[0] == 'proxy_pass':
                            socketList = re.findall('\d+.\d+.\d+.\d+:\d+', item[1])
                            for socket in socketList:
                                upstreamList.append(socket)
                                upstreams['main']['http']['proxy_pass'] = upstreamList


print(json.dumps(upstreams,indent=4))