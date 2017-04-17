
# coding: utf-8

# In[1]:

import pandas as pd
#from xlsxwriter.utility import xl_rowcol_to_cell
#from xlrd import open_workbook
#import csv

df=pd.read_csv('cust.csv')
out=df.style.highlight_null()


# In[11]:

#this is the function to be passed into applymap
def highlight_cell(val, date=39860,color1='purple',color2='blue'):
    if val==date:
        return 'background-color: %s' % color1
    elif val =='Active':
        return 'background-color:%s'%color2
    elif val=='Inactive':
        return 'background-color:%s'%color2
    else:
        return ''


# In[14]:

out1=out.applymap(highlight_cell,
                  subset=['Update_Date','Status','Updated_by'])
#type(out1)
#dir(out1)
#out1.render()


# In[88]:

out1


# In[ ]:

#find and replace
out=df.replace(['Active','Inactive'],['A','I'])
#df.str.replace('', '', case=False)


# In[48]:

#REGEX

match1=df.Updated_by[df.Updated_by.str.contains(
    '[A-Z]{1}[_]{1}[A-Z]{1}[a-z]*')].index.tolist()
type(match)
match2=df.Updated_by[df.Updated_by.str.contains('SYSTEM')].index.tolist()
#idx=df[df['Updated_by'].str.contains('SYSTEM')].index.tolist()
match2
match1
match=match1+match2
len(match)
#len(df.Updated_by)

testlist=[]
for i in range(131):
    testlist.append(i)

#testlist
notmatch=list(set(testlist) - set(match))
print notmatch
notmatch.sort()


# In[49]:

#test if the regex is true
df.Updated_by[df.Updated_by.str.contains('[A-Z]{1}[.]{1}[A-Z]{1}[a-z]*')]


# In[81]:

dff=pd.DataFrame({'a':[12,3,4,4],'b':[2,3,4,5],'c':['a','b','ab','abc']})
dff
dff.loc[[0,2,],['a','c']]
dff.c[dff.c == 'a'].index.tolist()
#def highlight(val, date=39860,color1='purple',color2='blue'):
 #   if val=='[a]*':
#      return 'background-color: %s' % color1
#dff.applymap(highlight)
#dff.a[dff.a==4].index.tolist()
dff
dff.c[dff.c.str.contains('abc')]#.index.tolist()

#def some_fn():
 #   if dff.index.vlues ==1:
#      return 'applymap_' + x
    #elif x:
     #   return 100 * x
#    else:
 #       return

#dff.applymap(some_fn)

dff.ix[[0]]
ix=dff.index.values


# In[ ]:

#below give a another column which is logical
df1['Flag'] = df1.applymap(f).all(axis=1).astype(bool)



# In[87]:

df1=pd.DataFrame({'a':[1,2,3,4],'b':['a','b','c','d']})
df1
print type(df1)
df1.to_csv('df1.csv')

