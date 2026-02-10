import psycopg2
import pandas as pd
import os

hostname = "pg-84cb3be-projectinnovex89-ad26.h.aivencloud.com"
database = "defaultdb"
username = "avnadmin"
password =  os.getenv("DB_PASSWORD")
port = 20311

print("HOST USED:", hostname)
print("PORT USED:", port)

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=password,
        port=port,
        sslmode="require"   
    )

    print("PostgreSQL connection established successfully")

    cur = conn.cursor()
    cur.execute("SELECT version();")
    print("DB VERSION:", cur.fetchone())

    query = "SELECT * FROM retail.retail_sales_view;"
    df = pd.read_sql(query, conn)
    print(df.head())
    print(df.columns)

    
    df['sales_date'] = pd.to_datetime(df['sales_date'])
    print(df.dtypes)

   
    snapshot_date = df['sales_date'].max() + pd.Timedelta(days=1)
    print("Snapshot Date:", snapshot_date)

    rfm = df.groupby('customer_id').agg({
        'sales_date': lambda x: (snapshot_date - x.max()).days,  
        'sales_id': 'count',                                     
        'total_amount': 'sum'                                   
    }).reset_index()

    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']
    print(rfm.head())

    rfm['R_score'] = pd.qcut(rfm['recency'], 5, labels=[5,4,3,2,1])
    rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
    rfm['M_score'] = pd.qcut(rfm['monetary'], 5, labels=[1,2,3,4,5])
    print(rfm[['customer_id','recency','frequency','monetary','R_score','F_score','M_score']].head())

   
    rfm['RFM_Score'] = (
    rfm['R_score'].astype(str) +
    rfm['F_score'].astype(str) +
    rfm['M_score'].astype(str))

    print(rfm[['customer_id','RFM_Score']].head())
    def rfm_segment(row):
      
      if row['RFM_Score'] >= '444':
        return 'Champions'
      elif row['RFM_Score'] >= '344':
        return 'Loyal'
      elif row['RFM_Score'] >= '244':
        return 'Potential Loyalist'
      elif row['RFM_Score'] >= '144':
        return 'Hibernating'
      else:
        return 'At Risk'

    rfm['Segment'] = rfm.apply(rfm_segment, axis=1)

    print(rfm['Segment'].value_counts())

    segment_validation = rfm.groupby('Segment')['monetary'].mean().sort_values(ascending=False)
    print(segment_validation)

    rfm.to_csv(r"C:\rfm_project\data\rfm_output.csv", index=False)
    print("RFM results exported to rfm_analysis_results.csv")


except Exception as e:
    print("Connection failed")
    print(e)
