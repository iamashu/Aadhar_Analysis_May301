from pandas import *
import pandasql

if __name__ == '__main__':
    aadhar_data = read_csv('C:/Users/iamashu/Documents/aadhar_data.csv')
    #aadhar_data1 = aadhar_data['Gender']
    #print aadhar_data1
    #aadhar_data['Gender'] = aadhar_data['Gender'].map({'F' : 'Female', 'M' : 'Male'})
    aadhar_data.rename(columns=lambda x: x.replace(' ', '_').lower(), inplace=True)
    q1 = 'SELECT count(distinct(Gender))from aadhar_data where Gender="M";'
    q2 = 'SELECT age, count(*) as count from aadhar_data group by age order by count desc;'
    q3 = 'SELECT State, count(*) as count from aadhar_data group by State order by count desc;'

    aadhar_solution = pandasql.sqldf(q3, locals())
    print aadhar_solution