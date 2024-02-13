from sqlalchemy import create_engine
import pandas as pd

try:
    # DataFrame'i yüklemek
    df = pd.read_parquet('C:\\Users\\user\\Desktop\\assigment\\data.parquet')

    # MySQL veritabanına bağlanma bilgilerini belirtin
    db_host = 'localhost'
    db_user = 'user'
    db_password = 'mysqltasks'
    db_name = 'MYSQL'
    schema_name = 'mysql'
    table_name = 'sensordata'

    # MySQL veritabanı bağlantı dizesi oluşturun
    db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

    # SQLAlchemy Engine oluşturun
    engine = create_engine(db_url)

    # DataFrame'i MySQL veritabanına aktarın
    df.to_sql(name='table_name', con=engine, if_exists='replace', index=False)
    print(f"DataFrame başarıyla {schema_name}.{table_name} tablosuna MySQL veritabanına aktarıldı.")


except Exception as e:
    print("DataFrame aktarımı sırasında bir hata oluştu:", e)
