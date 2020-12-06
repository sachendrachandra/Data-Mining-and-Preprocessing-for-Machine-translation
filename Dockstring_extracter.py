# -*- coding: utf-8 -*-
"""Parse Python source code and get or print docstrings."""

__all__ = ('get_docstrings', 'print_docstrings')

import ast
import os
import tokenize
import json 

from itertools import groupby
from os.path import basename, splitext


NODE_TYPES = {
    ast.ClassDef: 'Class',
    ast.FunctionDef: 'Function/Method',
    ast.Module: 'Module'
}


def get_docstrings(source):
    """Parse Python source code and yield a tuple of ast node instance, name,
    line number and docstring for each function/method, class and module.
    The line number refers to the first line of the docstring. If there is
    no docstring, it gives the first line of the class, funcion or method
    block, and docstring is None.
    """
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, tuple(NODE_TYPES)):
                docstring = ast.get_docstring(node)
                lineno = getattr(node, 'lineno', None)
                if (node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str)):
                    lineno = node.body[0].lineno - len(node.body[0].value.s.splitlines()) + 1

                yield (node, getattr(node, 'name', None), lineno, docstring)
    except:
        pass


def print_docstrings(source, module='<string>'):
    a=[]
    if hasattr(source, 'read'):
        filename = getattr(source, 'name', module)
        module = splitext(basename(filename))[0]
        source = source.read()
    docstrings = sorted(get_docstrings(source),key=lambda x: (NODE_TYPES.get(type(x[0])), x[1]))
    grouped = groupby(docstrings, key=lambda x: NODE_TYPES.get(type(x[0])))

    for type_, group in grouped:
        for node, name, lineno, docstring in group:
            name = name if name else module
            # print("ii")
            heading = "%s '%s', line %s" % (type_, name, lineno or '?')
            
        # print(name)
        # a.append(name)
        a.append(docstring)
    
    return a

import sys, token, tokenize

def do_file(fname):
    source = open("/home/sachendra/TSE/split2/"+str(fname),'r+')
    mod = open("/home/sachendra/TSE/striped2/"+str(fname), "w")
    
    prev_toktype = token.INDENT
    first_line = None
    last_lineno = -1
    last_col = 0
        
    tokgen = tokenize.generate_tokens(source.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
        if 0:   # Change to if 1 to see the tokens fly by.
            print("%10s %-14s %-20r %r" % (
                tokenize.tok_name.get(toktype, toktype),
                "%d.%d-%d.%d" % (slineno, scol, elineno, ecol),
                ttext, ltext
                ))
        if slineno > last_lineno:
            last_col = 0
        if scol > last_col:
            mod.write(" " * (scol - last_col))
        if toktype == token.STRING and prev_toktype == token.INDENT:
                # Docstring
            mod.write("'''DocString Placeholder'''")
        elif toktype == tokenize.COMMENT:
                # Comment
            mod.write("#Comment Placeholder")
        else:
            mod.write(ttext)
        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno



li=[]
li2=[]
if __name__ == '__main__':
    import sys
    i=1
    for file in os.listdir("/home/sachendra/TSE/split2"):
        ci=[]
        # ci2=[]
        print(i)
        dic={}
        with open("/home/sachendra/TSE/split2/"+file) as f:
            li=print_docstrings(f)
            print(li)
        i=i+1
        fileObj = open("/home/sachendra/TSE/split2/"+file)
        try:
            for toktype, tok, start, end, line in tokenize.generate_tokens(fileObj.readline):
                if toktype == tokenize.COMMENT:
                    li.append(tok)
        except:
            pass

        # with open("/home/sachendra/split/"+file) as f:
        #     try:
        #         tokens = tokenize.generate_tokens(f.readline)
        #         for token in tokens:
        #             ci.append(token.string)
        #             # ci2.append(str(token.type)+"_"+str(ci.count(token.type)))
        #     except:
        #         pass

        with open("/home/sachendra/TSE/split2/"+file,'r') as f:
            # do_file("/home/sachendra/split/"+file)
            try:
                do_file(file)
            except:
                li=[]


            

        ci=[]
        f=open("/home/sachendra/TSE/striped2/"+file,'r')
        ci = f.read()
        # print(ci)

        with open("/home/sachendra/TSE/data2.json", "a") as fil:
            if(len(li)>0 and len(ci)<=5000):
                dic["code"] = ci
                dic["nl_comment"] = li
            else:
                os.remove("/home/sachendra/TSE/split2/"+file)
                os.remove("/home/sachendra/TSE/striped2/"+file)
            json.dump(dic,fil,indent=4)
        