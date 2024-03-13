import pandas as pd
import numpy as np

airlines_df = pd.read_csv(r'C:\Users\gauri\Desktop\archive\austrian_airlines_reviews.csv')

print(type(airlines_df))


#We will start by finding the basic information related to our dataset

print(airlines_df.describe())

airlines_df.info()

recommended_vals = airlines_df["Recommended"].unique().tolist()
print(recommended_vals)

'''
As the entire recommended column consists of only one value
i.e 10, we can drop this column.
'''

airlines_df_cleaned = airlines_df.drop(columns ='Recommended')
print(airlines_df_cleaned)

#Let us look at the null values in the dataset.

print(airlines_df_cleaned.isna().sum())

#Finding mean, median and mode of the column Ratings

mean_rating =airlines_df_cleaned['Rating'].mean() #4.997
median_rating =airlines_df_cleaned['Rating'].median() #5.0 
mode_rating =airlines_df_cleaned['Rating'].mode()  #0  1.0


#For the null values we can replace it with the mean of the entire Ratings column

airlines_df_cleaned.fillna({'Rating' : mean_rating}, inplace = True)
print(airlines_df_cleaned["Rating"].unique().tolist()) 
print(airlines_df_cleaned.isna().sum()) #Null values has been brought down to zero in ratings

#Another standard practice is to change date columns to datetime datatype

airlines_df_cleaned['Date Published'] =  pd.to_datetime(airlines_df_cleaned['Date Published'])
airlines_df_cleaned['Date']  = pd.to_datetime(airlines_df_cleaned['Date'])
airlines_df_cleaned['Date Flown']  = pd.to_datetime(airlines_df_cleaned['Date Flown'])

#Now we start with the analysis

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

def rating(row):
    rating_value = row['Rating']
    if 1.0 <= rating_value <= 3.0:
        return 'Poor'
    elif 3.0 <= rating_value <= 5.0:
        return 'good'
    elif 5.0 <= rating_value <=7.0:
        return 'very good'
    elif rating_value > 7:
        return 'excellent'
airlines_df_cleaned['Satisfaction'] = airlines_df_cleaned.apply(rating,axis=1)
print(airlines_df_cleaned.info())

#Let us find the country from where the positive reviews were the highest

plt.figure(figsize=(50,30))
plt.title('Country vs Reviews')
plt.xlabel('Rating')
plt.ylabel('Countries')
sns.barplot(y = 'Country', x='Rating', data = airlines_df_cleaned)
plt.show()

'''From the above plot we can establish that Portugal is the country 
which has the best experience (on the basis of ratings) while Macedonia and Albania
have the worst
 '''

#Let us now find the country which gave maximum number of reviews

plt.figure(figsize=(15,8))
sns.countplot(data = airlines_df_cleaned, x='Country', color='skyblue')
plt.title('Number of reviews per country')
plt.xlabel('Country')
plt.ylabel('number of reviews')
plt.xticks(rotation =90)
plt.show()

'''
As we can see US,UK and Austria gave the maximum number of reviews,
Now let us move to the type of traveller category.
'''
#Let us plot a graph between type of traveller vs Satisfaction Level

plt.figure(figsize =(15,8))
sns.countplot(x='Type Of Traveller', hue = 'Verified', data = airlines_df_cleaned)
plt.xlabel('Type of Travellers')
plt.ylabel('Number of reviews')
plt.title("Reviews vs Type Of Travellers")
plt.show()

'''
This hence shows us that in both Verified and Non Verified Category 
The maximum number of reviews are gived by travellers travelling 
for Solo Leisure
'''
#By changing the hue we can also deduce satisfactory levels of the type of travellers
plt.figure(figsize =(15,8))
sns.countplot(x='Type Of Traveller', hue = 'Satisfaction', data = airlines_df_cleaned)
plt.xlabel('Type of Travellers')
plt.ylabel('Number of reviews')
plt.title("Reviews vs Type Of Travellers")
plt.show()

'''
On the basis of evaluation one can deduce that Solo Leisure Travellers 
reviews matter alot as they have maximum reviews in all categories of 
satisfaction
'''

#Finally lets create a graph between Seat type and number of reviews

plt.figure(figsize =(15,8))
sns.countplot(x='Seat Type', hue = 'Satisfaction', data = airlines_df_cleaned)
plt.xlabel('Seat Type')
plt.ylabel('Number of reviews')
plt.title("Seat type vs number of reviews")
plt.show()

'''
This also shows that Economy class gave most number of reviews 
with highest satisfaction and dis- satisfaction ratings.
'''


