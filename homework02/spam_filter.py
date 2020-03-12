"""
Ridge DeJong
CS 344
Homework 2.1

This approach is Bayesian because it uses Bayes Rule to calculate the probability of an event (email being spam)
given certain conditions (individual words). The spam probabilities of each individual word are combined to give
the overall spam probability of an email. Words can positively or negatively affect this probability, where good
words reduce the spam probability while bad words increase it.
"""

spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]


# This function returns a dictionary with words as the keys and spam probabilities as the values
def create_probabilityHT(spam, ham):
    # initialize counters for spam and non-spam messages
    nbad = 0
    ngood = 0
    # initialize list to record all unique words used
    allwords = []
    # initialize a dictionary of bad words
    bad = {}
    for phrase in spam:
        nbad += 1
        # count how many times each word is used
        for word in phrase:
            word = word.lower()
            if bool(bad.get(word)):
                bad[word] = bad[word] + 1
            else:
                bad[word] = 1
            if word not in allwords:
                allwords.append(word)
    # initialize a dictionary of good words
    good = {}
    for phrase in ham:
        ngood += 1
        # count how many times each word is used
        for word in phrase:
            word = word.lower()
            if bool(good.get(word)):
                good[word] = good[word] + 1
            else:
                good[word] = 1
            if word not in allwords:
                allwords.append(word)
    # initialize probability dictionary for all unique words
    probabilities = {}
    for word in allwords:
        if bool(good.get(word)):
            # weight good words more than bad words
            g = 2 * good[word]
        else:
            g = 0
        if bool(bad.get(word)):
            b = bad[word]
        else:
            b = 0
        # threshold of 1 so every word is evaluated
        # calculate the probability that a word is spam based on the number of occurrences and number of good
        # and bad messages
        probabilities[word] = max(0.01, min(0.99, min(1.0, b / nbad) / (min(1.0, g / ngood) + min(1.0, b / nbad))))
    return probabilities

# none of our test messages are 15+ words --> use all of them in test
# This function determines the probability that a message is spam based on the individual probability of each
# word being spam
def is_spam(message, dict):
    # keep track of words used so each one is used once
    usedwords = []
    prod = 0
    comp_prod = 0
    first = True
    for word in message:
        word = word.lower()
        if word not in usedwords:
            # first time through loop is different so that you don't multiply by 0
            if first:
                prod = dict[word]
                comp_prod = 1 - prod
                first = False
            else:
                # multiply all the probabilities together
                prod *= dict[word]
                # multiply all the complements together
                comp_prod *= 1 - dict[word]
            usedwords.append(word)
    # calculate combined probability
    if prod / (prod + comp_prod) > 0.9:
        return True
    else:
        return False


hash = create_probabilityHT(spam_corpus, ham_corpus)
test1 = is_spam(spam_corpus[0], hash)
test2 = is_spam(spam_corpus[1], hash)
test3 = is_spam(ham_corpus[0], hash)
test4 = is_spam(ham_corpus[1], hash)

print(hash)
print("First message spam? ", test1)
print("Second message spam? ", test2)
print("Third message spam? ", test3)
print("Fourth message spam? ", test4)