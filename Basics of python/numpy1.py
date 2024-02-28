import pandas as pd

my_dict = {
    'Name': ['suman', 'raju', 'dhruva'],
    'Marks': [90, 98, 89]
}
df = pd.DataFrame(data=my_dict)
pic = df.plot.line(title='Marks')
pic = pic.get_figure()
pic.savefig('a.jpg')
