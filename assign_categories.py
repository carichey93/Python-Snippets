def add_plant_area(df, input_column, category_dict):
    """ 
    Creates a new column called "Category" in the dataframe and each rows value
    is based on matched values from a dictionary of lists.
    """
    for category, category_items in category_dict.items():
        df.loc[df[input_column].isin(category_list), "Category"] = category

    return df
