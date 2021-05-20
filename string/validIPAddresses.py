"""
Valid IP Addresses

You're given a string of length 12 or smaller,
containing only digits. Write a function that
returns all the possible IP addresses that can
be created by inserting three . s in the
string.
An IP address is a sequence of four positive
integers that are separated by . s, where
each individual integer is within the range
0 - 255 , inclusive.
An IP address isn't valid if any of the
individual integers contains leading 0 s. For
example, "192.168.0.1" is a valid IP
address, but "192.168.00.1" and
"192.168.0.01" aren't, because they
contain "00" and 01 , respectively.
Another example of a valid IP address is
"99.1.1.10" ; conversely, "991.1.1.0"
isn't valid, because "991" is greater than
255.
Your function should return the IP addresses
in string format and in no particular order. If
no valid IP addresses can be created from
the string, your function should return an
empty list.
Note: check out our Systems Design
Fundamentals on SystemsExpert to learn
more about IP addresses!

Sample Input
string = "1921680"

Sample Output
[
 "1.9.216.80",
 "1.92.16.80",
 "1.92.168.0",
 "19.2.16.80",
 "19.2.168.0",
 "19.21.6.80",
 "19.21.68.0",
 "19.216.8.0",
 "192.1.6.80",
 "192.1.68.0",
 "192.16.8.0"
]
"""

# O(1) time, O(1) space 因为最大是255，有上限，不是无穷大的n，所以统统是O(1)
# 一位一位的循环，找出所有valid的ip地址组合
def validIPAddresses(string):
	ipAddressesFound = []
	
	# 从前1位到3位之间循环，如果不足3位则取全部剩余长度
	for i in range(1,min(len(string),4)):
		currentIPAddressParts = ["","","",""]
		
		# 第一部分IP地址，从开始一直到i
		currentIPAddressParts[0] = string[:i]
		if not isValidIPAddress(currentIPAddressParts[0]):
			# 如果第一部分不合法，直接跳出这个循环，做下一个，后面的part 1,2,3不用看了
			continue
		# 第二部分IP地址，从j = i+1开始，往后看3位，如果不足3位则看全部的剩余长度
		for j in range(i+1,i + min(len(string)-i, 4)):
			# 切出来第二部分，i到j这一段
			currentIPAddressParts[1] = string[i:j]
			if not isValidIPAddress(currentIPAddressParts[1]):
				continue
			for k in range(j+1,j + min(len(string)-j, 4)):
				# 第三部分 j到k这一段
				currentIPAddressParts[2] = string[j:k]
				# 第四部分不需要循环了，把剩下的都拿到即可，从k到结束
				currentIPAddressParts[3] = string[k:]
				# 第三第四部分，一起判断
				if isValidIPAddress(currentIPAddressParts[2]) and isValidIPAddress(currentIPAddressParts[3]):
					# 都合法，则添加到结果集，用"."join在一起
					ipAddressesFound.append(".".join(currentIPAddressParts))
	return ipAddressesFound
		

def isValidIPAddress(string):
	stringAsInt = int(string)
	if stringAsInt > 255:
		return False
	# 这里不能直接返回True, 需要检查起始0的情况
	# 返回如果长度如果相等，则说明没有leading 0,如果不等，说明一开始有0
	# 例如 011, 结果就是不相等，string是3，len(str(int)是2
	return len(string) == len(str(stringAsInt))
