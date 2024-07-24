

from flask import Flask, request, render_template
import subprocess
from random import randint
from hashlib import md5
import os
import re

def main():
    with open('flag.txt','r') as f :
        flag=f.read()
    return flag +""*(10-len(flag))
from parse import rgb_parse
print(rgb_parse(main()))   