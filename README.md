# WhatsApp-Autocorrect-Checker
Autocorrect checker for WhatsApp chats that detects and analyzes text corrections. Includes preprocessing, NLP-based error detection, and visualization of typing patterns to study autocorrect behavior in real-world conversations.

NOTE: This project is executed keeping SOLID principles in mind.

# Technical Overview
This project is aimed to rectify incorrect messages commonly caused by typos or lack of linguistic knowledge. 
It is implemented using a probabilistic model for a large pool of vocabulary initially calculated on a big dataset from kaggle.
TF-IDF technique is used to calculate the overall probability that represents the use of a word in a persons vocabulary.
This datatset increases/improves dynamically with more and more interactions with the user. Thereby enabling a customised recommendation engine.
The initial computed probabilistic dataset is stores as JSON file named "word_prob_json.json". As the name indicates it stores the probability of each and every word and gets updated/recalculated frequently.

exmaple piece from the JSON file:
"lodgings": 9.860297512067659e-06,
  "Intriguer": 8.963906829152417e-07,
  "ossify": 8.963906829152417e-07,
  "slough": 2.509893912162677e-05,

As you can clearly see, the values are in the range of 10^-7 indicating the diversity and quality of the dataset.

NOTE: misspelled words are also present indicating previous interaction with the user.

# How the Suggestion Algorithm Works?

The rule of thumb taken into account is that misspelled words and similar(semantic) words both are a possibility.
Hence, the algo used NLP to get similar words and  does the robust permutation/combination logics for the case of misspelling.
Different logics to arrive at permutations and combinations:
1. Addition
2. Deletion
3. Replacement
4. Swapping

Each class handles a micro-problem statement
with WordOps handling the string logics
Similarity_parser handling the semantic similarity
Spell_suggestion being a wrapper that combines and aggregates and preprocess the data before combutation.

The words are then run through a loop identifying them with the words from the JSON model and are sorted based on probability.
The top 3 suggestions per words are returned which can be configured manually as well.


Here are some snapshots attached 
<img width="958" height="452" alt="image" src="https://github.com/user-attachments/assets/7eaaa42a-9bda-4571-bd40-f41cafe4b817" />
<img width="953" height="406" alt="image" src="https://github.com/user-attachments/assets/70cdb09d-9128-4b1a-a35f-c95542f03d85" />
<img width="926" height="404" alt="image" src="https://github.com/user-attachments/assets/3d35de10-49d7-4a32-a5fb-9bd0c3db8fde" />
Viewing, expanding all suggestions:
<img width="766" height="406" alt="image" src="https://github.com/user-attachments/assets/88e8e5b0-3483-468e-b000-3b19f4db9b73" />

The word recommended  as a suggestion is user-specific, meaning your words are updated in the backend probabilistic model that determines the preference of listing.
CONCLUSION
Conclusion

The WhatsApp Autocorrect Checker demonstrates a robust approach to detecting and correcting text errors in real-world conversations. By combining probabilistic modeling, semantic similarity, and string-level operations, the system is capable of providing personalized, context-aware suggestions. The dynamic nature of the backend dataset ensures that the model continuously adapts to the user’s vocabulary and typing patterns, resulting in increasingly accurate and user-specific recommendations over time. This project highlights the practical application of NLP techniques in enhancing communication efficiency and user experience while adhering to sound software design principles.
