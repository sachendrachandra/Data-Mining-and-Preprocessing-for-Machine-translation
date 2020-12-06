# TSE_mini_project_1

This is a part of the Topics in Software Engineering course Project offered at IISc Bangalore by Associate Professor Aditya Kanade and Professor Shirish Shevade.

The project involves Data Collection and Preprocessing for a Neural Machine Translation Model(NMT). The NMT model gives a novel approach to automatically generate Natural Language comments for a Python Source Code.

The project is mainly divide into 4 parts:
 
 Part 1:
 It involves Cloning the python repositories from which useful python programs can be scraped along with Natural Language Comments. The API used to clone the   repository is "https://api.github.com/search/repositories?q=language:python&sort=forks&order=desc&page=1". About 310 most forked repositories were Cloned. The file "repository_cloner.py" contains the python code for the same. The list of repositories cloned is mentioned in the file "List_of_cloned_repositories.txt".
 
 Part 2:
 Once the repositories have been cloned, the next task was to extract python files from the all the repositories. The file PythonFilesExtracter.py contains the code for doing so. The code recursively searches a folder and subfolder to extract all the python files that are present in any repository using os and shutil modules.
 
 Part 3:
 Ones the Python files have been collected the next task was to preprocess each python file and break it into different methods/functions so that data can be presented in (code, natural language comment) pair. Each function/method extracted is saved as a separate python file. The file "Decompose_py_file_into_functions.py" contains the code for the same.
 
 Part 4:
 The last part involves extracting the Docstring and Comments written in natural language in each Python file collected in Part 3. It uses tokenizing module to tokenize a python file to extract the Comments along with AST traversal of Source code to extract docstring of the source code. Once the comments and docstring has been extracted, the next part of involves replacing the the comments and Docstring with Placeholders for python file collected in Part 3. Each Comment is replaced with "Comment Placeholder" and each Docstring is replaced with "Docstring Placeholder".
 Now once the Comments, Docstrings and the Python Code(with Placeholders) has been collected,the next part was to store it in JSON format with each entry of JSON file was following way:
 
 {
 "code":"The Python Code",
 "nl_comment":[ "docstring","comment 1", "comment 2"...]
 }
 
 The code for doing the above process is present in the file "Dockstring_extracter.py". 

The data has been compressed into file titled data2.tar.gz
The file "data2.json" can be seen to understand the format of data collected.
The total (code, natural language comment) pair collected are 222513
