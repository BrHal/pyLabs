#!/usr/bin/env python2
from jinja2 import Environment, FileSystemLoader

mybooks=[
    {"title":'Foundation', "author":'Isaac Asimov', "price": 2.50},
    {"title":'I, robot', "author":'Isaac Asimov', "price": 2.30},
    {"title":'Mostly harmless', "author":'Douglas Adams', "price": 2.42},
]

print(
    Environment(
        loader=FileSystemLoader('mytemplates')
    ).get_template('templ1.txt')
    .render(books=mybooks)
)
