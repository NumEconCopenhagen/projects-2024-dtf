from types import SimpleNamespace
import pandas as pd

class data_project:
    
    def __init__(self, eco_api):
        self.eco_api = eco_api

    def calculate_percentage_changes(self):
        # Create an empty DataFrame to store the results
        percentage_changes = pd.DataFrame()

        # Define the period
        years = range(2004, 2023) 

        # Loop through each year and create the variable current_year_values and next_year_values
        for TID in years:
            if TID + 1 in self.eco_api.index:
                current_year_values = self.eco_api.loc[self.eco_api.index == TID, 'INDHOLD'].astype(float)
                next_year_values = self.eco_api.loc[self.eco_api.index == TID + 1, 'INDHOLD'].astype(float)

                # Calculate the percentage change for each variable
                change = (next_year_values.values - current_year_values.values) / current_year_values.values * 100

                # Create a new column in the results DataFrame for each year
                percentage_changes[f'{TID+1}'] = change

        # Rename the index-column to the true variable names
        Variables_names = ['Total_Turn_Over', 'Total_Meat', 'Total_Dairy', 'Total_Fruits', 'Total_Vegetables']
        percentage_changes.index = Variables_names

        # Transpose the dataframe so the years become the index column
        percentage_changes_transposed = percentage_changes.T
        percentage_changes_transposed = percentage_changes_transposed.rename_axis('TID')

        # Transform index column to numeric values
        percentage_changes_transposed.index = pd.to_numeric(percentage_changes_transposed.index)


  