import os 
#! Approach 1 for windows
# email_txt = "Day 10 - Files - Create, Read & Download\\templates\\email.txt"
#! Approach 2 for any os
# email_txt = os.path.join("Day 10 - Files - Create, Read & Download","templates","email.txt")
#! Approach 3 
this_file_path = os.path.abspath(__file__)
# print(this_file_path)
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)
# print(BASE_DIR, ENTIRE_PROJECT_DIR)

email_txt = os.path.join(BASE_DIR, "templates", "email.txt")

content = ""

with open(email_txt, "r") as f:
    content = f.read()
    
print(content.format(name="Ayush"))