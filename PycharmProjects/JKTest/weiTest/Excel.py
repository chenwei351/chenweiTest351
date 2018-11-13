# -*- coding: UTF-8 -*-
import xlrd

data = xlrd.open_workbook('/Users/jumei/desktop/文件1.xlsx')
# table=data.sheets()[0]
table=data.sheet_by_name(u'工作表1')

t= table.col_values(0)
l=[]
a='id, partner_order_id, order_id, merchant_no, store_no, logistic_no, warehouse_no, out_store_no, logistic_id, tracking_no, effective_period, delivery_status, shipping_time, deliver_time, pickup_time, retention_time, send_area_code, province_code, city_code, district_code, street_code, total_price, total_deal_price, after_discount_price, weight, distance, delivery_type, user_id, receiver_name, address_id, address, street, change_status_reason, handling_suggestion, remark, delay_time, need_delivery_finish_time, create_user, create_time, update_user, update_time'
for i in range(len(a)-1):
    b=a.split(", ")
    l=l.append(b)
print l