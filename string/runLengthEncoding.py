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
	currentCharPointer = 1
	for i in range(1,len(string)):
		if string[i] != string[i - 1] or currentCharPointer == 9:
			encodedString.append(str(currentCharPointer))
			encodedString.append(string[i - 1])
			currentCharPointer = 0
		currentCharPointer = currentCharPointer + 1
	
	encodedString.append(str(currentCharPointer))
	encodedString.append(string[len(string) - 1])
	
	return "".join(encodedString)
	
	
	
