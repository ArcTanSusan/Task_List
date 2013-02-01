import random
import string 

def process_file(str):
	#open desired file
	f = open(str)
	#read it in, lower case
	text = f.read() #.lower()
	f.close()
	text=text.split()
	#print len(text)
	return text

#process_file("emma.txt")

def markov_dictionary(text, ngram):
	text = process_file(text)
	#print type(text)
	#print len(text)
	#index = ngram
	index = 0
	markov_dict = {}
	ngram = int(ngram)
	# while count <= ngram:
	# 	key +=text[count]
	key = []
	key_index = 0

	while index <(len(text)):
		#index= ngram-index
		index -= ngram 
		while key_index < ngram: # Placing every character from sample text into the string "key". 
			key.append(text[index]) #+" "+ str(text[index])
			key_index +=1
			index += 1
		key = " ".join(key)
	 	if markov_dict.get(key): #markov_dict[key] == None:
 	 		markov_dict[key].append(text[index])
 	 		index +=1
 	 		key_index = 0
 	 		key =[]
	 	else:
 			markov_dict[key] = [(text[index])] #Values have to  be in a list! There can be more than 1 value in a key! Tuples or strings won't work 
 			index += 1
 			key_index = 0
 	 		key = [] 

	return markov_dict

#markov_dictionary("sample5.txt",6)
#markov_dictionary("emma.txt",5)
#markov_dictionary("emma.txt",10)

def print_markov(text, ngram):
	text_split = process_file(text)
	#print len(text_split)
	markov_dict = markov_dictionary(text, ngram)
	keys = markov_dict.keys()
	key = random.choice(keys)
	val = random.choice(markov_dict[key])

	keywords = key.split()

	new_list = [ ]
	new_list.extend(keywords)
	new_list.append(val)
	#print new_list
	last_word = val

	while last_word[-1] not in '?.!': #"?.!": #this makes the while loop stop when there's a  #period at the end of a word
		# ( w1 ... wn ) -> w( n+ 1)
		# ( w2 .... wn + 1)
		keywords = keywords[1:]
		keywords.append(last_word)
		new_val = markov_dict[" ".join(keywords)]
		last_word = random.choice(new_val)
		new_list.append(last_word)

	new_list = " ".join(new_list)
	#print new_list
	first_char = new_list[0].capitalize()
	#print type(first_char)
	#print first_char
	new_list=new_list.replace(new_list[0], first_char,1)
	#print new_list
	return new_list

#print_markov("emma.txt", 3)

def print_twitter(sample_text, num_sentences, ngram): 
	i=0
	sentences= " "
	char_count=0 
	while i<num_sentences: 
		sentences+=print_markov(sample_text,ngram) 
		i+=1	
	# print sentences
	# num_chars =0
	# for chars in sentences:
	# 	num_chars +=1
	#print num_chars
	# if num_chars > 9000:
	# 	print_twitter(sample_text, 1, ngram)
	# else:
	# 	print sentences
	return sentences

#print_twitter("hp.txt", 2,2)
#print_twitter("Midsummer_Night's_Dream.txt",2, 2)
#print_twitter("Last_Guardian.txt",2, 3)
