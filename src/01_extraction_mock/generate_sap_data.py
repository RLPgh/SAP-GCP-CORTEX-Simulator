import os
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

def generate_sap_sales_data(num_orders=10000, output_dir="data_mock"):
    """
    Generates synthetic data for SAP tables: VBAK (Sales Document Header), 
    VBAP (Sales Document Item), and KNA1 (Customer Master).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    fake = Faker()
    Faker.seed(42)
    random.seed(42)
    
    print(f"Generating synthetic SAP data for {num_orders} orders...")

    # 1. Generate KNA1 (Customers)
    num_customers = max(1, num_orders // 10)  # Approx 10 orders per customer
    kna1_data = []
    customer_ids = []
    
    for i in range(num_customers):
        kunnr = f"CUST{str(i).zfill(6)}"
        customer_ids.append(kunnr)
        kna1_data.append({
            "KUNNR": kunnr,
            "NAME1": fake.company(),
            "LAND1": fake.country_code(),
            "ORT01": fake.city(),
            "REGIO": fake.state_abbr() if fake.country_code() == 'US' else fake.state()
        })
    
    df_kna1 = pd.DataFrame(kna1_data)
    
    # 2. Generate VBAK (Sales Document Header)
    vbak_data = []
    order_ids = []
    materials = [f"MAT{str(i).zfill(4)}" for i in range(1, 51)] # 50 generic materials
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2025, 12, 31)
    
    for i in range(num_orders):
        vbeln = f"ORD{str(i).zfill(7)}"
        order_ids.append(vbeln)
        order_date = fake.date_between(start_date=start_date, end_date=end_date)
        
        vbak_data.append({
            "VBELN": vbeln,
            "ERDAT": order_date.strftime("%Y%m%d"),
            "ERZET": fake.time(pattern="%H%M%S"),
            "KUNNR": random.choice(customer_ids),
            "NETWR": round(random.uniform(100.0, 10000.0), 2),
            "WAERK": "USD"
        })
        
    df_vbak = pd.DataFrame(vbak_data)
    
    # 3. Generate VBAP (Sales Document Items)
    vbap_data = []
    for vbeln in order_ids:
        # 1 to 5 items per order
        num_items = random.randint(1, 5)
        for pos_idx in range(num_items):
            posnr = str((pos_idx + 1) * 10).zfill(6) # 000010, 000020...
            qty = random.randint(1, 100)
            price = round(random.uniform(10.0, 500.0), 2)
            
            vbap_data.append({
                "VBELN": vbeln,
                "POSNR": posnr,
                "MATNR": random.choice(materials),
                "ARKTX": fake.catch_phrase(),
                "KWMENG": qty,
                "NETPR": price,
                "WAERK": "USD"
            })
            
    df_vbap = pd.DataFrame(vbap_data)

    # Export to CSV
    kna1_path = os.path.join(output_dir, "sap_kna1.csv")
    vbak_path = os.path.join(output_dir, "sap_vbak.csv")
    vbap_path = os.path.join(output_dir, "sap_vbap.csv")
    
    df_kna1.to_csv(kna1_path, index=False)
    df_vbak.to_csv(vbak_path, index=False)
    df_vbap.to_csv(vbap_path, index=False)

    print(f"Extraction successful!")
    print(f" - KNA1 generated: {len(df_kna1)} records ({kna1_path})")
    print(f" - VBAK generated: {len(df_vbak)} records ({vbak_path})")
    print(f" - VBAP generated: {len(df_vbap)} records ({vbap_path})")

if __name__ == "__main__":
    generate_sap_sales_data()
