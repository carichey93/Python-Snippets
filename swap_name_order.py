def swap_name_order(df):
  """Swap from Last Name, First Name to First Name Last Name"""
  df["Full_Name"] = df["Full_Name"].str.replace(
    r"^(\w+),\s+(\w+)\*?", "\\2 \\1", regex=True  
  )
  return df
