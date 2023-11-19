import pandas as pd
import os
dir = "Opal/Origin/Opal.xlsx"

df  = pd.read_excel(dir)

'''Calculate threshold'''
column_name = ['Cytoplasm Granzyme B (Opal 650) Mean (Normalized Counts, Total Weighting)', 'Membrane CD45 (Opal 690) Mean (Normalized Counts, Total Weighting)',
               'Membrane CD4 (Opal 520) Mean (Normalized Counts, Total Weighting)','Membrane CD56 (Opal 540) Mean (Normalized Counts, Total Weighting)',
               'Membrane CD8 (Opal 570) Mean (Normalized Counts, Total Weighting)','Nucleus FoxP3 (Opal 620) Mean (Normalized Counts, Total Weighting)',
               'Nucleus Nucleus (DAPI) Mean (Normalized Counts, Total Weighting)']
indice = [df.columns.get_loc(col) for col in column_name ] 
print(indice)

for i in range(len(indice)):
    specific_df = pd.read_excel(dir,usecols=[0,indice[i]])
    average = specific_df.iloc[:,1].mean()
    #print(f"specific_df : {specific_df.shape}")
    #print(specific_df.head(5))
    #print(f"average(threshold): {average}")
    new_df = specific_df[specific_df[column_name[i]] > average]
    #print(f"new_df: {new_df.shape}")
    #print(new_df.head(5))
    new_df.to_excel(f"Opal/Processed/Opal_After_Threshold/{column_name[i]}.xlsx")

'''
file = os.listdir('Opal/Processed/Opal_After_Threshold')
'1~33/33~66/66~99'
q1 = new_df[column_name].quantile(0.33)
q2 = new_df[column_name].quantile(0.66)

subset1 = new_df[new_df[column_name]<=q1]
subset2 = new_df[(new_df[column_name]<=q2) & (new_df[column_name]>q1)]
subset3 = new_df[new_df[column_name]>q2]

print(f"subset1: {subset1.shape}")
print(f"subset2: {subset2.shape}")
print(f"subset3: {subset3.shape}")

subset1.to_excel('Opal/Processed/Opal 1~33%.xlsx')
subset2.to_excel('Opal/Processed/Opal 34~66%.xlsx')
subset3.to_excel('Opal/Processed/Opal 67~100%.xlsx')'''

