# the column represents the original word
word_file = open('words2.txt')
word_list = word_file.read().split('\r\n')
print "dictionary words count =",len(word_list)
def get_minimum_edit_distance(word_original, word_input):
    distance_matrix = [[x for x in range(len(word_original)+1)]]
#     def print_distance_matrix() :
#         for x in distance_matrix:
#             print x
    for x in range(len(word_input)):
        distance_matrix.append([x+1])
#     for x in distance_matrix:
#         print x
    for x in range(1, len(word_input)+1):
        current_row = distance_matrix[x];
        for y in range(1, len(word_original)+1):
            if(word_input[x-1] == word_original[y-1]):
                current_row.append(distance_matrix[x-1][y-1])
            else:
                current_row.append(min([distance_matrix[x-1][y-1], distance_matrix[x-1][y], current_row[y-1]] )+1)
#         print_distance_matrix()
#     print [' ']+list(word_original)
#     print_distance_matrix();
#     print [' '] + list(word_input)
    return distance_matrix[-1][-1]
# lesser value of threshold, less possibilities
threshold = 20
def get_ranked_list(word_input):
    print 'now checking', word_input,":",
    if word_input in word_list:
    	print "correct"
    	return []
    print "wrong"
    ranked_list = []
    for word in word_list:
        if abs(len(word) - len(word_input))/float(len(word_input)) >= threshold:
            distance = 100000
        else:
            distance = get_minimum_edit_distance(word, word_input)
        if distance/float(len(word_input)) <= threshold/100.0:
            ranked_list.append((word, distance))
    def getKey(x):
        return x[1]
    ranked_list.sort(key=getKey)
    #print ranked_list
    if ranked_list[0][1]==0:
        #print word_input,"is present in the dictionary"
        pass
    return ranked_list

word_input= raw_input("Please enter some text: ").split(" ")
for word in word_input:
	l = get_ranked_list(word)
	if l:
		print word, ":",[ll[0] for ll in l];
