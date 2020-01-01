{
    "Description": "this template will create a EOS environment.",
    "Parameters": {
        "ClusterURL": {
            "Type": "String",
            "Value": "http://10.255.20.122:8056/v1"
        },
        "SSD_DiskList_Pool": {
            "Type": "Integer",
            "Value": 13
        },
        "HDD_DiskList_Pool1": {
            "Type": "Integer",
            "Value": 14
        },
        "HDD_DiskList_Pool2": {
            "Type": "Integer",
            "Value": 15
        }
    },
    "Resources": [
        {
            "Name": "Token",
            "Type": "Token",
            "Action": "Create",
            "Properties": {
                "Name": "admin",
                "Password": "admin"
            }
        },
        {
            "Name": "SSDPool",
            "Type": "Pool",
            "Properties": {
                "name": "SSDPool",
                "ProtectionDomainID": 1,
                "WaitInterval": 60,
                "CheckInterval": 60,
                "PoolType": "replicated",
                "PoolRole": "index",
                "OsdIDs": {"Ref": "SSD_DiskList_Pool"},
                "Size": 1
            }
        },
        {
            "Name": "HDDPool",
            "Type": "Pool",
            "Properties": {
                "name": "HDDPool",
                "ProtectionDomainID": 1,
                "WaitInterval": 60,
                "CheckInterval": 60,
                "PoolType": "replicated",
                "PoolRole": "data",
                "OsdIDs": [
                    {"Ref": "HDD_DiskList_Pool1"},
                    {"Ref": "HDD_DiskList_Pool2"}
                ],
                "Size": 1
            }
        }
    ]
}
