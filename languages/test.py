#!/usr/bin/python3
import langread
print("------------------------")
print("Correct Test:")
langread.read_file('python.xml')
print("------------------------")
print("Fail Test:")
langread.read_file('badxml.xml')
