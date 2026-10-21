import json
import sys

def save(mapping,filepath):
    with open(filepath,"w") as f:
        json.dump(mapping,f)

def load(filepath):
    try:
        with open(filepath,'r') as f:
            return json.load(f)
    except FileNotFoundError: 
        return {}