import py.test
#Read a file of sequences
#Get the length of each sequence in a file and save it as k
#Calculate the possible number of substrings for 1 to k
#Calculate observed number of substrings for 1 to k
#Divide possible substrings by observed substrings
#Return a list of each substring with linguistic complexity

#Obs_substrings will take a sequence and the desired substring length
def obs_substrings(sequence, k):
    '''
obs_substrings determines the number of substrings of length k in a sequence (sequence). 
It does this by iterating over the sequence and at each iteration creating a substring of length k.
It then adds the substring to a dictionary, if it is the first instance of that substring.
If the substring had already been encountered it simply updates the number of times that string occurs.
Finally it returns the length of the dictionary which is the number of substrings.
    '''
#Making sure the the length of the sequence is >= k
    assert len(sequence) >= k, "The sequence should be longer than k"
#Creates an empty dictionary for storing the number of times a substring appears
    string_dict = {}
#Iterates over the sequence
    for i in range (0,len(sequence)-1):
#Creates a substring of length k
        sub = sequence[i:i+k]
#Updates the dictionary every time a string is encountered again or adding it if its the first time
        if sub in string_dict:
            cnt += 1
        else:
            cnt = 1
#Making sure the substring is only entered if it is the proper length
        if len(sub) == k:
            string_dict[sub] = cnt
#Returning the length of the dictionary which is equal to the number of unique substrings
    return(float(len(string_dict)))
def possible_substrings(sequence,k):
    '''
This function determines the number of possible substrings of length k in a sequence.
The number of possible substrings is equal to the length of the sequence minus k plus one.
This rule is violated if k is equal to one, in this instance the number of substrings is 4 for the nucelic acids
    '''
#Making sure the the length of the sequence is >= k
    assert len(sequence) >= k, "The sequence should be longer than k"
#If the length of the substring is 1, there are only 4 possible substrings (A,T,C,G) 
    if k==1:
        return(4)
#If the length of the substring is greater than 1 it will be limited by the length of the string 
    else:
#The number of substrings will be the length of the sequence - k-1
        return(float(len(sequence)-(k-1)))
def linguistic_complexity(sequence):
    '''
This function determines linguistic completixty of a sequence.
Linguistic complexity is the proportion of substrings of all sizes that are observed and the possible number of substrings of all sizes
It does so by creating a for loop that iterates a number of times equal to the length of the substring. 
At each iteration it calculates the number of observed substring and the potential number of substrings of that size
At the end of the loop it returns the sum of observed and possible substrings of each possible size
Finally it returns the observed number of substrings/possible number of substrings.
    '''
#Creating variables for observed and possible substrings
    observed = 0
    possible = 0 
#Determining the observed and possible number of substrings for each substring length to determine linguistic complexity
    for i in range(1,len(sequence)+1):
        observed += obs_substrings(sequence, i)
        possible += possible_substrings(sequence, i)
    return(observed/possible)

def test_obs_substrings():
    '''
    Tests if obs_substrings works with a known value.
    '''
    known_string = 'ATTTGGATT'
    if obs_substrings(known_string, 2) != 5:
        assert False
    else:
        assert True

def test_possible_substrings():
    '''
    Tests if possible_substrings works with a known value.
    '''
    known_string = 'ATTTGGATT'
    if possible_substrings(known_string, 2) != 8:
        assert False
    else:
        assert True
        
def test_linguistic_complexity():
    '''
    Tests if linguistic_complexity works with a known value.
    '''
    known_string = 'ATTTGGATT'
    if linguistic_complexity(known_string) != 0.875:
        assert False
    else:
        assert True
        
if __name__ == '__main__':
#Accepting user input for a file of sequences in quotes (e.g 'sample_file.txt')
    file = open(input("Add sequences file in quotes(\'\'):"), 'r').read().split('\n')
#Creating a new file to save the Linguistic Complexity of the sequences and creating a header line, tab separated
    output = open("Linguistic_Completixty.txt", 'w')
    output.write("Sequence\tLinguistic Complexity\n")
#Calculating the linguistic complexity of each sequence at each line and adding it to the output file tab separated
    for i in file:
        output.write("{}\t{}\n".format(i, linguistic_complexity(i)))
    output.close()
