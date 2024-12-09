import pandas as pd
from datetime import datetime
import os
def create_transaction_log():
    curr_month=datetime.now().strftime("%B_%Y")
    file_path=os.path.join(f'./artifacts/data/transaction_log/{curr_month}.xlsx')

    columns=['Code', 'Product', 'Sold', 'Purchased', 'Consumer', 'Date', 'Remarks']
    brand_names=['hind','straw','glass','spoon','bionomic','chuk','earthco','wonder','2d','kuber','gcdc']
    df=pd.DataFrame(columns=columns)

    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name=brand_names[0], index=False)
        df.to_excel(writer, sheet_name=brand_names[1], index=False)
        df.to_excel(writer, sheet_name=brand_names[2], index=False)
        df.to_excel(writer, sheet_name=brand_names[3], index=False)
        df.to_excel(writer, sheet_name=brand_names[4], index=False)
        df.to_excel(writer, sheet_name=brand_names[5], index=False)
        df.to_excel(writer, sheet_name=brand_names[6], index=False)
        df.to_excel(writer, sheet_name=brand_names[7], index=False)
        df.to_excel(writer, sheet_name=brand_names[8], index=False)
        df.to_excel(writer, sheet_name=brand_names[9], index=False)
        df.to_excel(writer, sheet_name=brand_names[10], index=False)
create_transaction_log()