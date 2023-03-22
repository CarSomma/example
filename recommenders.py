"""
Here we define our functions for the recommender system
"""

from utils import MOVIES
import random


def get_random_recommendations(n):
    
    if n > len(MOVIES):
        print(f"YO choose at most {len(MOVIES)}")
        return []    
    else:
        random.shuffle(MOVIES)
        top_n = MOVIES[:n]
        return top_n

        
if __name__ == "__main__":
    top_3 = get_random_recommendations(3)
    print(top_3)

        
