# A Pytest Verified Search Engine

This is a simple search engine that scrapes 1000 webpages containing a limited number of words (e.g. fruit names) and saves data such as term frequency, page rank, ... in 7 json files. The user can search for one or more words and receive the top 10 most reputable URLs (based on page rank calculations) with the most occurrences of those words (based on Vector Space Model).

The project uses pytest to perform automated tests on different metrics calculated, including page rank, tf, idf, tf-idf, and search results.

This was written for 1405Z Project, Carleton University, Fall 2022. Due to instructions in the ["Course Project Specification"](/docs/Course%20Project%20Specification.pdf), only a limited number of modules has been used. For more info see the ["Report"](/docs/Report.pdf).

In the ["mongo-1 branch"](https://github.com/ca-sajad/Python-SearchEngine-1405Project/tree/mongo-1), instead of using json files as database, a mongoDB database has been used.


