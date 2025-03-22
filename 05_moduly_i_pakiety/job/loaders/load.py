def load(df, path):
  return df.to_json(path, orient="records", index=False, lines=True)
