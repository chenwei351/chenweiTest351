#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import  data
def resql():
    filed_name = "(`partner_order_id`, `order_id`, `merchant_no`, `store_no`, `logistic_no`, `warehouse_no`, `out_store_no`, `logistic_id`, `tracking_no`, `effective_period`, `delivery_status`, `shipping_time`, `deliver_time`, `pickup_time`, `retention_time`, `send_area_code`, `province_code`, `city_code`, `district_code`, `street_code`, `total_price`, `total_deal_price`, `after_discount_price`, `weight`, `distance`, `delivery_type`, `user_id`, `receiver_name`, `address_id`, `address`, `street`, `reject_conn_address`, `reject_conn_user_tel`, `reject_conn_user_name`, `change_status_reason`, `handling_suggestion`, `remark`, `delay_time`, `need_delivery_finish_time`, `create_user`, `create_time`, `update_user`, `update_time`)"

    ins="INSERT INTO `shoppe_delivery_info` "
    va = "VALUES"
    v=data.data()
    sql = ins +filed_name + va +str(v)

    # print sql
    return  sql