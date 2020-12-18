from final_project_shiyinglai import __version__
from final_project_shiyinglai import final_project_shiyinglai
import os
import pandas as pd
import urllib3
import json
from PIL import Image
import requests
from io import BytesIO
from datetime import date
import matplotlib. pyplot as plt 
api_key = os.environ.get("PRIVATE_API_KEY")

def test_version():
    assert __version__ == '0.1.0'


def test_search_artwork_by_culture():
    actual=type(final_project_shiyinglai.search_artwork_by_culture(apikey=api_key,culture="British",page="1"))
    expected = pd.core.frame.DataFrame
    assert actual == expected 
def test_find_artist():
    actual=type(final_project_shiyinglai.find_artist(name="Cronin",apikey=api_key))
    expected = pd.core.frame.DataFrame
    assert actual == expected 
def test_exhibition_explorer():
    actual=type(final_project_shiyinglai.exhibition_explorer(apikey=api_key,exhibition="Botticelli's Witness:  Changing Style in a Changing Florence"))
    expected = pd.core.frame.DataFrame
    assert actual == expected 
    
   
