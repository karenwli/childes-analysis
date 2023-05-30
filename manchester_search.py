from multiprocessing import freeze_support
import pylangacq
import json
import mlconjug3
import spacy
    # Run this in terminal for Spanish processing
    # python -m spacy download es_core_news_md

if __name__ == '__main__': 
    freeze_support()

    english_conjugator = mlconjug3.Conjugator(language='en')

    ####### IMPORTING DATA FROM CHILDES ######

    url = "https://childes.talkbank.org/data/Eng-UK/Manchester.zip"

    def import_english_child_dir():
        url = "https://childes.talkbank.org/data/Eng-UK/Manchester.zip"

        english_corpora = pylangacq.read_chat(url)

        return english_corpora

    def import_english_child():
        # ENGLISH DATA
        url = "https://childes.talkbank.org/data/Eng-UK/Manchester.zip"

        english_corpora = pylangacq.read_chat(url)

        return english_corpora
    
    ###
    english_cp_verbs = ['say', 'know', 'think', 'believe', 'suggest', 'find', 'show', 'mean', 'see', 'realize', 
            'note', 'argue', 'indicate', 'feel', 'understand', 'hope', 'report', 'state', 'assume', 'agree', 
            'claim', 'ensure', 'learn', 'remember', 'conclude', 'hear', 'admit', 'notice', 'decide', 'add', 
            'insist', 'recognize', 'tell', 'explain', 'discover', 'reveal', 'prove', 'seem', 'acknowledge', 
            'announce', 'estimate', 'demonstrate', 'write', 'mention', 'imply', 'appear', 'confirm', 
            'imagine', 'require', 'suspect', 'worry', 'forget', 'expect', 'demand', 'determine', 
            'recommend', 'complain', 'assert', 'declare', 'fear', 'predict', 'warn', 'deny', 'ask', 'accept', 
            'doubt', 'observe', 'contend', 'consider', 'maintain', 'guess', 'read', 'wish', 'rule', 
            'emphasize', 'propose', 'pretend', 'use', 'love', 'recall', 'pray', 'suppose', 'allege', 'testify', 
            'figure', 'concede', 'stress', 'speculate', 'guarantee', 'call', 'convince', 
            'promise', 'assure', 'teach']
            # Deleted: "let", "make", "hold", "like" (not a bad CP taking verb, null C is too easily mistaken), "happen", "want?"

    ### TESTING/EXPLORING FUNCTIONS ###

    def print_sample_from(corpus,word):
    # Prints a sample starting from a particular word (helpful for finding a language in biling corpus)

        printing = False
        counter = 0
        found = False

        for token in corpus:
            
            try:
                # Find input word
                if token.word == word and found == False:

                    printing = True
                    found = True
                
                if printing == True and  counter < 10:
                    try:
                        print("word:", token.word + " | " + "part-of-speech tag:", token.pos + "|" + "morph:", token.mor)
                    except TypeError:
                        print("word:", token.word + " | part-of-speech tag: - | morph: -")
                    
                    counter += 1
                elif counter == 10:
                    break
            except AttributeError:
                continue

    def print_thats(corpus):
    # Prints all instances of "that"

        for i , token in enumerate(corpus):

            last_token = corpus[i-1]
            #last_pos = wn.synsets(last_token.word)[0].pos()

            # Print first 60 words
            if i > 0 and i < len(corpus)-4 and token.word == "that" and last_token.pos == "v":

                last_token = corpus[i-1]
                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]


                print(last_token.word, token.word + " ("+ token.pos +")" , token2.word, token3.word, token4.word)

    def count_thinks(corpus):
    # Counts all conjugations of "think"

        counter = 0

        think_string = ""


        for i, token in enumerate(corpus):

            if token.mor == "think":

                last_token = corpus[i-1]
                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]
                token5 = corpus[i+4]

                try:
                    this_ex = last_token.word + " " + token.word + " " + token2.word + " " + token3.word + " "+ token4.word + " " + token5.word
                    print(this_ex)
                    think_string = think_string+ this_ex + "\n"
                except IndexError:
                    think_string = think_string

                counter += 1

        print("Think counter: " + str(counter))

        return think_string

    ### HELPER FUNCTIONS ###
    def is_okay_intermediate(verb, subsequent_tokens):
    # In searching for an embedded finite verb, we need to allow space for an NP (especially in English).
    # Here we allow for 3 tokens between verbs, which should cover an NP
    # This function makes sure that those three (or fewer) intermediates do not contain:
    #   Sentence endings, reduplication, adjectives as an argument, prepositions, wh words, complementizers, or infinitives

        is_okay = True
        subsequent_words= []
        punct_stops = [ ".", "?", ",", "!", "/", "/.", '"/.', "//.","..."]
        eng_stops = ["who", "what", "where", "when", "why", "if", "how"]
        stops = punct_stops + eng_stops

        for token in subsequent_tokens:
            subsequent_words.append(token.mor)

            if token.word in stops:
                # Checks for sentence endings, prepositions, 
                is_okay = False

        #if verb in subsequent_words:
            # Checks for reduplication
        #    is_okay = False
        #elif subsequent_tokens[0].pos in adj_set:
            # Checks for adjective following matrix (particularly important for copula)
        #    is_okay = False
        if "to" in subsequent_words:
            is_okay = False
        elif subsequent_tokens[-1].pos == "inf":
            is_okay = False
        
        return is_okay
        
    ### INTERMEDIATE STEPS ###
    def split_into_children():
    # Takes in array of corpora and returns child utterances separated by age
        
        child_array = ["Anne", "Aran", "Becky", "Carl", "Dominic", "Gail", "Joel", "John", "Liz", "Nick", "Ruth", "Warren"]

        token_array = []

        for child in child_array:

            corpus_array = pylangacq.read_chat(url, child)
            token_array.append(corpus_array.tokens(participants="CHI"))

        print("Anne", len(token_array[0]), ", Aran", len(token_array[1]), ", Becky", len(token_array[2]))

        return token_array
    
    def split_into_ages(corpus_array):
    # Takes in array of corpora and returns child utterances separated by age
        max_age = 4
        token_array = []
        i =0
        while i < max_age:
            token_array.append([])
            i +=1 

        failed_files = 0
        sli_files = 0

        for corpus in corpus_array:
            for i, header in enumerate(corpus.headers()):

                try:
                    # Rule out SLI files
                    if 'SLI' in header['Types']:
                        sli_files += 1
                        continue
                    else:
                        transcript = corpus[i]

                    for participant in header['Participants']:
                        try:
                            part_age = header['Participants'][participant]['age'].split(';')[0]
                            if part_age != "":
                                int_age = int(part_age)

                                if int_age >= max_age:
                                    continue
                                else:
                                    part_tokens = transcript.tokens(participants = participant)
                                    # perhaps add CHI2, I don't remember if they added the age
                                    token_array[int_age] = token_array[int_age] + part_tokens
                            else:
                                continue
                            
                        except TypeError or IndexError or ValueError:
                            continue

                except KeyError or TypeError:
                    # If there's no age info, just skip this file
                    failed_files = failed_files +1
                    continue

        print("Total failed files: " + str(failed_files))
        print("Total SLI files: " + str(sli_files))
        print("1yo:", len(token_array[1]), ", 2yo:", len(token_array[2]), ", 3yo:", len(token_array[3]))

        return token_array

    def adult_split_into_ages(corpus_array): #TODO Make this less clunky

        max_age = 4
        token_array = []
        i =0
        while i < max_age:
            token_array.append([])
            i +=1

        adult_tags = ["MOT", "FAT", "MAD", "PAD", "INV", "ADU"]

        for corpus in corpus_array:
            for transcript in corpus:
                corpus_tokens = []
                for participant in adult_tags:
                    adult_tokens = transcript.tokens(participants=participant)
                    corpus_tokens += adult_tokens

                try:
                    age = transcript.ages(months= True)[0]//12
                    int_age = int(age)

                    if int_age >= max_age:
                        continue
                    else:
                        token_array[int_age] = token_array[int_age] + corpus_tokens
                except TypeError or IndexError or ValueError:
                            continue

        return token_array

    def that_counter(corpus):
    # Counts instances of null and overt "that" in given corpus and returns two dictionaries with those values

        verb_dict = {}
        ambig_nps = []
        bad_nps = [".", "?"]
        counter = 0

        that_counter = 0
        think_string = ""
        emb_verb_types = ["v", "cop", "mod", "aux", "part"]
        np_types = ["n", "pro:sub", "pro:per", "pro:prop", "pro:obj"] # This needs expansion

        ### STEP 1: Search for instances of that [VERB that]
        for i , token in enumerate(corpus):

            if i > 0 and i < len(corpus)-4:

                token_minus2 = corpus[i-2]
                last_token = corpus[i-1]
                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]
                token5 = corpus[i+4]

                #[good_matrix, root] = is_good_matrix_verb(last_token.word,english_cp_conj)

                # Check for sequence VERB that (NP) finiteV
                if token.word == "that" and token.pos == "comp" and last_token.pos == "v" and last_token.mor in english_cp_verbs:

                    embedded_conj_verb = False
                    
                    if is_okay_intermediate(last_token.mor, [token2, token3]) and token3.pos in emb_verb_types:
                        embedded_conj_verb = True
                    elif is_okay_intermediate(last_token.mor, [token2, token3, token4]) and token4.pos in emb_verb_types:
                        embedded_conj_verb = True
                    elif is_okay_intermediate(last_token.mor, [token2, token3, token4, token5]) and token5.pos in emb_verb_types:
                        embedded_conj_verb = True

                    np_subj = False

                    if token_minus2.pos in np_types:
                        np_subj = True
                    elif token_minus2.pos not in bad_nps or ambig_nps:
                        ambig_nps.append(token_minus2.pos)

                        try:
                            print(token_minus2.word + " (" + token_minus2.pos + ")")
                        except TypeError:
                            counter += 1
                            

                    if embedded_conj_verb and np_subj:
                        that_counter += 1

                        try:
                            try:
                                this_ex = ""
                                #this_ex =  last_token.word + " " + token.word + " (" + token.pos + ") " + token2.word + " (" + token2.pos + ") " + token3.word + " (" + token3.pos  + ") "+ token4.word + " (" +token4.pos +")"
                                if token.mor == "think":
                                    this_ex = token_minus2.word + " " + last_token.word + " " + token.word + " " + token2.word + " " + token3.word + " "+ token4.word
                            #print(tokenminus2.word, last_token.word, token.word + " (" + root + ") " + token2.word + " (" + token2.pos + ") " + token3.word + " (" + token3.pos  + ") "+ token4.word + " (" +token4.pos +")")
                                think_string = think_string + this_ex + "\n"
                            except UnicodeEncodeError:
                                think_string = think_string
                        except TypeError:
                            think_string = think_string

                        # Update frequency in verb dictionary
                        if last_token.mor in verb_dict:
                            verb_dict[last_token.mor] += 1
                        else: 
                            verb_dict[last_token.mor] = 1

                    # An earlier version pulled the root from the MOR tier of the token, rather than the conjugated verb dictionary
                    #verb_str = last_token.mor
                    #verb_array = re.split(r'-|&', verb_str)
                    #verb = verb_array[0]
        
        print(verb_dict)

        ### STEP 2: Search for instances of null CP with these same verbs

        null_counter = 0
        null_dict = {}
        null_string = ""
        

        for i, token in enumerate(corpus):

            if i < len(corpus) - 4:

                tokenminus3 = corpus[i-3]
                tokenminus2 = corpus[i-2]
                last_token = corpus[i-1]
                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]
                token5 = corpus[i+4]
                
                #[good_matrix, root] = is_good_matrix_verb(token.word, english_cp_conj)
                
                # Check that verb is in cp-taking verb list
                if token.pos == "v" and token.mor in english_cp_verbs:

                    embedded_conj_verb = False

                    if is_okay_intermediate(token.mor, [token2, token3]) and token3.pos in emb_verb_types:
                        embedded_conj_verb = True
                    elif is_okay_intermediate(token.mor, [token2, token3, token4]) and token4.pos in emb_verb_types:
                        embedded_conj_verb = True
                    elif is_okay_intermediate(token.mor, [token2, token3, token4, token5]) and token5.pos in emb_verb_types:
                        embedded_conj_verb = True

                    np_subj = False

                    if last_token.pos in np_types:
                        np_subj = True
                    elif token_minus2.pos not in bad_nps:
                        bad_nps.append(token_minus2.pos)
                    
                    if embedded_conj_verb and np_subj:
                        null_counter += 1

                        try:
                            try:
                                this_ex = ""
                                #this_ex = last_token.word + " " + token.word + " "+token2.word + " (" + token2.pos + ") " + token3.word + " (" + token3.pos  + ") "+ token4.word + " (" +token4.pos +")"
                            #print(tokenminus2.word, last_token.word, token.word + " (" + root + ") " + token2.word + " (" + token2.pos + ") " + token3.word + " (" + token3.pos  + ") "+ token4.word + " (" +token4.pos +")")
                                if token.mor == "think":
                                    this_ex = last_token.word + " " +token.word + " " + token2.word + " " + token3.word + " "+ token4.word + " " + token5.word
                                think_string = think_string + this_ex + "\n"
                            except UnicodeEncodeError:
                                think_string = think_string
                        except TypeError:
                            think_string = think_string

                        # Update frequency in null dictionary
                        if token.mor in null_dict:
                            null_dict[token.mor] += 1
                        else: 
                            null_dict[token.mor] = 1                        

        print(null_dict)

        print("'That' appeared as a complementizer " + str(that_counter) + " times")
        print("'That' was unpronounced " + str(null_counter) + " times")
        this_analysis = [[verb_dict, null_dict], think_string]
        print(bad_nps)

        return this_analysis

    def combine_age_arrays(age_arrays):
        #age_arrays should come in as [array1[age1, age2, age3...], array2[age1,age2,age3]]

        total_tokens = []
        i = 0
        while i < len(age_arrays[0]):
            total_tokens.append([])
            i += 1
        
        for sub_array in age_arrays:

            for i, age in enumerate(sub_array):
                total_tokens[i] = total_tokens[i] + age
        
        return total_tokens

    def dict_to_csv(cp_verbs, dictionary_array, complementizer, label):
    # Takes array of paired dictionaries and prints them into a summary csv

        filename = label +" "+ complementizer +" manchester.csv"
        group_counter = 3

        # Dictionary array will come in as:
        # dictionary_array[age_group1[verb_dict1, null_dict1], age_group[verb_dict2, null_dict1], etc]

        with open(filename,"w") as outfile:

            ## Write the first line of the csv so we know what we're looking at
            first_line = " ,"

            for age_group in dictionary_array:

                first_line = first_line + "group"+ str(group_counter) + " overt, group" + str(group_counter) + " null, "
                group_counter = group_counter + 1
            
            first_line = first_line + "\n"
            outfile.write(first_line)

            ## Add information to these columns
            for cp_verb in cp_verbs:
                # First column
                verb_line = cp_verb

                for age_group in dictionary_array:

                    overt_col = "n/a"
                    null_col = "n/a"

                    if cp_verb in age_group[0]:
                        overt_col = age_group[0][cp_verb]

                    if cp_verb in age_group[1]:
                        null_col = age_group[1][cp_verb]
            
                    verb_line = verb_line +","+ str(overt_col) +","+ str(null_col)
                
                verb_line = verb_line + "\n"

                #outfile.write(f"{cp_verb},{col2},{col3}\n")
                outfile.write(verb_line)

    ### PRIMARY FUNCTIONS ###
    def that_analysis(age_array, name):

        child_array = ["Anne", "Aran", "Becky", "Carl", "Dominic", "Gail", "Joel", "John", "Liz", "Nick", "Ruth", "Warren"]

        counter = 0

        frequency_array = []

        if len(age_array) > 1:
            counter = 0

        filename = name + " instances of V_CP.txt"
        with open(filename,"w") as outfile:

            for corpus in age_array:

                age_marker = child_array[counter] + "\n"
                print(age_marker)

                [that_counts,think_string] = that_counter(corpus)
                frequency_array.append(that_counts)
                #print(exception_string)

                outfile.write(age_marker + "\n")
                outfile.write(think_string)

                counter = counter +1

        return dict_to_csv(english_cp_verbs, frequency_array, "that", name)


    ### MAIN ####

    english_corpora = import_english_child()
    #english_ages = split_into_ages(english_corpora)
    #manchester = split_into_children()
    #that_analysis(manchester, "manchester separated")
    #print_sample_from(manchester[2], "dog")
    #filename = "manchester_instances_of_think.txt"
    #with open(filename,"w") as outfile:
    #    for age in english_ages:
    #        think_string = count_thinks(age)
    #        outfile.write(think_string)
    english_child_dir = adult_split_into_ages(english_corpora)
    #for age in english_child_dir:
    #    count_thinks(age)
    #that_analysis(english_ages, "child")
    that_analysis(english_child_dir, "child dir")

 
