from multiprocessing import freeze_support
import pylangacq
import json
import mlconjug3
import spacy
    # Run this in terminal for Spanish processing
    # python -m spacy download es_core_news_md

if __name__ == '__main__': 
    freeze_support()

    ###### QUICKSTART TESTING CODE ######
    #data = "*CHI:\tI want cookie .\n*MOT:\tokay ."
    #reader = pylangacq.Reader.from_strs([data])
    #len(reader.utterances())
    #reader.n_files()
    #reader.utterances()
    #reader = pylangacq.Reader.from_strs([eve])

    english_conjugator = mlconjug3.Conjugator(language='en')
    spanish_conjugator = mlconjug3.Conjugator(language='es')

    ####### IMPORTING DATA FROM CHILDES ######
    def import_english_child_dir():
        child_urls = {"https://childes.talkbank.org/data/Eng-NA/Brown.zip", "https://childes.talkbank.org/data/Eng-NA/Bloom.zip",
                        "https://childes.talkbank.org/data/Clinical-MOR/Gillam.zip", "https://childes.talkbank.org/data/Eng-NA/Bohannon.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Gathercole.zip", "https://childes.talkbank.org/data/Eng-NA/Haggerty.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Garvey.zip", "https://childes.talkbank.org/data/Eng-NA/Braunwald.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Warren.zip", "https://childes.talkbank.org/data/Eng-NA/Brent.zip",
                        "https://childes.talkbank.org/access/Eng-NA/Weist.html", "https://childes.talkbank.org/data/Eng-NA/Clark.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Fletcher.zip", "https://childes.talkbank.org/data/Eng-NA/Demetras1.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Wells.zip", "https://childes.talkbank.org/data/Eng-NA/Demetras2.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Tommerdahl.zip", "https://childes.talkbank.org/data/Clinical-MOR/EllisWeismer.zip",
                        "https://childes.talkbank.org/data/Clinical-MOR/Conti/Conti1.zip", "https://childes.talkbank.org/data/Eng-NA/Evans.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Bates.zip", "https://childes.talkbank.org/data/Eng-NA/Feldman.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Bernstein.zip", "https://childes.talkbank.org/data/Eng-NA/Hall.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Bliss.zip", "https://childes.talkbank.org/data/Eng-NA/Higginson.zip",
                        "https://childes.talkbank.org/data/Eng-NA/HSLLD.zip", "https://childes.talkbank.org/data/Eng-NA/Kuczaj.zip",
                        "https://childes.talkbank.org/data/Eng-NA/McCune.zip", "https://childes.talkbank.org/data/Eng-NA/Morisset.zip",
                        "https://asd.talkbank.org/data/English/Nadig.zip", "https://childes.talkbank.org/data/Eng-NA/Nelson.zip",
                        "https://childes.talkbank.org/data/Eng-NA/NewEngland.zip", "https://childes.talkbank.org/data/Eng-NA/NewmanRatner.zip",
                        "https://childes.talkbank.org/data/Clinical-MOR/Nicholas/TD.zip", "https://childes.talkbank.org/data/Eng-NA/Peters.zip",
                        "https://childes.talkbank.org/data/Clinical-MOR/POLER.zip", "https://childes.talkbank.org/data/Eng-NA/Post.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Rollins.zip", "https://childes.talkbank.org/data/Clinical-MOR/Rondal/TD.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Sachs.zip", "https://childes.talkbank.org/data/Eng-NA/Sawyer.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Snow.zip", "https://childes.talkbank.org/data/Eng-NA/Soderstrom.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Sprott.zip", "https://childes.talkbank.org/data/Eng-NA/Suppes.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Tardif.zip", "https://childes.talkbank.org/data/Eng-NA/Valian.zip",
                        "https://childes.talkbank.org/data/Eng-NA/VanHouten.zip", "https://childes.talkbank.org/data/Eng-NA/VanKleeck.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Belfast.zip", "https://childes.talkbank.org/data/Eng-UK/Edinburgh.zip",
                        "https://phon.talkbank.org/data/Eng-UK/Cruttenden.zip", "https://childes.talkbank.org/data/Eng-UK/Forrester.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Howe.zip", "https://childes.talkbank.org/data/Eng-UK/KellyQuigley.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Korman.zip", "https://childes.talkbank.org/data/Eng-UK/Lara.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Manchester.zip", "https://childes.talkbank.org/data/Eng-UK/Nuffield.zip",
                        "https://childes.talkbank.org/data/Eng-UK/OdiaMAIN.zip", "https://asd.talkbank.org/data/English/QuigleyMcNally.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Sekali.zip", "https://phon.talkbank.org/data/Eng-UK/Smith.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Thomas.zip"
                    }

        english_child_dir_corpora = []
        
        for url in child_urls:

            english_child_dir_corpora.append(pylangacq.read_chat(url))

        return english_child_dir_corpora

    def import_english_child():
        # ENGLISH DATA
        child_urls = {"https://childes.talkbank.org/data/Eng-NA/Brown.zip", # 1-5yo, Child: CHI, Adult: MOT, FAT COU, GLO, GAI, MEL, URS, RIC
                        "https://childes.talkbank.org/data/Clinical-MOR/Gillam.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Gathercole.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Garvey.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Warren.zip",
                        "https://childes.talkbank.org/access/Eng-NA/Weist.html",
                        "https://childes.talkbank.org/data/Eng-UK/Fletcher.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Wells.zip",
                        "https://childes.talkbank.org/data/Eng-UK/Tommerdahl.zip",
                        "https://childes.talkbank.org/data/Clinical-MOR/Conti/Conti1.zip",
                        "https://childes.talkbank.org/data/Clinical-MOR/ENNI.zip",
                        "https://childes.talkbank.org/data/Clinical-MOR/UCSD.zip",
                        "https://childes.talkbank.org/data/Clinical-MOR/Rondal/TD.zip",
                        "https://childes.talkbank.org/data/Clinical-MOR/Nicholas/TD.zip",
                        "https://childes.talkbank.org/data/Eng-NA/Bliss.zip"
                    }

        english_child_corpora = []
        
        for url in child_urls:

            english_child_corpora.append(pylangacq.read_chat(url))
        
        #english_child_corpora = [brown, gillam, gathercole, garvey, warren, weist, fletcher, wells, tommerdahl, conti]

        return english_child_corpora

    def import_biling_child():
        # BILINGUAL DATA
        perez_url = "https://childes.talkbank.org/data/Biling/Perez.zip"
        perez = pylangacq.read_chat(perez_url)
        perez_tokens = perez.tokens(participants="CHI")
        # not POS notated

        reyes_url = "https://childes.talkbank.org/data/Biling/Reyes.zip"
        reyes = pylangacq.read_chat(reyes_url)
        # annotated, not labelled as CHI

        deuchar_url = "https://childes.talkbank.org/data/Biling/Deuchar.zip"
        deuchar = pylangacq.read_chat(deuchar_url)

        silva_url = "https://childes.talkbank.org/data/Biling/SilvaCorvalan.zip"
        silva = pylangacq.read_chat(silva_url)

        fuertes_url = "https://childes.talkbank.org/data/Biling/FerFuLice.zip"
        fuertes = pylangacq.read_chat(fuertes_url)
        # POS annotated

        biling_child_corpora = [fuertes, perez, silva, deuchar]

        url_list = ["https://childes.talkbank.org/data/Biling/Perez.zip",
                    "https://childes.talkbank.org/data/Frogs/Spanish-MiamiBiling.zip"
                    ] 

        unannotated_list = []
        
        for url in url_list:

            unannotated_list.append(pylangacq.read_chat(url))

        return [biling_child_corpora, unannotated_list]
    
    def import_biling_adult():
        # BILINGUAL ADULT DATA

        miami_url = "https://biling.talkbank.org/data/Bangor/Miami.zip"
        miami = pylangacq.read_chat(miami_url)

        return miami

    def import_spanish_child():
        # SPANISH MONO CHILD DATA

        marrero_url = "https://childes.talkbank.org/data/Spanish/Marrero.zip"
        # Annotated, 3-4yo
        # Child: CHI, Adult: TOY, MJO (investigators), TAN, TNI, JOS
        marrero = pylangacq.read_chat(marrero_url)

        hess_url = "https://childes.talkbank.org/data/Spanish/Hess.zip"
        # Annotated, 6, 9, 12 yo
        # Child: CHI, Adult: KAR
        hess = pylangacq.read_chat(hess_url)

        koine_url = "https://phon.talkbank.org/data/Spanish/Koine.zip"
        # Annotated, 3 yo
        # Child: IAG, RIC, ART, Adult: MON 
        koine = pylangacq.read_chat(koine_url)

        aguilar_url = "https://childes.talkbank.org/data/Frogs/Spanish-Aguilar.zip"
        # Annotated, 6 & 12 yo
        # Child: CHI, Adult: CES
        aguilar = pylangacq.read_chat(aguilar_url)

        fernaguado_url = "https://childes.talkbank.org/data/Spanish/FernAguado.zip"
        # Annotated, 3 & 4 yo
        # Child: CHI, Adult: MOT, INV, misc older siblings with ages specified
        fernaguado = pylangacq.read_chat(fernaguado_url)

        colmex_url = "https://childes.talkbank.org/data/Spanish/ColMex.zip" #6-7, annotated
        # Annotated, 6 & 7 yo
        # Child: CHI, Adult: INV
        colmex = pylangacq.read_chat(colmex_url)

        url_list = ["https://childes.talkbank.org/data/Spanish/BecaCESNo.zip", # 3-11, Child: CHI, Adult: MOT, PAT, AUN, INT, EXP, PAU? (too much overlap)
                    "https://childes.talkbank.org/data/Spanish/DiezItza.zip", # 3yo, Child: CHI, Adult: MOT, INV
                    "https://childes.talkbank.org/data/Frogs/Spanish-Ornat.zip", # 3-5, 8, Child: CHI
                    "https://childes.talkbank.org/data/Spanish/Shiro.zip", # annotated
                    "https://childes.talkbank.org/data/Frogs/Spanish-Sebastian.zip"] # 3-5, 9, 20, CHI: CHI

        unannotated_list = []
        
        for url in url_list:

            unannotated_list.append(pylangacq.read_chat(url))
        

        spanish_child_corpora = [marrero, hess, aguilar,colmex,koine, fernaguado]

        return [spanish_child_corpora, unannotated_list]

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

    spanish_cp_verbs = ['decir', 'ser', 'asegurar', 'creer', 'saber', 'contar', 'señalar', 'afirmar', 'pensar', 
            'recordar', 'indicar', 'explicar', 'querer', 'aclarar', 'comentar', 'esperar', 'ver', 'revelar', 
            'agregar', 'parecer', 'hacer','manifestar', 'confesar', 'demostrar', 'considerar', 'sostener', 
            'sentir', 'entender', 'reconocer', 'confirmar', 'declarar', 'descubrir', 'argumentar', 'informar',
            'añadir', 'mencionar', 'responder', 'alegar', 'destacar', 'relatar', 'admitir', 'suponer', 'dejar',
            'gustar', 'conocer', 'negar', 'expresar', 'evitar', 'anunciar', 'significar', 'permitir', 'enterar', 
            'imaginar', 'denunciar', 'notar', 'sospechar', 'decidir', 'aceptar', 'determinar', 'precisar', 
            'resultar', 'aprovechar', 'mostrar', 'recalcar', 'advertir', 'detallar', 'olvidar', 'lograr', 'impedir',
            'reiterar', 'provocar', 'referir', 'comprobar', 'pedir', 'resaltar', 'apuntar', 'subrayar', 'sugerir',
            'contestar', 'aseverar', 'establecer', 'escuchar', 'insinuar', 'acordar', 'descartar', 'remarcar', 
            'presumir', 'probar', 'asumir', 'enfatizar', 'narrar', 'desear', 'temer', 'lamentar', 'importar',
            'aducir', 'defender', 'conseguir', 'desmentir']
            # Deleted: "poder"

    ### TESTING/EXPLORING FUNCTIONS ###
    def print_sample(corpus):
    # Prints sample of corpus, change i to specify length of sample

        for i , token in enumerate(corpus):

            # Print first 10 words
            if i < 10:

                print("word:", token.word + " | " + "part-of-speech tag:", token.pos + "|" + "morph:", token.mor)

    def print_sample_from(corpus,word):
    # Prints a sample starting from a particular word (helpful for finding a language in biling corpus)

        printing = False
        counter = 0
        found = False

        # Reference for syntax to call these attributes
        #print("~~" + english_child_tokens[i-1].word + " " + english_child_tokens[i].word + " " + english_child_tokens[i+1].word)
        #print("word:", english_child_tokens[i-1].mor + " | " + "part-of-speech tag:", english_child_tokens[i-1].pos)
        #print("word:", token.word + " | " + "part-of-speech tag:", token.pos)
        #print("word:", english_child_tokens[i+1].word + " | " + "part-of-speech tag:", english_child_tokens[i+1].pos)
        #print("morphological information:", token.mor)
        #print("grammatical relation:", token.gra) 

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

    def print_ques(corpus):
    # Prints all instances of "que"

        for i , token in enumerate(corpus):

            last_token = corpus[i-1]
            #last_pos = wn.synsets(last_token.word)[0].pos()

            # Print first 60 words
            if i > 0 and i < len(corpus)-4 and token.word == "que":

                last_token = corpus[i-1]
                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]


                try:              
                    print(last_token.word, token.word + " (" + token.pos + ") ", token2.word, token3.word, token4.word) 

                except TypeError:
                    print(last_token.word, token.word + " (-) ", token2.word, token3.word, token4.word)

    def print_que_cs(corpus):
    # Prints all instances of "que" where "que" is labelled as a complementizer

        for i , token in enumerate(corpus):

            last_token = corpus[i-1]
            matrix_pos = ["cop", "v","inf"]
            embedded_pos = ["cop", "v"]

            # Find a que
            if i > 0 and i < len(corpus)-4 and token.word == "que":

                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]

                try:
                    last_pos = last_token.pos.split("|")[0]
                    next_pos = token2.pos.split("|")[0]
                    third_pos = token3.pos.split("|")[0]
                    fourth_pos = token4.pos.split("|")[0]
                except AttributeError:
                    continue

                embedded_conj_verb = False

                # Want to make sure the next verb isn't an infinitive
                if next_pos in embedded_pos:
                    embedded_conj_verb = True
                elif next_pos != "inf" and third_pos in embedded_pos:
                    embedded_conj_verb = True
                elif next_pos != "inf" and third_pos != "inf" and fourth_pos in embedded_pos:
                    embedded_conj_verb = True
                    

                if last_pos in matrix_pos and embedded_conj_verb == True:
                    try:              
                        print(last_token.word, token.word + " (" + token.pos + ") ", token2.word, token3.word, token4.word) 

                    except TypeError:
                        print(last_token.word, token.word + " (-) ", token2.word, token3.word, token4.word)

    def print_null_ques(corpus):
    # Prints instances of null "que"

        for i , token in enumerate(corpus):

            matrix_pos = ["cop", "v","inf"]
            embedded_pos = ["cop", "v"]

            # Find a que
            if i > 0 and i < len(corpus)-4 and token.pos in matrix_pos:

                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]

                try:
                    next_pos = token2.pos.split("|")[0]
                    third_pos = token3.pos.split("|")[0]
                    fourth_pos = token4.pos.split("|")[0]
                except AttributeError:
                    continue

                embedded_conj_verb = False

                # Want to make sure the next verb isn't an infinitive
                if next_pos in embedded_pos:
                    embedded_conj_verb = True
                elif next_pos != "inf" and third_pos in embedded_pos:
                    embedded_conj_verb = True
                elif next_pos != "inf" and third_pos != "inf" and fourth_pos in embedded_pos:
                    embedded_conj_verb = True
                    

                if token.pos in matrix_pos and embedded_conj_verb == True:
                    try:              
                        print(token.word, token2.word, token3.word, token4.word) 

                    except TypeError:
                        print(token.word, token2.word, token3.word, token4.word)

    def print_conjugations(conjugator, verb):
        # This is basically from the mlconjug3 example

        test_verb = conjugator.conjugate(verb)
        all_conjugated_forms = test_verb.iterate()
        print(all_conjugated_forms)

    ### HELPER FUNCTIONS ###
    def expand_cp_verbs(verb_array, conjugator):        

        cp_conjugations = {}
        
        bad_verbs = ["me", "mí", "sí", "se"]
        # these are most commonly used as clitics, but mostrar conjugates to me apparently?

        for verb in verb_array:

            this_verb = conjugator.conjugate(verb)
            conjugated_forms = this_verb.iterate()
            cp_conjugations[verb] = [verb]

            for form in conjugated_forms:
                #print(form)
                try:
                    token = form[3]
                except IndexError:
                    #sometimes for the infinitive the tuples are shorter-- we are contributing inifinitive so don't need it
                    continue

                if token in cp_conjugations[verb] or token in bad_verbs:
                    continue

                ## This covers both Spanish and English
                elif str(form[0])[0:6] == "indica" or str(form[0])[0:6] == "Indica":
                    cp_conjugations[verb].append(token)
                else:
                    continue

        return cp_conjugations
    
    def is_okay_intermediate(verb, subsequent_tokens):
    # In searching for an embedded finite verb, we need to allow space for an NP (especially in English).
    # Here we allow for 3 tokens between verbs, which should cover an NP
    # This function makes sure that those three (or fewer) intermediates do not contain:
    #   Sentence endings, reduplication, adjectives as an argument, prepositions, wh words, complementizers, or infinitives

        is_okay = True
        subsequent_words= []
        punct_stops = [ ".", "?", ",", "!", "/", "/.", '"/.', "//.","..."]
        spa_stops = ["que", "qué", "o", "y", "pero", "dónde", "cómo", "más", "cuándo", "donde", "cuando", "como", "mas","sí", "si", "quién", "cuánto", "porqué","porque", "de","cual", "cuántas", "cuántos", "pues"]
        eng_stops = ["who", "what", "where", "when", "why", "if", "how", "that", "because"]
        # Consider adding ahora, as and adjectives after ser
        indef_stops = ["para", "así"]
        stops = punct_stops + spa_stops + indef_stops + eng_stops

        for token in subsequent_tokens:
            subsequent_words.append(token.word)

            if token.word in stops:
                # Checks for sentence endings, prepositions, 
                is_okay = False

        adj_set = ["ADJ", "Adj", "adj"]
        if verb in subsequent_words:
            # Checks for reduplication
            is_okay = False
        elif subsequent_tokens[0].pos in adj_set:
            # Checks for adjective following matrix (particularly important for copula)
            is_okay = False
        elif "to" in subsequent_words:
            is_okay = False
        elif subsequent_tokens[-1].pos == "inf":
            is_okay = False
        
        return is_okay

    def is_good_matrix_verb(token, verb_conj):

        is_good = False
        verb_root = "-"

        for root in verb_conj:
            #print(spanish_cp_conj)
            
            if token in verb_conj[root]:
                is_good = True
                verb_root = root

                return [is_good, verb_root]

        return [is_good, verb_root]
    
    def good_embedded_verb(token):

        infinitive_endings = ["rlo", "rla", "rle", "rlos", "rlas", "rles","rte", "rme", "rse", "ando", "rnos"]
        bad_verbs = ["este", "corta", "corto", "larga", "nada", "completo", "completa", "cumple", "llama", "duro", "tardes", "colores", "//.", "poque", "polque", "corriendo", "daño", "vale", "iguales"]

        good_verb = False

        if token.pos == "v":
            good_verb = True

        if str(token.word)[-1] == "r":
            good_verb = False
        elif str(token.word)[-3:-1] in infinitive_endings:
            good_verb = False
        elif str(token.word)[-4:-1] in infinitive_endings:
            good_verb = False
        elif str(token.word)[-5:-1] in infinitive_endings:
            good_verb = False
        elif token.word in bad_verbs:
            good_verb = False
        
        return good_verb

        
    ### INTERMEDIATE STEPS ###
    def split_into_ages(corpus_array):
    # Takes in array of corpora and returns child utterances separated by age
        max_age = 11
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

                except TypeError:
                    # If there's no age info, just skip this file
                    failed_files = failed_files +1
                    continue

        print("Total failed files: " + str(failed_files))
        print("Total SLI files: " + str(sli_files))
        print("3yo:", len(token_array[3]), ", 4yo:", len(token_array[4]), ", 5yo:", len(token_array[5]))

        return token_array

    def adult_split_into_ages(corpus_array): #TODO Make this less clunky
        infants = []
        one_yos = []
        two_yos = []
        three_yos= []
        four_yos = []
        five_yos = []
        six_yos = []
        older_kids = []

        for corpus in corpus_array:
            for transcript in corpus:

                try:
                    # Sorting subsequent files into 3yo, 4yo, 5yo, and above
                    if transcript.ages(months = True)[0] < 12:
                        infants.append(transcript)
                    elif transcript.ages(months = True)[0] < 24:
                        one_yos.append(transcript)
                    elif transcript.ages(months = True)[0] < 36:
                        two_yos.append(transcript)
                    elif transcript.ages(months = True)[0] < 48:
                        three_yos.append(transcript)
                    elif transcript.ages(months = True)[0] < 60:
                        four_yos.append(transcript)
                    elif transcript.ages(months = True)[0] < 72:
                        five_yos.append(transcript)
                    elif transcript.ages(months = True)[0] < 84:
                        six_yos.append(transcript)
                    elif transcript.ages(months = True)[0] >= 84:
                        older_kids.append(transcript)

                except TypeError:
                    # If there's no age info, just skip this file
                    continue

        infant_tokens = []
        one_yo_tokens = []
        two_yo_tokens = []
        three_yo_tokens = []
        four_yo_tokens = []
        five_yo_tokens = []
        six_yo_tokens = []
        older_kids_tokens = []

        for transcript in infants:
            mot = transcript.tokens(participants="MOT")
            fat = transcript.tokens(participants="FAT")
            inv = transcript.tokens(participants ="INV")
            transcript_tokens = mot + fat + inv
            infant_tokens = infant_tokens + transcript_tokens

        for transcript in one_yos:
            mot = transcript.tokens(participants="MOT")
            fat = transcript.tokens(participants="FAT")
            inv = transcript.tokens(participants ="INV")
            transcript_tokens = mot + fat + inv
            one_yo_tokens = one_yo_tokens + transcript_tokens

        for transcript in two_yos:
            mot = transcript.tokens(participants="MOT")
            fat = transcript.tokens(participants="FAT")
            inv = transcript.tokens(participants ="INV")
            transcript_tokens = mot + fat + inv
            two_yo_tokens = two_yo_tokens + transcript_tokens

        for transcript in three_yos:
            mot = transcript.tokens(participants="MOT")
            fat = transcript.tokens(participants="FAT")
            inv = transcript.tokens(participants ="INV")
            transcript_tokens = mot + fat + inv
            three_yo_tokens = three_yo_tokens + transcript_tokens

        for transcript in four_yos:
            mot = transcript.tokens(participants="MOT")
            fat = transcript.tokens(participants="FAT")
            inv = transcript.tokens(participants ="INV")
            transcript_tokens = mot + fat + inv
            four_yo_tokens = four_yo_tokens + transcript_tokens

        for transcript in five_yos:
            mot = transcript.tokens(participants="MOT")
            fat = transcript.tokens(participants="FAT")
            inv = transcript.tokens(participants ="INV")
            transcript_tokens = mot + fat + inv
            five_yo_tokens = five_yo_tokens + transcript_tokens

        for transcript in six_yos:
            mot = transcript.tokens(participants="MOT")
            fat = transcript.tokens(participants="FAT")
            inv = transcript.tokens(participants ="INV")
            transcript_tokens = mot + fat + inv
            six_yo_tokens = six_yo_tokens + transcript_tokens

        for transcript in older_kids:
            mot = transcript.tokens(participants="MOT")
            fat = transcript.tokens(participants="FAT")
            inv = transcript.tokens(participants ="INV")
            transcript_tokens = mot + fat + inv
            older_kids_tokens = older_kids_tokens + transcript_tokens

        age_arrays = [infant_tokens, one_yo_tokens, two_yo_tokens, three_yo_tokens, four_yo_tokens, five_yo_tokens, six_yo_tokens, older_kids_tokens]

        return age_arrays

    def annotate_corpus(corpus_array, participant = "child"):
        
        if participant == "child":
            age_corpora = split_into_ages(corpus_array)
        elif participant == "adult":
            age_corpora = adult_split_into_ages(corpus_array)

        nlp = spacy.load('es_core_news_md')

        new_token_array = []
        corpus_counter = 0

        for corpus in age_corpora:

            # STEP 1: CONVERT TOKENS TO STRING AND RUN SPACY
            filestring = ""
            for token in corpus:
                filestring = filestring + token.word + " "


            document = nlp(filestring)
            converted_tokens = []

            # STEP 2: CONVERT BACK TO CHAT FORMAT
            for token in document:

                # I want the pos tagging to be the same as CHAT format
                pos = token.pos_

                infinitive_endings = ["rlo", "rla", "rle", "rlos", "rlas", "rles","rte", "rme", "rse", "ando"]

                if token.pos_ == "VERB":
                    if str(token.text)[-1] == "r":
                        pos = "inf"
                    elif str(token.text)[-3:-1] in infinitive_endings:
                        pos = "inf"
                    elif str(token.text)[-4:-1] in infinitive_endings:
                        pos = "inf"
                    elif str(token.text)[-5:-1] in infinitive_endings:
                        pos = "prog" 
                    else:
                        pos = "v"

                newToken = pylangacq.objects.Token(token.text, pos, token.tag_, (0,0,token.dep_))

                converted_tokens.append(newToken)

            #print_sample(converted_tokens)

            new_token_array.append(converted_tokens)

            corpus_counter += 1
        
        return new_token_array

    def that_counter(corpus):
    # Counts instances of null and overt "that" in given corpus and returns two dictionaries with those values

        verb_dict = {}
        that_counter = 0

        ### STEP 1: Search for instances of that [VERB that]
        for i , token in enumerate(corpus):

            if i > 0 and i < len(corpus)-4:

                last_token = corpus[i-1]
                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]
                token5 = corpus[i+4]

                [good_matrix, root] = is_good_matrix_verb(last_token.word,english_cp_conj)

                # Check for sequence VERB that (NP) finiteV
                if token.word == "that" and last_token.pos == "v" and  good_matrix:

                    embedded_conj_verb = False
                    
                    if is_okay_intermediate(last_token.word, [token2]) and token2.pos == "v":
                        embedded_conj_verb = True
                    elif is_okay_intermediate(last_token.word, [token2, token3]) and token3.pos == "v":
                        embedded_conj_verb = True
                    elif is_okay_intermediate(last_token.word, [token2, token3, token4]) and token4.pos == "v":
                        embedded_conj_verb = True
                    elif is_okay_intermediate(last_token.word, [token2, token3, token4, token5]) and token5.pos == "v":
                        embedded_conj_verb = True

                    if embedded_conj_verb == True:
                        that_counter += 1

                        # Update frequency in verb dictionary
                        if root in verb_dict:
                            verb_dict[root] += 1
                        else: 
                            verb_dict[root] = 1

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
                
                [good_matrix, root] = is_good_matrix_verb(token.word, english_cp_conj)
                
                # Check that verb is in cp-taking verb list
                if good_matrix and token.pos == "v":

                    embedded_conj_verb = False
                    
                    if is_okay_intermediate(token.word, [token2]) and token2.pos == "v":
                        embedded_conj_verb = True
                    elif is_okay_intermediate(token.word, [token2, token3]) and token3.pos == "v":
                        embedded_conj_verb = True
                    elif is_okay_intermediate(token.word, [token2, token3, token4]) and token4.pos == "v":
                        embedded_conj_verb = True
                    elif is_okay_intermediate(token.word, [token2, token3, token4, token5]) and token5.pos == "v":
                        embedded_conj_verb = True

                    if embedded_conj_verb:
                        null_counter += 1

                        try:
                            if root != "say":
                                try:
                                    this_ex = tokenminus3.word + " " + tokenminus2.word + " " + last_token.word + " " + token.word + " (" + root + ") " + token2.word + " (" + token2.pos + ") " + token3.word + " (" + token3.pos  + ") "+ token4.word + " (" +token4.pos +")"
                                #print(tokenminus2.word, last_token.word, token.word + " (" + root + ") " + token2.word + " (" + token2.pos + ") " + token3.word + " (" + token3.pos  + ") "+ token4.word + " (" +token4.pos +")")
                                    null_string = null_string + this_ex + "\n"
                                except UnicodeEncodeError:
                                    null_string = null_string
                        except TypeError:
                            null_string = null_string

                        # Update frequency in null dictionary
                        if root in null_dict:
                            null_dict[root] += 1
                        else: 
                            null_dict[root] = 1                        

        print(null_dict)

        print("'That' appeared as a complementizer " + str(that_counter) + " times")
        print("'That' was unpronounced " + str(null_counter) + " times")
        this_analysis = [[verb_dict, null_dict], null_string]

        return this_analysis
    
    def que_counter(corpus):
    # Counts instances of null and overt "que" in given corpus and returns two dictionaries with those values

        verb_dict = {}
        que_counter = 0

        ques = ["que", "qué" ]
        bad_predecessors = ["el", "este", "si", "que"]

        ### STEP 1: Search for instances of that [VERB que ...VERB]
        ## Excluding infinitives 
        for i , token in enumerate(corpus):

            last_token = corpus[i-1]
            
            # Find a que
            [good_matrix, root] = is_good_matrix_verb(last_token.word, spanish_cp_conj)

            if i > 0 and i < len(corpus)-4 and token.word in ques and good_matrix:
                
                tokenminus2 = corpus[i-2]
                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]
                token5 = corpus[i+4]

                embedded_conj_verb = False

                # Want to make sure the next verb isn't an infinitive
                if tokenminus2.word in bad_predecessors:
                    embedded_conj_verb = False
                elif is_okay_intermediate(last_token.word, [token2]) and good_embedded_verb(token2):
                    embedded_conj_verb = True
                elif is_okay_intermediate(last_token.word, [token2, token3]) and good_embedded_verb(token3):
                    embedded_conj_verb = True
                elif is_okay_intermediate(last_token.word, [token2, token3, token4]) and good_embedded_verb(token4):
                    embedded_conj_verb = True
                elif is_okay_intermediate(last_token.word, [token2, token3, token4, token5]) and good_embedded_verb(token5):
                    embedded_conj_verb = True
                    

                if embedded_conj_verb:
                    que_counter += 1

                    # Update frequency in verb dictionary
                    if root in verb_dict:
                        verb_dict[root] += 1
                    else: 
                        verb_dict[root] = 1
        
        print(verb_dict)

        ### STEP 2: Search for instances of null CP with these same verbs

        null_counter = 0
        null_dict = {}
        null_string = ""

        for i, token in enumerate(corpus):

            [good_matrix, root] = is_good_matrix_verb(token.word, spanish_cp_conj)
            #print(token.word + root)

            if i < len(corpus) - 4 and good_matrix:

                tokenminus3 = corpus[i-3]
                tokenminus2 = corpus[i-2]
                last_token = corpus[i-1]
                token2 = corpus[i+1]
                token3 = corpus[i+2]
                token4 = corpus[i+3]
                token5 = corpus[i+4]

                embedded_conj_verb = False

                # Want to make sure the next verb isn't an infinitive
                if last_token.word == "que" or last_token.word in bad_predecessors:
                    embedded_conj_verb= False
                elif is_okay_intermediate(token.word, [token2]) and good_embedded_verb(token2):
                    embedded_conj_verb = True
                elif is_okay_intermediate(token.word, [token2, token3]) and good_embedded_verb(token3):
                    embedded_conj_verb = True
                elif is_okay_intermediate(token.word, [token2, token3, token4]) and good_embedded_verb(token4):
                    embedded_conj_verb = True
                elif is_okay_intermediate(token.word, [token2, token3, token4, token5]) and good_embedded_verb(token5):
                    embedded_conj_verb = True

                if embedded_conj_verb == True:
                    null_counter += 1

                    if root != "decir":
                        this_ex = tokenminus3.word + " " + tokenminus2.word + " " + last_token.word + " " + token.word + " (" + root + ") " + token2.word + " (" + token2.pos + ") " + token3.word + " (" + token3.pos  + ") "+ token4.word + " (" +token4.pos +")"
                        #print(tokenminus2.word, last_token.word, token.word + " (" + root + ") " + token2.word + " (" + token2.pos + ") " + token3.word + " (" + token3.pos  + ") "+ token4.word + " (" +token4.pos +")")
                        null_string = null_string + this_ex + "\n"

                    # Update frequency in verb dictionary
                    if root in null_dict:
                        null_dict[root] += 1
                    else: 
                        null_dict[root] = 1

        print(null_dict)        

        print("'Que' appeared as a complementizer " + str(que_counter) + " times")
        print("'Que' was unpronounced " + str(null_counter) + " times") 
        this_analysis = [[verb_dict, null_dict], null_string]

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

        filename = label +" "+ complementizer +" frequency_array.csv"
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

        counter = 0

        frequency_array = []

        if len(age_array) > 1:
            counter = 0

        filename = name + " instances of null that.txt"
        with open(filename,"w") as outfile:

            for corpus in age_array:

                age_marker = str(counter) + "yo--- \n"
                print(age_marker)

                [that_counts,exception_string] = that_counter(corpus)
                frequency_array.append(that_counts)
                #print(exception_string)

                outfile.write(age_marker + "\n")
                outfile.write(exception_string)

                counter = counter +1

        return dict_to_csv(english_cp_verbs, frequency_array, "that", name)
    
    def que_analysis(age_array, name):
        ## If not splitting, submit list of tokens to corpus
        ## If splitting, submit array of corpora
        ## This is b/c the corpora contain age info that we still need 
        ## TODO: Make this not a problem haha

        counter = 0

        frequency_array = []

        if len(age_array) > 1:
            counter = 0

        filename = name + " instances of null que.txt"
        with open(filename,"w") as outfile:

            for corpus in age_array:

                age_marker = str(counter) + "yo---"
                print(age_marker)

                [que_counts, exception_string] = que_counter(corpus)
                frequency_array.append(que_counts)
                #print(exception_string)

                outfile.write(age_marker + "\n")
                outfile.write(exception_string)

                counter = counter +1

        return dict_to_csv(spanish_cp_verbs, frequency_array, "que", name)


    ### MAIN ####

    with open("spa_conj", 'r') as f:
        spanish_cp_conj = json.load(f)


    #spanish_cp_conj = expand_cp_verbs(spanish_cp_verbs, spanish_conjugator)
    #with open("spa_conj", 'w') as f:
    #    f.write(json.dumps(spanish_cp_conj, indent=4))
    #print(english_cp_conj)
    #english_corpora = import_english_child()
    #english_ages = split_into_ages(english_corpora)
    #english_child_dir = adult_split_into_ages(english_corpora)
    #that_analysis(english_ages, "child")

    # specific setup so we're not loading everything every time
    #spanish_cp_conj = expand_cp_verbs(spanish_cp_verbs, spanish_conjugator)
    [spanish_child_corpora, beca] = import_spanish_child()
    #[biling_child_corpora, unannotated_biling] = import_biling_child()
    #biling_annotated = annotate_corpus(unannotated_biling)
    #biling_ages = split_into_ages(biling_child_corpora)
    #total_biling_child = combine_age_arrcdays([biling_ages, biling_annotated])
    #que_analysis(total_biling_child, "total biling")
    #that_analysis(total_biling_child, "total biling")


    # Child data
    beca_annotated = annotate_corpus(beca)
    spanish_ages = split_into_ages(spanish_child_corpora)
    total_spanish_child = combine_age_arrays([beca_annotated, spanish_ages])
    #que_analysis(spanish_ages, "spanish child")
    que_analysis(total_spanish_child, "total spanish child")

    # Child directed data
    #child_dir_spanish = adult_split_into_ages(spanish_child_corpora)
    #child_dir_unannotated = annotate_corpus(beca, "adult")
    #total_spanish_child_dir = combine_age_arrays([child_dir_spanish, child_dir_unannotated])
    #que_analysis(total_spanish_child_dir, "total child dir")
