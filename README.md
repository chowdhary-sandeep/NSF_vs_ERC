# NSF_vs_ERC

1) 
The details of ERC and NSF winners used in this analyses can be obtained from https://erc.europa.eu/project-statistics/project-database
and https://www.nsf.gov/awardsearch/download.jsp respectively.
2) The career data for the winners can be obtained from openalex.org via the author search feature. Here is the API we used: https://api.openalex.org/works. For each winner, all works they published were downloaded along with all the relevant infomation for each paper such as author affiliations, concepts, citations etc. The data was filtered and put into a dataframe which is used for the analyses in main.ipynb.
3) main.ipynb contains all the analyses presented in the paper.
4) plots.ipynb loads data for figures created in main.ipynb and creates the final figures used in the paper.
