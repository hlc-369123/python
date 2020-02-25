#!/usr/bin/bash
set -x
export PS4='+[#$LINENO ${FUNCNAME[0]}() $BASH_SOURCE] '

declare -a IP
IP[0]=$1
IP[1]=$2
IP[2]=$3
#cd /tmp
if [ "${IP[2]}" ];then
        XSKY_THREE_NODES=yes
elif [ -z "${IP[2]}" -a "${IP[1]}" ];then
        XSKY_TWO_NODES=yes
fi
wget http://192.168.200.100/mirror/pengtao/cluster.json
if [[ ${IP[0]} == 172.24.* ]]; then
        sed -i "s/172.20.0.1/172.24.0.1/g" cluster.json
fi

tar zxvf SDS_4.1.000.2_RTMVersion_ZStack_WithLicense.tar.gz

sed -i "s/10.0.0.x/${IP[0]}/" tools/ansible/hosts
sed -i "s/10.0.1.x/${IP[1]}/" tools/ansible/hosts
#sed "4 i${IP[0]}" -i tools/ansible/hosts
#sed "4 i${IP[1]}" -i tools/ansible/hosts
if [ "${XSKY_THREE_NODES}" == yes ];then
        sed "4 i${IP[2]}" -i tools/ansible/hosts
fi
sed -i 's/passwd/password/' tools/ansible/hosts
#sed -i 's/ansible_ssh_pass=/ansible_ssh_pass=password/' tools/ansible/hosts
sed -i 's/set_hostname: false/set_hostname: true/' tools/ansible/group_vars/nodes
sed '10 idisable_firewalld: true' -i tools/ansible/group_vars/nodes
#sed -i 's/hostname_prefix: sds/hostname_prefix: ceph/' tools/ansible/group_vars/nodes
sed -i "s/172.20.196.210/${IP[0]}/g" cluster.json
sed -i "s/172.20.195.198/${IP[1]}/g" cluster.json
if [ "${XSKY_THREE_NODES}" == yes ];then
        sed -i "s/172.20.198.209/${IP[2]}/g" cluster.json
fi

sshpass -p password  ssh root@${IP[1]} "rm -f /root/.ssh/id_rsa*;chown root:root /root;chmod g-w /root"
if [ "${XSKY_THREE_NODES}" == yes ];then
        sshpass -p password  ssh root@${IP[2]} "rm -f /root/.ssh/id_rsa*;chown root:root /root;chmod g-w /root"
fi
sshpass -p password  ssh root@${IP[0]} "rm -f /root/.ssh/id_rsa*;chown root:root /root;chmod g-w /root"

#sshpass -p password ssh root@172.20.195.153 "ls /root"
[ ! -f /root/.ssh/id_rsa ] && ssh-keygen -q -t rsa -N "" -f /root/.ssh/id_rsa
sleep 2

cd tools
bash prepare.sh -i ansible/hosts --silent
if [ $? -eq 0 ];then
        sleep 1
        cd ..
        bash install.sh ${IP[0]}
        if [ $? -eq 0 ];then
        sleep 60
#               for ((i=0;i<10;i++))
#               do
#                       xms-cli --user admin -p password bootnode show
#                       if [ $? -eq 0 ];then
#                               break
#                       else
#                               sleep 5
#                       fi
#               done
#               sleep 1
                init_admin_token=`cat /etc/xms/initial-admin-token`
                sds-formation -f cluster.json -t $init_admin_token
                if [ $? -ne 0 ];then
                        echo "setup cluster failed"
                                        fi
        else
                echo "Install xsky failed"
        fi
else
        echo "Prepare setup environment failed"
fi
