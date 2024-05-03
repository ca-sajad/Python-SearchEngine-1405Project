# 1405-Project
Final Code for 1405Z Project, Carleton University, Fall 2022

This is a simple search engine that scrapes 1000 webpages containing a limited number of words (i.e. fruit names) and saves data such as term frequency, page rank, ... in 7 json files. Then, the user can search for fruit names and receive the top 10 most reputable URLs (based on page rank calculations) with the most occurrences of those fruit names (based on Vector Space Model).

In the ["mongo-1 branch"](https://github.com/ca-sajad/Python-SearchEngine-1405Project/tree/mongo-1), instead of using file-storage, a mongoDB database has been used.

For more info see ["Course Project Specification.pdf"](/Course%20Project%20Specification.pdf) and ["Report.pdf"](/docs/Report.pdf).
