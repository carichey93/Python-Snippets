def add_plant_area(df, input_column, category_dict):
    for category, category_items in category_dict.items():
        df.loc[df[input_column].isin(category_list), "Category"] = category

    return df
