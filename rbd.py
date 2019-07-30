import rados
import rbd
import pdb

pdb.set_trace()
client = rados.Rados(rados_id="cinder",clustername="ceph",conffile="/etc/ceph/ceph.conf")
client.connect()
ioctx = client.open_ioctx("pool-a69d5cd8585540baa0188ee30317ffc1")
try:
    rbd.Image(ioctx, 'voludc240159e288b1e52342d3c', snapshot=None, read_only=False)
except rbd.Error:
    ioctx.close()
    client.shutdown()

print('===end===')
