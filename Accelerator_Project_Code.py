#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import time
import re


# In[12]:


begin=time.time()
file_path ="F:/Attempt_4/Simulator_Meta_Data_Attempt4.xlsx"     #filePath from Local Computer
file_reading= open("F:/Attempt_4/Code_Template_Final.txt",'r')   #Reading Code Template
file_writing= open("F:/Attempt_4/output_Final.txt",'w')           #Writing a Code 
pattern1=re.compile(r"<<<(\w+).\d+.!(\w+)!.(\w+).!(\w+)!>>>")
pattern2=re.compile(r"<<<(\w+).\d+.(\w+).(\w+)>>>")                                #(\d+) Represent a group of one or more digits
pattern3= re.compile(r"<<<(\w+).\d+.([\w.(]+)!(\w+)!.!([\w.]+)!!(\w+)!>>>")        #(\w+) Represent a group of one or more words
pattern4= re.compile(r"<<<(\w+).\d+.(\w+).!(\w+)!.!(\w+)!>>>") 
for line in file_reading:
   
    for word in line.split():                              #Spliting a Line By Word by Word
        try:
    #In Regular Expression Group 0 Represents a whole Pattern and Group 1 represents first  items of '()' and so on...   
            for key1 in re.finditer(pattern1, word):
                Sheet_name=key1[1]
                column1=key1[2]
                finding_value=key1[3]
                column2=key1[4]
                Reading_Excel = pd.read_excel(file_path,sheet_name=Sheet_name)   #Reading_Sheet
                Reading_Excel.dropna(subset = [column1,column2], inplace=True)   #Droping NAN Cells
                Key_column=Reading_Excel[column1] 
                ValuePair_column=Reading_Excel[column2] 
                for check,rep in zip(Key_column,ValuePair_column):             
                    if check==finding_value: 
                        word = word.replace(key1[0], rep)        #Replacing Contents From Sheet Using (Key,Value) Pair
        except:
            print("Pattern1 ERROR!!! Please Re-Verify The Code-Template")
        
        try:
            for key2 in re.finditer(pattern2, word):
                Sheet_name=key2[1]                                      #Sheet_name through Dynamic
                Column_name=key2[2]                                     #Extracting a column through Dynamic 
                Condition_operation=key2[3]
                Reading_Excel = pd.read_excel(file_path,sheet_name=Sheet_name)   #Reading Excel Based upon Template

                if Condition_operation=="ALL":     # 'All' Accessing all Variables 
                    Respective_column=Reading_Excel[Column_name].tolist()
                    Removing_Quotes_for_Respectivecolumn=",".join([str(s) for s in Respective_column[:]])
                    word=word.replace(key2[0],str(Removing_Quotes_for_Respectivecolumn))

                if Condition_operation=="Extended":  # 'Extended' is Adding Values via Code Syntax
                    Respective_column="@"+Reading_Excel[Column_name] 
                    Respective_column_toList=Respective_column.tolist()
                    Removing_Quotes_for_Respectivecolumnvalues=",".join([str(s) for s in Respective_column_toList[:]])
                    word=word.replace(key2[0],str(Removing_Quotes_for_Respectivecolumnvalues)) #Replacing Contents         
        except:
            print("Pattern2 ERROR!!! Please Re-Verify The Code-Template")
            
        try:   
            for key3 in re.finditer(pattern3, word):
                Sheet_name=key3[1]
                variable_name=key3[2]
                Column_name_for_Parameters=key3[3]
                Telemetry_variablename=key3[4]
                Telemetry_Column_Parameters=key3[5]
                Reading_Excel = pd.read_excel(file_path,sheet_name=Sheet_name)
                For_SQL_AddValue=pd.DataFrame(variable_name+'"@'+Reading_Excel[Column_name_for_Parameters]+'",'+Telemetry_variablename+Reading_Excel[Telemetry_Column_Parameters]+");")
                sql_addvalue_Dataframe=For_SQL_AddValue.to_string(header=False,index=False)
                sql_addvalue_Dataframe=sql_addvalue_Dataframe.replace(" ","")       
                word=word.replace(key3[0],sql_addvalue_Dataframe)                   #Replacing Contents
        except:
            print("Pattern3 ERROR!!! Please Re-Verify The Code-Template")         
        try:
            
            for key4 in re.finditer(pattern4, word):
                Sheet_name=key4[1]
                Access_modifier=key4[2]
                data_type_column=key4[3]
                Column_name=key4[4]
                Reading_Excel = pd.read_excel(file_path,sheet_name=Sheet_name)
                For_GetAndSet=Access_modifier+" "+Reading_Excel[data_type_column]+" "+Reading_Excel[Column_name]+" "+"{get;set;}"
                GetAndSet=For_GetAndSet.to_string(index=False)
                GetAndSet=GetAndSet.replace("  ","")                            #Removing Spaces
                word=word.replace(key4[0],str(GetAndSet))  
        except:
            print("Pattern4 ERROR!!! Please Re-Verify The Code-Template") 
        file_writing.write(' ')
        file_writing.write(word)
    file_writing.write("\n")

file_reading.close()                  #Closing The Code Template 
file_writing.close()                  #Closing The Output Write File
time.sleep(1)
end=time.time() 
print(f"Time Execution {end-begin}")               #Displaying The Time


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




