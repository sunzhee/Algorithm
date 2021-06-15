"""
Run-Length Encoding

Write a function that takes in a non-empty string and returns its
run-length encoding.
From Wikipedia, "run-length encoding is a form of lossless data
compression in which runs of data are stored as a single data
value and count, rather than as the original run." For this
problem, a run of data is any sequence of consecutive, identical
characters. So the run "AAA" would be run-length-encoded as
"3A" .
To make things more complicated, however, the input string can
contain all sorts of special characters, including numbers. And
since encoded data must be decodable, this means that we can't
naively run-length-encode long runs. For example, the run
"AAAAAAAAAAAA" (12 A s), can't naively be encoded as
"12A" , since this string can be decoded as either
"AAAAAAAAAAAA" or "1AA" . Thus, long runs (runs of 10 or
more characters) should be encoded in a split fashion; the
aforementioned run should be encoded as "9A3A" .

Sample Input
string = "AAAAAAAAAAAAABBCCCCDD"

Sample Output
"9A4A2B4C2D"


"""







def runLengthEncoding(string):
	encodedString = []
	letterCounter = 1
	# 一定要i和i-1比较
	for i in range(1,len(string)):
		# 必须要把这两个条件合成一个，否则当正好等于9的时候，会输出9A,0A,这个edge case无法处理
		if letterCounter == 9 or string[i-1] != string[i]:
			encodedString.append(str(letterCounter))
			encodedString.append(string[i-1])
			letterCounter = 0

		letterCounter += 1
	# 处理最后一个字符
	encodedString.append(str(letterCounter))
	encodedString.append(string[-1])

	return "".join(encodedString)
	
	
	
