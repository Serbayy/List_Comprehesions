Ödev 3 List Comprehension

## Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
harfe çeviriniz ve başına NUM ekleyiniz

import seaborn  as sns

df = sns.load_datadet ('car_crashes')

df.columns

for col in df.columns:
    print (col.upper())
    new_columns = ['NUM-' + col.upper() if df(col) dtypes in (float), 'int'] else col.upper() for col in df.columns]
print(new_columns)

## Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
değişkenlerin isimlerinin sonuna "FLAG" yazın.

 ##  import seaborn as sns
        df = sns.load_dataset('car-crashes')
        df.columuns [ col.upper() for col in df.columns ]
        df.columns = [ col + 'FLAG_' if 'NO' not in col else col for col in df.columns ]

        print (new_columns)


## Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz

## import seaborb as sns

        df = sns.load_dataset ('car crashes')
        df.columuns

        og.list = ['abbrev', 'no previous'}
        new_cols =  [col for col in df.columns if col not in og_list]
        new_df = df(new_cols)
        print (new_df)