# -*- coding: UTF-8 -*-
import random
import  reject
def data():
    time1="2018-09-17 14:50:26"

    a=random.randint(0,999999)

    partner_order_id=str(1033000000+a)

    o = 'E00000001'
    order_id=o+str(a)

    merchant_no="180700002"

    s=['ESTO1808660','ESTO1802417','ESTO1807546']
    i=random.randint(0,2)
    store_no=str(s[i])

    warehouse_no="TSN1"

    out_store_no="c6b83970dc32052a7d4be4b5b6fab0a9"

    # lid=[507,1371,1372,5]
    # j=random.randint(0,len(lid)-1)
    logistic_id ="507"
    # print logistic_id

    if logistic_id== "507" :
        logistic_no ='dada'
    elif logistic_id == "1372":
        logistic_no = 'SF'
    elif logistic_id == "1371":
        logistic_no='jishuSF'
    else: logistic_no='yunda'
    # print logistic_no
    tracking_no=str(a+1000*a+10000000*a)
    # print tracking_no
    effective_period="0"
    de = [800,1300,1500,900,800,800,800,800,800,800,]
    d=random.randint(0,len(de)-1)
    delivery_status=str(de[d])
    # delivery_status = "1300"
    # print delivery_status

    #出库时间
    shipping_time=time1
    #妥投时间
    deliver_time=time1
    #取件时间
    pickup_time=time1
    # 滞留时间
    retention_time=time1

    if delivery_status == "1300" or delivery_status == "1500":
        deliver_time =time1
    # print  deliver_time

    scode=[110101,510134,110105,510107,510101,510105,110107]
    #北京东城区 成都高新区 北京市朝阳区 成都武侯区 成都市辖区 成都市青羊区 北京石景山区
    saddress =""
    s=random.randint(0,len(scode)-1)
    pcode=[11,51,11,51]
    j=random.randint(0,len(pcode)-1)
    send_area_code=str(scode[s])
    province_code=str(pcode[j])
    # print province_code
    city_code="01"
    dcode=[01,05,07,34]
    district_code=str(pcode[j]*10000+01*100+dcode[j])
    street_code=""
    if scode == 110101:
        saddress = "北京东城区"
    elif scode == 510134:
        saddress = "成都高新区"
    elif scode == 110105:
        saddress = "北京市朝阳区"
    elif scode == 510107:
        saddress = "成都武侯区"
    elif scode == 510101:
        saddress = "成都市辖区"
    elif scode == 510105:
        saddress = "成都市青羊区"
    elif scode == 110107:
        saddress = "北京石景山区"
    # print district_code
    if district_code =="510134":
        address = '四川省-成都市-高新区 天府软件园G区'
    elif district_code == "510101":
        address = '四川省-成都市-市辖区  成都市武侯区天府大道北段1199号'
    elif district_code == "510105":
        address = '四川省-成都市-青羊区 成都市青羊区日月大道一段978号'
    elif district_code == "510107" :
        address = '四川省-成都市-武侯区 成都市武侯区晋阳路269号'
    elif district_code == "110101":
        address = '北京市-市辖区-东城区 北京市东城区崇文门外大街5号'
    elif district_code == "110105":
        address = '北京市-市辖区-朝阳区 北京市朝阳区阜通东大街59号'
    elif district_code == "110107" :
        address = '北京市-市辖区-石景山区 北京市石景山区阜石路165号'
    elif district_code == "110134" :
        district_code ="510134"
        address = '四川省-成都市-高新区 天府软件园G区'
    # print  address
    address_id=""

    street=""
    receiver_name="微微"
    user_id=""

    #包裹重量
    w=[3.22,8,10,17,33,50,0.5,1,2,22]

    dis=[0.5,0.1,1,1.5,1.9,2,2.5,3,3.6,5]

    k=random.randint(0,len(w)-1)
    weight=str(w[k])
    # print weight
    # print send_area_code
    delivery_type="2"
    distance = "0"
    # 极速达配送距离
    # 当发货地址和收获地址的城市code一样，且 快递公司是极速顺丰和达达时更改订单是极速达订单
    # 重量变成1

    if  logistic_id=="507" or logistic_id == "1371" :
        weight ="1"
        distance=str(dis[k])
        delivery_type ="3"
    # print distance
    # print delivery_type
    #状态改变原因
    change_status_reason=""
    remark=""
    #丢失处理意见
    handling_suggestion=""
    delay_time="0"
    need_delivery_finish_time=time1

    create_user="wei"
    create_time=time1
    update_user="wei"
    update_time=time1

    #价格
    #包裹商品总金额
    t=[350,260,100,999,5,60,88,1314,520]
    k=random.randint(0,len(t)-1)
    total_price=str(t[k])
    # print total_price
    # 包裹折后金额(含运费),即用户应付金额
    total_deal_price=str(t[k]/2+2)
    # print total_deal_price
    # 包裹折后金额
    after_discount_price=str(t[k]/2)
    # print after_discount_price

    reject_conn_user_tel="0"
    reject_conn_user_name="商家"
    reject_conn_address = saddress
    # '拒收取件地址',
    if store_no == 'ESTO1807546' and delivery_type != "3":
        reject_conn_address = "天津市-市辖区-武清区 天津市武清区大王古庄镇京滨工业园古达路41号"
        reject_conn_user_name="天津聚美"

    # '拒收取件联系电话',
        reject_conn_user_tel ="4001238888"
    # print  reject_conn_address
    # print  store_no
    shipping_no = str(random.randint(0,999999999))
    reject_order_no = "JMZG"+str(shipping_no)
    reject_status ="1"
    reject_tracking_no = "1"+tracking_no
    reject_type="1"
    if reject_conn_user_name =="天津聚美":
        reject_type="2"
    # 是否取消

    identification=str(random.randint(0,1))
    # 快递费
    if identification =="1":
        courier_fee="10"
        deduct_fee = "0"
    #取消违约金
    elif identification=="0" and logistic_id == "507":
        deduct_fee="2"
        courier_fee = "0"
        delivery_status = '350'



    if delivery_status =="1300":
        sql_name = "( `order_no`, `tracking_no`, `warehouse_no`, `logistic_id`, `logistic_no`, `shipping_no`, `reject_order_no`, `reject_tracking_no`, `reject_status`, `reject_address`, `reject_type`, `create_time`, `create_user`, `update_time`, `update_user`, `remark`)"

        # sql_value = " ( 'E000000017999', '444054845999', '180700002', '1372', '', '10332841233', 'JMZG201908085', '', '1', '', '1', '2018-08-08 15:20:28', 'weic', '2018-08-08 15:20:28', 'weic', 'test')"
        sql_value = "('" + order_id + "','" + tracking_no + "','" + warehouse_no + "','" + logistic_id + "','" + logistic_no + "','" + shipping_no + "','" + reject_order_no + "','" + reject_tracking_no + "','" + reject_status + "','" + reject_conn_address + "','" + reject_type + "','" + create_time + "','" + create_user + "','" + create_time + "','" + update_user + "','" + remark + "')"
        print sql_value
        sql_reject = "INSERT INTO `shoppe_reject_info`" + sql_name + "VALUES" + sql_value

        reject.db_reject(sql_reject)

    if logistic_id == "507" :
        sql_name1="(`logistic_id`, `tracking_no`, `order_no`, `store_no`, `merchant_no`, `logistic_name`, `deliver_time`, `cancel_time`, `order_time`, `distance`, `deduct_fee`, `courier_fee`, `identification`, `create_time`, `create_user`, `update_time`, `update_user`)"

        sql_value1 = "('" + logistic_id + "','" + tracking_no + "','" + order_id + "','" + store_no + "','" + merchant_no + "','" + logistic_id + "','" + deliver_time + "','" + deliver_time + "','" + deliver_time + "','" + distance + "','" + deduct_fee + "','" + courier_fee + "','" + identification + "','" + create_time + "','" + update_user + "','" + update_time +"','" + update_user+"')"
        print sql_value1
        sql_yufu = "INSERT INTO `jishuda_deduct_fee`" + sql_name1 +"VALUES" + sql_value1
        reject.db_reject(sql_yufu)


    # '拒收取件联系人',


    value = "('"+partner_order_id+"','"+ order_id+"','"+ merchant_no+"','"+ store_no+"','"+logistic_no+"','"+ warehouse_no+"','"+ out_store_no+"','"+logistic_id+"','"+ tracking_no+"','"+ effective_period+"','"+delivery_status+"','"+ shipping_time+"','"+ deliver_time+"','"+ pickup_time+"','"+retention_time+ "','"+ send_area_code+"','"+ province_code+"','"+ city_code+"','"+district_code+"','"+ street_code+"','"+ total_price+"','"+ total_deal_price+"','"+after_discount_price+"','"+ weight+"','"+ distance+"','"+ delivery_type+"','"+user_id+"','"+ receiver_name+"','"+ address_id+"','"+ address+"','"+ street+"','"+reject_conn_address+"','"+ reject_conn_user_tel+"','"+reject_conn_user_name+"','"+ change_status_reason+"','"+handling_suggestion+"','"+ remark+"','"+ delay_time+ "','"+ need_delivery_finish_time+ "','"+create_user+"','"+create_time+"','"+ update_user+"','"+ update_time+"')"
    return  value
