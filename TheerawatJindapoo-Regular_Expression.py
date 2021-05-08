import numpy as np
import pandas as pd
import PyPDF2
import re
import os
from os import path
from os import listdir
from os.path import isfile, join

### change syllabi folder directory here please.
file_name = 'C:\\Users\\Admin\\Desktop\\wrangling\\assignment2\\syllabi'

pdf_files = [os.path.abspath(os.path.join(file_name,x)) for x in listdir(file_name)
                                            if x.endswith('.pdf')]
data = pd.DataFrame(columns=["direct","text","Professor's name", "University", "Email", "Website","Phone number","Date","Day"])
data.direct = pdf_files

def get_text(get):
    with open(get, 'rb') as pdf:
        read_pdf = PyPDF2.PdfFileReader(pdf, strict=False)
        num_page = read_pdf.numPages
        main_text = []
        for x in range(num_page):
            getpage = read_pdf.getPage(x)
            text = getpage.extractText().split("\n")
            main_text = main_text + text
    return main_text

for i in range(len(pdf_files)):
    data.text[i] = get_text(data.direct[i])

regex_name = re.compile("(Instructors|Instructor|Professors|Professor)+:\s*[A-Za-z\.]+,?\s?(?:[A-Za-z]*\.?\s*)?[A-Za-z]+")
regex_university = re.compile("(((u|U)niversity)\s?((o|O)f)[a-zA-Z\s]*)|([a-zA-Z/s]*\s?(College))")
regex_email = re.compile("([a-zA-Z]|[0-9]|\.|-|_)+@([a-zA-Z]|\.)+\.(com|net|gov|org|edu)")
regex_website = re.compile("(?P<url>https?://[^\s]+)")
regex_phone = re.compile("(\(?[0-9]{3}\)?(\s*|\-?)[0-9]{3}(\s*|\-?)[0-9]{4})")
regex_date = re.compile("(\d{2}(/|-|\s)(\d{2}|[a-zA-Z]+)(/|-|\s)\d{4})|(\d{4}(/|-|\s)(\d{2}|[a-zA-Z]+)(/|-|\s)\d{2})")
regex_day = re.compile("[a-zA-Z]*(day)")

name_list = []
university_list = []
email_list = []
website_list = []
phone_list = []
date_list = []
day_list = []

def converter(ToString):
    str = ""
    for each_list in ToString:
        str += each_list
    return str

for each_text in data.text:
    if regex_name.search(converter(each_text)) != None:
        name_found = regex_name.search(converter(each_text))
        name_list.append(name_found.group())
    else:
        name_list.append("Not Found")
    
    if regex_university.search(converter(each_text)) != None:
        university_found = regex_university.search(converter(each_text))
        university_list.append(university_found.group())
    else:
        university_list.append("Not Found")
    
    if regex_email.search(converter(each_text)) != None:
        email_found = regex_email.search(converter(each_text))
        email_list.append(email_found.group())
    else:
        email_list.append("Not Found")
    
    if regex_website.search(converter(each_text)) != None:
        website_found = regex_website.search(converter(each_text))
        website_list.append(website_found.group())
    else:
        website_list.append("Not Found")
        
    if regex_phone.search(converter(each_text)) != None:
        phone_found = regex_phone.search(converter(each_text))
        phone_list.append(phone_found.group())
    else:
        phone_list.append("Not Found")
        
    if regex_date.search(converter(each_text)) != None:
        date_found = regex_date.search(converter(each_text))
        date_list.append(date_found.group())
    else:
        date_list.append("Not Found")

    if regex_day.search(converter(each_text)) != None:
        day_found = regex_day.search(converter(each_text))
        day_list.append(day_found.group())
    else:
        day_list.append("Not Found")


data["Professor's name"] = name_list
data["University"] = university_list
data["Email"] = email_list
data["Website"] = website_list
data["Phone number"] = phone_list
data["Date"] = date_list
data["Day"] = day_list

final_data = data[["Professor's name","University","Email","Website","Phone number","Date","Day"]]
final_data.to_csv("Assignment2_Theerawat-Jindapoo.csv")