# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 23:13:41 2025

@author: sudha
"""
import spacy
import json
import numpy as np
import time

nlp = spacy.load("en_core_web_lg")


class SimilarityParser:
    
    def __init__(self,word):
        self.word = word

        with open(r"C:\Users\sudha\Desktop\dhanush\Personal DS\NLP/word_prob_json.json","r",encoding="utf-8") as f:
            words_dict = json.load(f)
            f.close()
            
        self.words_dict = words_dict["word_dict"]
        
    def pre_vectorize(self,words):
        word_vectors = np.array([nlp.vocab[word].vectors.reshape(-1,1) for word in words]) 
        
    def find_similarity_spacy(self,word,no_of_words):
        
        word = np.array(nlp.vocab[word].vector.reshape(1,-1))
        similar_words = nlp.vocab.vectors.most_similar(word,n=no_of_words)
        similar_words = [nlp.vocab.strings[word_vec] for word_vec in similar_words[0][0]]
        return similar_words
        
        
    def find_similarity_og(self,word):
        
        words = self.load_words()
        word_vectors = self.pre_vectorize(words)
        word_vec = nlp.vocab.vectors[word]
        
        
# example usage
class WordOps:
    
    def __init__(self,word):
        self.word = word
        
    def deletion(self):
        
        new_words = []
        start_ind = 0
        new_words += [self.word]
        while True:
            for word in new_words[start_ind:]:
                sub_words = []
                for i in range(0,len(word)):
                    sub_words += [(word[0:i]+word[i+1:])]
                start_ind = len(new_words)
                print(sub_words)
                print("new start_ind: ",start_ind)
                new_words += sub_words
                if len(sub_words[0])==1:
                    print("done with deletion op...")
                    print(list(set(new_words)))
                    return list(set(new_words))
            
            
    def replace(self):
        start_ascii = ord('a')
        char_list = [chr(start_ascii+i) for i in range(0,26)]
        new_words = []
        for i in range(0,len(self.word)):
            # replace the ith letter with a-z
            for char in char_list:
                new_words += [(self.word[0:i]+char+self.word[i+1:])]
        return new_words        
    
    
    def swapping(self):
        start_ind = 0 
        new_words=[self.word]
        all_words = [self.word]
        while len(new_words)!=0:
            swapped_words = []
            for word in new_words:
                print(word) 
                # perform swapping
                for i in range(0,len(word)):
                    for j in range(0,len(word)):
                        if i!=j:
                            if i<j:
                                swapped_words += [(word[0:i]+word[j]+word[i+1:j]+word[i]+word[j+1:])]
                            else:
                                swapped_words += [(word[0:j]+word[i]+word[j+1:i]+word[j]+word[i+1:])]
            new_words = [word for word in swapped_words if word not in all_words]
            if len(new_words) == 0:
                print("all combinations found !!")
                print(new_words)
                all_words += new_words
                
            else:
                new_words = list(set(new_words))
                start_ind = len(all_words) 
                all_words += new_words 
                print("new new_words: ",new_words)
                
        all_words.sort()
        return all_words
                    
                   
    def addition(self):
        start_ascii = ord('a')
        char_list = [chr(start_ascii+i) for i in range(0,26)]
        all_words = [self.word]
        for i in range(0,len(self.word)):
            new_words = [(self.word[0:i] + (char) + (self.word[i:])) for char in char_list]
        all_words += new_words
        return all_words
        
    
    def perform_all_ops(self):
        possible_words = []
        possible_words += self.deletion()
        possible_words += self.replace()
        possible_words += self.swapping()
        possible_words += self.addition()
        
        print(possible_words)
        return possible_words
        
        

class SpellSuggestion(SimilarityParser,WordOps) :
    
    def __init__(self,word,no_of_suggestions):
        SimilarityParser.__init__(self,word)
        WordOps.__init__( self,word)
        self.no_of_suggestions = no_of_suggestions
        
    def aggregated_suggestion(self): 
        
        simi_words = self.find_similarity_spacy(self.word,no_of_words=10)
        sugg_words = self.perform_all_ops()
        
        # initial suggestion logic - words with highest probability
        final_sugg_words = []
        
        for word in sugg_words:
            
            if word in self.words_dict.keys() and abs(len(word)-len(self.word))<2:
                if len(word) > 1:
                    final_sugg_words += [word]
            
                
        del sugg_words 
        
        
        final_sugg_words = list(set(final_sugg_words))
        if len(final_sugg_words)<self.no_of_suggestions:
            i=0
            while len(final_sugg_words) <self.no_of_suggestions:
                if simi_words[i].lower() not in final_sugg_words:
                    final_sugg_words += [simi_words[i]]
                i+=1
        else:
            final_sugg_words = final_sugg_words[:self.no_of_suggestions]
            if self.word not in final_sugg_words:
                final_sugg_words[len(final_sugg_words)-1] = self.word
                
                
        return final_sugg_words
    


word = "wine"
start = time.time()
spell_checker = SpellSuggestion(word=word,no_of_suggestions=3)
sugg_words = spell_checker.aggregated_suggestion()
end = time.time()
print("suggested words: ",sugg_words)
print("time taken: ",end-start)



