# Project1

### 1.Introduction

​	The dataset "Biopics" is derived from the story ['Straight Outta Compton' Is The Rare Biopic Not About White Dudes](http://fivethirtyeight.com/features/straight-outta-compton-is-the-rare-biopic-not-about-white-dudes),  as featured on FiveThirtyEight. The data originates from [IMDb](http://www.imdb.com/), a popular online database of films, television programs, and related content. This dataset encompasses information related to biographical films, commonly known as biopics, along with their attributes. The dataset primarily aims to explore and understand the diversity and characteristics of biographical films, particularly in terms of their subjects and subjects' backgrounds.

​	The dataset is stored in CSV format, containing both text and numeric data types. Through this dataset, we aim to research the following questions:

1. **Development of Biographical Film Quantity:** How has the number of biographical films changed over the years?

2. **Racial Preferences:** Do biographical film subjects exhibit racial preferences?

3. **Gender Preferences:** Do biographical film subjects exhibit gender preferences?

4. **Primary Subjects:** Which professions have more representation as the main characters in biographical films?

   

### 2.Data Summary

2.1 Data link

​     We acquired the data from this GitHub repository: https://github.com/fivethirtyeight/data/tree/master/biopics. 

2.2 Data information

​	In DataSummary.py file, we write DataSummary class with the summary function.

 To print the Data information in jupyter notebook we can get:

<img src="img/summary.png" alt="summary" style="zoom: 50%;" />

​	By looking at the returned values, we can see that there are a total of 761 cases in the dataset, each having 14 attributes. The specific names and data types of each attribute are listed below, with 'object' indicating text data. 

![overview](img/overview.png)

​	This is an overall overview of the data. In other words, it has 761 rows and 14 columns.

2.3 Attributes details

`biopics.csv` contains the following attributes:

| Attributes           | Definition                                                   |
| -------------------- | ------------------------------------------------------------ |
| `title`              | Title of the film.                                           |
| `site`               | URL from IMDB.                                               |
| `country`            | Country of origin.                                           |
| `year_released`      | Year of release.                                             |
| `box_office`         | Gross earnings at U.S. box office.                           |
| `director`           | Director of film.                                            |
| `number_of_subjects` | The number of subjects featured in the film.                 |
| `subject`            | The actual name of the featured subject.                     |
| `type_of_subject`    | The occupation of subject or reason for recognition.         |
| `race_known`         | Indicates whether the subject’s race was discernible based on background of self, parent, or grandparent. |
| `subject_race`       | Race of the subject.                                         |
| `person_of_color`    | Dummy variable that indicates person of color.               |
| `subject_sex`        | Sex of subject.                                              |
| `lead_actor_actress` | The actor or actress who played the subject.                 |




### 3.Exploratory Data Analysis (EDA)

3.1 Summary statistics

​	 Firstly we analysis the missing values in each attribute, with the miss_value function in DataExploration class. See details in DataAnalysis.py file, and the return results are:

<img src="img/miss_data.png" alt="miss_data" style="zoom:50%;" />

​	From the table above, there are 197 values missed in subject_race attribute and 7 values missed in lead_actor_actress attribute. Here the missing value means the data value is None.

​	To provide the summary statistics for each attribute, we define a visualize_data function in DataExploration class. We counted the occurrences of each data value in each attribute and presented them in the form of histograms. We first used Matplotlib to create the plots and then used Seaborn. The results are analyzed in detail in Section 3.2.

```python
def visualize_data(self,column_name):
  if column_name in self.dataset.columns:
    column_data = self.dataset[column_name]
    summary_stats = column_data.describe()

    if column_data.dtype == 'object':
      ## process the column with string(object) data type

      plt.figure(figsize=(8, 4))
      ## calculate frequency
      value_counts = column_data.value_counts().sort_values(ascending=False)

      ## visualize with Matplotlib
      plt.bar(value_counts.index, value_counts.values)
      plt.title(f"{column_name} Data Distribution (Matplotlib)")
      plt.xticks(rotation=45)
      plt.show()

      ## visualize with Seaborn
      plt.figure(figsize=(8, 4))
      sns.barplot(x=value_counts.index, y=value_counts.values)
      plt.title(f"{column_name} Data Distribution (Seaborn)")
      plt.xticks(rotation=45)
      plt.show()

    else:
      ## process the column with int data type
      ## visualize with Matplotlib
      plt.figure(figsize=(8, 4))
      plt.hist(column_data.dropna(), bins=20)
      plt.title(f"{column_name} Data Distribution (Matplotlib)")
      plt.show()

      ## visualize with Seaborn
      plt.figure(figsize=(8, 4))
      sns.histplot(data=column_data.dropna(), bins=20, kde=True)
      plt.title(f"{column_name} Data Distribution (Seaborn)")
      plt.show()

    else:
      summary_stats = None

      return summary_stats

```



3.2 Analysis for each attribute

​	

 1. Title 

    <img src="img/title_plt.png" alt="title_plt" style="zoom: 55%;" /><img src="/Users/youhengyu/Documents/personal/work/python-visual/Biopics_Analysis/img/title_sns.png" alt="title_sns" style="zoom: 55%;" />

​		  From the histogram, it can be observed that there are hardly any significant repetitions in the titles of biographical films. The maximum number of overlaps is four times, with only a few occurrences of three or two repetitions.

2. Site

   <img src="img/site_plt.png" alt="title_plt" style="zoom: 55%;" /><img src="img/site_sns.png" alt="title_plt" style="zoom: 55%;" />

3. Country

   <img src="img/country_plt.png" alt="title_plt" style="zoom: 65%;" /><img src="img/country_sns.png" alt="title_plt" style="zoom: 65%;" />

4. 



### 4.Inference

### 5.Conclusion

### Reference