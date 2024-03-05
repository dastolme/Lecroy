import lecroy_module
import argparse
import sys

scope_ip_address = '172.17.19.40'

# create the object
obj = lecroy_module.LecroyScope(scope_ip_address)
save = lecroy_module.AutoSaveMode

parser = argparse.ArgumentParser(description='Set the scope folder')
parser.add_argument("-f", "--field", help='Add drift field', action='store', type=int, default=None)
parser.add_argument("-hol", "--hole", help='Add hole', action='store', type=int, default=None)
parser.add_argument("-d", "--directory", help='Add directory', action='store', type=str, default=r'E:\nid\He_CF4_60_40_575mbar')
                    
args = parser.parse_args()

if args.field is None or args.hole is None:
    print('Add parameters')
    sys.exit()

file_path=args.directory+"\hole"+str(args.hole)+"\\"+str(args.field)+"V_cm\\"
print(file_path)

try:
    # connect to the device
    obj.open()

    #obj.create_directory(file_path = file_path)

    obj.action('app.SaveRecall.Setup.PanelFilename', r'C:\Users\LeCroyUser\Desktop\cygno_scripts\2024-NID.lss')
    obj.action('app.SaveRecall.Setup.DoRecallSetupFileDoc2')

    # Get the current AutoSave mode
    #obj.set_save_directory(file_path=r'E:\melba_tests\test1')
    obj.set_save_directory(file_path = file_path)
    obj.action('app.SaveRecall.ShowAutoSave')
    obj.set_auto_save_mode(save.FILL)

finally:
    # disconnect from the device
    print("disconnecting...")
    obj.close()