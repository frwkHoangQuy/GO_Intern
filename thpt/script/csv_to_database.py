import pandas as pd

from thpt.models import DiemThiTHPT


def insert_csv_to_db(file_path):
    chunksize = 10 ** 6
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        objs = []
        for _, row in chunk.iterrows():
            objs.append(DiemThiTHPT(
                sbd=row['sbd'],
                toan=row['toan'] if pd.notnull(row['toan']) else None,
                ngu_van=row['ngu_van'] if pd.notnull(row['ngu_van']) else None,
                ngoai_ngu=row['ngoai_ngu'] if pd.notnull(row['ngoai_ngu']) else None,
                vat_li=row['vat_li'] if pd.notnull(row['vat_li']) else None,
                hoa_hoc=row['hoa_hoc'] if pd.notnull(row['hoa_hoc']) else None,
                sinh_hoc=row['sinh_hoc'] if pd.notnull(row['sinh_hoc']) else None,
                lich_su=row['lich_su'] if pd.notnull(row['lich_su']) else None,
                dia_li=row['dia_li'] if pd.notnull(row['dia_li']) else None,
                gdcd=row['gdcd'] if pd.notnull(row['gdcd']) else None,
                ma_ngoai_ngu=row['ma_ngoai_ngu']
            ))
        DiemThiTHPT.objects.bulk_create(objs, batch_size=1000)  # batch_size dựa vào dung lượng của ram


insert_csv_to_db('dataset/diem_thi_thpt_2024.csv')
