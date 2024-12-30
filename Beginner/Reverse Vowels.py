def reverseVowels(s):

	vowels = 'aeiouAEIOU'

	str_list = list(s)

	i = 0
	j = len(s)-1

	while i < j:
		if str_list[i] in vowels:
			while j > i:
				if str_list[j] in vowels:

					temp = str_list[j]
					str_list[j] = str_list[i]
					str_list[i] = temp

					j -= 1

					break
				else:
					j -= 1
				
		i += 1

	return ''.join(str_list)

#----------------------------------------

def reverseVowels(s):
	left = 0
	right = len(s) - 1
	s = list(s)
	vowels = set('aeiouAEIOU')

	while left < right:
		while s[left] not in vowels and left < right:
			left += 1
		while s[right] not in vowels and left < right:
			right -= 1

		s[left], s[right] = s[right], s[left]
		left += 1
		right -= 1

