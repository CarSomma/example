"""TODO

Write a programs that checks that random recommender 
works as expected

we use pytest

to install pytest  type in the terminal/Git-bash
    + conda install -c conda-forge pytest
    + pip install pytest

TDD (Test Driven Development) cycle:

0. Our hypothesis: the program works
1. We want to write tests that disprove our hypothesis
2. We rewrite the code so that the hypothesis holds
3. repet steps 0-1-2

"""
from recommenders import get_random_recommendations
from utils import MOVIES

def test_2_movie():
    top2 = get_random_recommendations(2)
    assert len(top2) == 2

def test_10_movie():
    top10 = get_random_recommendations(10)
    assert len(top10) == 0

def test_is_a_string():
    for movie in MOVIES:
        assert isinstance(movie,str)