import pandas as  pd

csvData=pd.read_csv('path to csv')


csv_data2=pd.read_csv('pathto csv', index_col=0)

#selecting a column

csv_data2['columnname']
csv_data2.columnname

#adding a column
csv_data2['columnname']=['vlaue' , .....]

#make columns using other column
csv_data2['newcolumn']=csv_data2["old column1"] * csv_data2['old column2']


#to access rows
csv_data2.loc['rowname']


#to access one value in table
csv_data2.loc['row', 'column']
csv_data2['columnname'].loc['rowname']
