import pandas as pd

data = pd.read_csv("star2_dwarf.csv")

data = data.dropna()
print(data.dtypes)


data["Radius"] = 0.102763*  data["Radius"]

data['Mass']=data['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

data['Mass'] = 0.000954588* data['Mass']

data.to_csv("conv_data.csv")
