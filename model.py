import pandas as pd
co_names=["user_id","item_id","ratings","timestamp"]

df=pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/file.tsv', sep="\t", names=co_names)

print(df.head())

movie_titles=pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv')
print(movie_titles.head())


data=pd.merge(df, movie_titles, on="item_id")

print(data.head())

print(data.groupby('title')['ratings'].mean().sort_values(ascending=False).head())



ratings=pd.DataFrame(data.groupby('title')['ratings'].mean())

ratings['num of ratings']=pd.DataFrame(data.groupby('title')['ratings'].count())

print(ratings.head())



import matplotlib.pyplot as plt
import seaborn as sns





plt.figure(figsize=(10, 4))




ratings['ratings'].hist(bins=70)



print(ratings.sort_values('num of ratings', ascending=False).head())



moviemat=data.pivot_table(index="user_id",columns="title",values="ratings")

print(moviemat.head())

starwars_user_ratings=moviemat['Star Wars (1977)']
print(starwars_user_ratings.head())


similar_to_starwars=moviemat.corrwith(starwars_user_ratings)

corr_starwars=pd.DataFrame(similar_to_starwars, columns=['correlation'])

print(corr_starwars.head())

corr_starwars.sort_values('correlation',ascending=False)

corr_starwars=corr_starwars.join(ratings['num of ratings'])

preffered_movies_for_starwars=corr_starwars[corr_starwars['num of ratings']>100].sort_values('correlation',ascending=False).head()

print(preffered_movies_for_starwars.head())








