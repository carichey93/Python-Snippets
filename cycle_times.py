def calculate_cycles(df):
  """ 
  Adds a new column 'Cycle' that contains the cycle time between different timestamps for each
  ID value 
  """
  
  df["Cycle"] = (
      df.groupby(["ID"])["Timestamp"]
          .diff()
          .apply(lambda x: x / np.timedelta64(1, "m"))
          .copy()
  )
  
  return df
