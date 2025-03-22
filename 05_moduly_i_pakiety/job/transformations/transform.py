def transform(df):
  return df[["Imię"]].drop_duplicates()
