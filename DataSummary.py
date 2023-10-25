import pandas as pd

class DataSummary:
    def __init__(self, dataset_path):
        self.dataset = pd.read_csv(dataset_path,encoding='gbk')

    def get_summary(self):
        """
        calculate the number of use cases of the dataset
        calculate the numbre of attributes of each case
        and get the data types of each attribute
        
        Parameters:
        - self: The instance of the class with dataset.
        
        Return:
        - the number of use cases(int),attributes of each case(int), and the type for each attribute(DataFrame)

        """
        num_cases = len(self.dataset)
        num_attributes = len(self.dataset.columns)
        attribute_data_types = self.dataset.dtypes
        return num_cases, num_attributes, attribute_data_types

if __name__ == "__main__":
    dataset_path = "biopics.csv" 
    data_summary = DataSummary(dataset_path)
    num_cases, num_attributes, attribute_data_types = data_summary.get_summary()

    print(f"Number of Cases (Examples): {num_cases}")
    print(f"Number of Attributes: {num_attributes}")
    print("\nAttribute Data Types:")
    print(attribute_data_types)
