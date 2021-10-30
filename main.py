import camelot as cm

input_pdf = cm.read_pdf("ast_sci_data_tables_sample.pdf", flavor="lattice", pages="1,2")

for n in input_pdf:
    print(n)

print(input_pdf[0].df)

df = input_pdf[0].df


df = df.reset_index(drop=True)

df.columns=['Names', 'Paperclips']

print(df)

df.to_csv('test.csv')

print('Ending...')