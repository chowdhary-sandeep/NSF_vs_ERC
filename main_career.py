import pickle


import requests, json
import pandas as pd
import glob
import timeit
import time
from multiprocessing import Pool
import numpy as np
def toc(start_time):
    elapsed = timeit.default_timer() - start_time
    print(elapsed)
from zipfile import ZipFile
import re
import xmlschema
from pprint import pprint
import glob
# importing element tree
import lxml.etree as etree

import pickle
from get_career import *

def main(year):
    year=str(year);


    path_career='/mnt/sdb1/sandeep/5. NSF vs ERC/data/'

    #----------------
    dict_careers={}
    with open(path_career+'NSF_names_'+str(year)+'.pkl', 'rb') as f:
        names_=pickle.load(f)    
    t_ic = time.time();
    path_codes='/mnt/sdb1/sandeep/5. NSF vs ERC/codes/'
    
    for it in range(0,len(names_)):
        auth_name_to_search=names_[it]
        career_=get_career_from_name(auth_name_to_search);
        dict_careers[auth_name_to_search] = json.dumps(career_)
#         if it%10==0:
        print(it,len(names_),end='\r')
        t_oc = time.time();
        progress=year+'   '+str(it)+ '---- '+str(it/len(names_))+' '+str(round(t_oc-t_ic,2))+'--estimated---'+str(round((t_oc-t_ic)/(it/len(names_))/3600,3))+'hours'
        print(progress,end='\r')
        with open(path_codes+"0_track_"+year+".txt", "w") as file_object:
            file_object.write(progress+'\n')

        if it%100:
            num_file=round((it+1)/100)
            path_career='/mnt/sdb1/sandeep/5. NSF vs ERC/data/'
            with open(path_career+'dict_ERC_careers_'+year+str(num_file)'.pkl', 'wb') as f:
                pickle.dump(dict_careers, f)
            dict_careers={} 
