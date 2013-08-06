voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    f = open('voting_record_dump109.txt')
    data = list(f)
    senators = []
    records = []
    for line in data:
        bill_history = list(line.split())
        process_line( bill_history, senators, records)
    return dict(zip(senators,records)) 
    
def process_line( votingHistory, senatorsList, recordsList):
    senatorsList.append(votingHistory[0])
    recordsList.append([int(votingHistory[x]) for x in range(3, len(votingHistory))])

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    return list_dot(voting_dict[sen_a], voting_dict[sen_b])

def list_dot(u,v): return sum([u[i]*v[i] for i in range(len(u))])

## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    setSenators = set( voting_dict.keys() ) - {sen}
    mostAgreeable = 'none'
    mostAgreeableScore = -1000000    
    for x in setSenators:
        agreementScore = policy_compare( x, sen, voting_dict)
        if agreementScore >= mostAgreeableScore:
            mostAgreeable = x
            mostAgreeableScore = agreementScore
    return mostAgreeable

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    setSenators = set( voting_dict.keys() ) - {sen}
    leastAgreeable = 'none'
    leastAgreeableScore = 100000000000
    for x in setSenators:
        agreementScore = policy_compare( x, sen, voting_dict)
        if agreementScore <= leastAgreeableScore:
            leastAgreeable = x
            leastAgreeableScore = agreementScore
    return leastAgreeable

## Task 5

most_like_chafee    = 'Jeffords' # most_similar('Chafee' , voting_dict)
least_like_santorum = 'Feingold' # least_similar('Santorum' , voting_dict)

# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    scores = []
    for x in sen_set:
        scores.append(policy_compare( x, sen, voting_dict))
    return sum(scores)/len(scores)

#apparently ungraded
most_average_Democrat = ... # give the last name (or code that computes the last name)

# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    sen_votes = [voting_dict[x] for x in sen_set]
    return averageVotes(sen_votes)

def averageVotes(listVotes):
    averageScore = []
    numOfVotes = len(listVotes[0])
    numOfSenators = len(listVotes)
    for i in range(numOfVotes):
        averageScore.append(0)
        for j in range(numOfSenators):
            averageScore[i] += listVotes[j][i]
        averageScore[i] = averageScore[i] / numOfSenators
    return averageScore

#democrats = politics_lab.democrats()
#vd = politics_lab.create_voting_dict()
#politics_lab.find_average_record(democrats, vd)

average_Democrat_record = [-0.16279069767441862, -0.23255813953488372, 1.0, 0.8372093023255814, 0.9767441860465116, -0.13953488372093023, -0.9534883720930233, 0.813953488372093, 0.9767441860465116, 0.9767441860465116, 0.9069767441860465, 0.7674418604651163, 0.6744186046511628, 0.9767441860465116, -0.5116279069767442, 0.9302325581395349, 0.9534883720930233, 0.9767441860465116, -0.3953488372093023, 0.9767441860465116, 1.0, 1.0, 1.0, 0.9534883720930233, -0.4883720930232558, 1.0, -0.32558139534883723, -0.06976744186046512, 0.9767441860465116, 0.8604651162790697, 0.9767441860465116, 0.9767441860465116, 1.0, 1.0, 0.9767441860465116, -0.3488372093023256, 0.9767441860465116, -0.4883720930232558, 0.23255813953488372, 0.8837209302325582, 0.4418604651162791, 0.9069767441860465, -0.9069767441860465, 1.0, 0.9069767441860465, -0.3023255813953488] # (give the vector)

#

def democrats():
    f = open('voting_record_dump109.txt')
    data = list(f)
    democrats = set()
    for line in data:
        bill_history = list(line.split())
        if 'D' in bill_history[1]:
            democrats.add(bill_history[0])
    return democrats

#politics_lab.find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
#politics_lab.democrats()

# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    allRivals = { (i,least_similar(i,voting_dict)) for i in voting_dict.keys()}
    lowScore = 100000000000
    sen_a = 'none'
    sen_b = 'none'
    for (x,y) in allRivals:
        agreementScore = policy_compare( x, y, voting_dict)
        if agreementScore < lowScore:
           sen_a = x
           sen_b = y
           lowScore = agreementScore
    return (sen_a, sen_b)
