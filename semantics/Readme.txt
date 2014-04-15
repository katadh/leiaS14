At this point, only a very basic and partial analysis is implemented.
See the tests.py file for examples.

INPUT:
    From Syntax: 
        A list of lemmatized token strings:
        e. g., ['I', 'buy', 'fish']
        In the future we will need POS, NER, and dependency information as well)
    
    From Lexicon: 
        A mapping from word lemmas to ontological concepts:
        e. g., {'I': [Animal],
                'buy' : [Buy, BuyEvent],
                'fish' : [Fish, FishEvent]}
        Again, in the future, we might also need syn-structs and sem-structs.

    From Ontology:
        A taxonomical hierarchy of concepts with specified slot filler types.
        e. g., see concept.py and slot.py
        
OUTPUT:
    A text meaning representation as a list of concept instances related via slots.
    e. g., ['Instance of FishEvent: {
                theme: {
                    type: Fish, 
                    filler: Instance of Fish: {}}, 
                agent: {
                    type: Animal, 
                    filler: Instance of Animal: {}}}']