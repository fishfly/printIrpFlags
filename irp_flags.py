"""
Description: This program is used for print IRP Flags

Developer: whtcjdtc2007@163.com
"""
import sys,string

base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
flags = ["IRP_NOCACHE", "IRP_PAGING_IO\\IRP_MOUNT_COMPLETION", "IRP_SYNCHRONOUS_API", "IRP_ASSOCIATED_IRP", "IRP_BUFFERED_IO", "IRP_DEALLOCATE_BUFFER", "IRP_SYNCHRONOUS_PAGING_IO\\IRP_INPUT_OPERATION", "IRP_CREATE_OPERATION", "IRP_READ_OPERATION", "IRP_WRITE_OPERATION", "IRP_CLOSE_OPERATION", "IRP_DEFER_IO_COMPLETION"]

def main():
	if len(sys.argv) < 2:
		print "Usage: python irp_flags.py param(hexadecimal)"
		print "Example: python irp_flags.py 0xa00"
		return

	# flag = string.atoi(sys.argv[1])
	flag_dec = int( sys.argv[1], 16 )
	print 'Decimal: ' + str(flag_dec)

	flag_str_bin = dec2bin(flag_dec)

	print 'Binary: ' + flag_str_bin

	length = len(flag_str_bin)

	if length > len(flags):
		length = len(flags)

	print 'IrpFlags:'
	for i in range(length):
		if flag_str_bin[length-i-1] == '1':
			print '\t' + flags[i]

def hex2dec(string_num):
	return str(int(string_num.upper(), 16))

def dec2bin(string_num):
	num = int(string_num)
	mid = []
	while True:
		if num == 0: break
		num,rem = divmod(num, 2)
		mid.append(base[rem])
	return ''.join([str(x) for x in mid[::-1]])


main()