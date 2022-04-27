import os, sys
try:
    __import__("naim3").niki()
except Exception as e:
    exit(str(e))