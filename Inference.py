import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Inference:
    def __init__(self, dataset_path):
        self.dataset = pd.read_csv(dataset_path)#,encoding='gbk')

    def box_year_analysis(self):
        """
        Analyze the total box office earnings for movies in different years.

        Returns:
        - box_by_year (Series): A Pandas Series containing the total box office earnings for each year.
        """
        # Assuming you have 'year_released' and 'box_office' columns in your dataframe
        save_path = "img/box_by_year_"
        if 'year_release' in self.dataset.columns and 'box_office' in self.dataset.columns:
            print("Now start analysis")
            # Group the data by year and calculate the total box office earnings for each year
            box_by_year = self.dataset.groupby('year_release')['box_office'].sum().sort_index()
            
            # Plot the total box office earnings for each year using Matplotlib
            plt.figure(figsize=(10, 6))
            plt.bar(box_by_year.index, box_by_year.values)
            plt.title("Total Box Office Earnings by Year (Matplotlib)")
            plt.xlabel("Year")
            plt.ylabel("Total Box Office Earnings")
            plt.xticks(rotation=45)
            plt.savefig(save_path+"sns.png",bbox_inches='tight')       
            plt.show()
            
            # Plot the total box office earnings for each year using Seaborn
            plt.figure(figsize=(10, 6))
            sns.barplot(x=box_by_year.index, y=box_by_year.values)
            plt.title("Total Box Office Earnings by Year (Seaborn)")
            plt.xlabel("Year")
            plt.ylabel("Total Box Office Earnings")
            plt.xticks(rotation=45)
            plt.gca().xaxis.set_major_locator(plt.MultipleLocator(11))
            plt.savefig(save_path+"sns.png",bbox_inches='tight')
            plt.show()
            
            return box_by_year
        else:
            return None

    def gender_analysis_by_year(self):
        """
        Analyze the number of male and female-oriented movies over the years.

        Returns:
        - gender_by_year (DataFrame): A Pandas DataFrame containing the count of Male and Female-oriented movies for each year.
        """
        save_path = "img/gender_by_year_"

        if 'year_release' in self.dataset.columns and 'subject_sex' in self.dataset.columns:
            print("Now start gender analysis")

            # Filter the dataset to include only Male and Female subjects
            gender_filtered = self.dataset[self.dataset['subject_sex'].isin(['Male', 'Female'])]

            # Group the filtered data by year and subject sex and count the occurrences
            gender_by_year = gender_filtered.groupby(['year_release', 'subject_sex']).size().unstack().fillna(0)

            # Plot the gender analysis using Seaborn
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=gender_by_year, x='year_release', y='Male', label='Male')
            sns.lineplot(data=gender_by_year, x='year_release', y='Female', label='Female')
            plt.title("Gender Analysis by Year (Seaborn)")
            plt.xlabel("Year")
            plt.ylabel("Number of Movies")
            plt.xticks(rotation=45)
            plt.savefig(save_path+"sns.png", bbox_inches='tight')
            plt.show()

            return gender_by_year

        else:
            return None
    


