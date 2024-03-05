import lecroy_module
import argparse
import sys

scope_ip_address = '172.17.19.40'

# create the object
obj = lecroy_module.LecroyScope(scope_ip_address)
save = lecroy_module.AutoSaveMode

try:
    # connect to the device
    obj.open()

    obj.disable_auto_save()

finally:
    # disconnect from the device
    print("disconnecting...")
    obj.close()