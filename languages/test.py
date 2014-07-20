#!/usr/bin/python3
import langread
print("------------------------")
print("Correct Test:")
langread.read_file('python.xml')
print("\tLang Read {}".format(str(langread)))
print("------------------------")
print("Fail Test:")
langread.read_file('badxml.xml')
print("\tLang Read {}".format(str(langread)))