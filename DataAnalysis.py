import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataExploration:
    def __init__(self, dataset_path):
        self.dataset = pd.read_csv(dataset_path,encoding='gbk')
        
    def preprocess(self):
        """
        Preprocess the 'box_office' column in the given dataframe.

        This function preprocesses the 'box_office' column in the given dataframe by converting
        string currency values to integer values. It removes symbols, spaces, and converts values 
        like '$56.7M' to 56700000 and '$537K' to 537000. The preprocessed data is saved as a new 
        column in the DataFrame with the name specified by 'output_column_name'.
        """
        def preprocess_box_office(box_office_str):
            if len(box_office_str) > 1:
                box_office_str = box_office_str.replace("$", "").replace(",", "").replace(" ", "")
                if box_office_str.endswith("M"):
                    # Example: $56.7M
                    box_office_int = int(float(box_office_str[:-1]) * 1000000)
                elif box_office_str.endswith("K"):
                    # Example: $537K
                    box_office_int = int(float(box_office_str[:-1]) * 1000)
                else:
                    box_office_int = int(box_office_str)
                return box_office_int
            else:
                return 0
        
        self.dataset['box_office'] = self.dataset['box_office'].apply(preprocess_box_office)
        self.dataset.to_csv("preprocessed_dataset.csv", index=False) 
        print("Finished preprocess and saved as preprocessed_dataset.csv")
        return self.dataset['box_office'] 
    
    

    def miss_value(self):
        """
        Perform missing value analysis on a Pandas DataFrame.
        
        Parameters:
            - self: The instance of the class with dataset.
            
        Returns:
            - missing_values (DataFrame): A DataFrame summarizing missing values, including columns with missing values, the count of missing values, and the percentage of missing values.

        """
        dataframe = self.dataset
        missing_values = pd.DataFrame(
            {
                 'Column Name': dataframe.columns,
                'Missing Values': dataframe.isnull().sum(),
                'Missing Percentage': dataframe.isnull().mean() * 100
        })
        print("\n Missing Value Analysis")
        # print(missing_values)
        return missing_values
    
    def get_column_names(self):
        """
          Get the names of all columns in a Pandas DataFrame.
        """
        column_names = self.dataset.columns.tolist()
        return column_names

    
    def visualize_data(self,column_name):
        """
         Get summary statistics and visualize the data distribution for a specific column in a Pandas DataFrame.
         
         Parameters:
             - self: The instance of the class with dataset.
             - column_name (str): The name of the column for which summary statistics and visualization are needed.
             
         Returns:
             - summary_stats (Series): A Pandas Series containing summary statistics for the specified column.

            
         Description:
            This function takes a Pandas DataFrame and the name of a specific column as input and returns a
            Pandas Series containing summary statistics for that column. It also visualizes the data distribution
            of the column using a countplot for text columns.

        """
        save_filepath = f"img/{column_name}_"
        if column_name in self.dataset.columns:
            column_data = self.dataset[column_name]
            summary_stats = column_data.describe()
                
            if column_data.dtype == 'object':
                ## process the column with string(object) data type
                
                plt.figure(figsize=(8, 4))
                ## calculate frequency
                value_counts = column_data.value_counts().sort_values(ascending=False)
                if column_name =="country":
                     value_counts = value_counts[value_counts.index.isin(['US', 'Canada','UK'])]

                ## visualize with Matplotlib
                plt.bar(value_counts.index, value_counts.values)
                plt.title(f"{column_name} Data Distribution (Matplotlib)")
                plt.xticks(rotation=45)
                plt.savefig(save_filepath+"plt.png",bbox_inches='tight')
                plt.show()
                
            
                ## visualize with Seaborn
                plt.figure(figsize=(8, 4))
                sns.barplot(x=value_counts.index, y=value_counts.values)
                plt.title(f"{column_name} Data Distribution (Seaborn)")
                plt.xticks(rotation=45)
                plt.savefig(save_filepath+"sns.png",bbox_inches='tight')
                plt.show()
                
                
            else:
                ## process the column with int data type
                ## visualize with Matplotlib
                plt.figure(figsize=(8, 4))
                plt.hist(column_data.dropna(), bins=20)
                plt.title(f"{column_name} Data Distribution (Matplotlib)")
                plt.savefig(save_filepath+"plt.png",bbox_inches='tight')
                plt.show()
                
                ## visualize with Seaborn
                plt.figure(figsize=(8, 4))
                sns.histplot(data=column_data.dropna(), bins=20, kde=True)
                plt.title(f"{column_name} Data Distribution (Seaborn)")
                plt.savefig(save_filepath+"sns.png",bbox_inches='tight')
                plt.show()
                
                
        else:
            summary_stats = None
        
        return summary_stats
        
      

if __name__ == "__main__":
    dataset_path = "biopics.csv" 
    data_explore = DataExploration(dataset_path)

