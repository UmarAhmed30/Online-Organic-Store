from flask import Flask,render_template,request,url_for
from flask_cors import CORS
from datetime import datetime

import cx_Oracle

app = Flask(__name__)
CORS(app)

farmer_id = None
farmer_name = None

buyer_id = None
buyer_name = None

cart_id = None
total_price=None

# Homepage

@app.route('/')
def index():
    return render_template ("homepage.html")


# Directs to Farmer Sign-in

@app.route('/to_farmer_signin')
def to_fsignin():
    return render_template ("farmer_signin.html")


# Directs to Buyer Sign-in

@app.route('/to_buyer_signin')
def to_bsignin():
    return render_template ("buyer_signin.html")


# Directs to Farmer Sign-up

@app.route('/to_farmer_signup')
def to_fsignup():
    return render_template ("farmer_signup.html")


# Directs to Buyer Sign-up    

@app.route('/to_buyer_signup')
def to_bsignup():
    return render_template ("buyer_signup.html")


# Farmer Validation

@app.route('/farmer_validation',methods=["POST"])
def farmer_validate():
    global farmer_id
    global farmer_name

    farmer_email_id = request.form["email_id"]
    farmer_identity = request.form["farmer_identity"]

    print(farmer_email_id)
    print(farmer_identity)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """ select email_id from farmer """
    cur.execute(sql)

    emailid_list = cur.fetchall()

    print(emailid_list)
    
    for i in emailid_list:
            if i[0] == farmer_email_id:
                sql = """ select farmer_id from farmer where email_id=:x_email_id"""
                cur.execute(sql,({'x_email_id':farmer_email_id}))
                y = cur.fetchone()

                if y[0] == int(farmer_identity):
                    sql = """ select name from farmer where email_id=:x_email_id """
                    cur.execute(sql,{'x_email_id':farmer_email_id})
                    z = cur.fetchone()
                    print(z[0])

                    farmer_name=z[0]
                    farmer_id = int(farmer_identity)
                    print(farmer_id)
                    cur.close()
                    return render_template("farmer_page.html",farmer_name=z[0])
                else:
                    cur.close()
                    return render_template("farmer_signin.html",flag=1)

    cur.close()
    return render_template("farmer_signin.html",flag=1)



# Buyer Validation

@app.route('/buyer_validation',methods=["POST"])
def buyer_validate():
    global buyer_id
    global buyer_name

    buyer_email_id = request.form["email_id"]
    buyer_identity = request.form["buyer_identity"]

    print(buyer_email_id)
    print(buyer_identity)

    conn = cx_Oracle.connect('Umar/ahmed3633@localhost/orcl')
    cur = conn.cursor()

    sql = """select email_id from buyer"""
    cur.execute(sql)

    emailid_list = cur.fetchall()
    print(emailid_list)

    for i in emailid_list:
        if i[0] == buyer_email_id:
                print(i[0])
                sql = """select buyer_id from buyer where email_id=:x_buyer_email_id"""
                cur.execute(sql,{'x_buyer_email_id':buyer_email_id})
                y = cur.fetchone()
                print(y[0])

                if y[0] == int(buyer_identity):
                    print(y[0])
                    sql = """ select name from buyer where email_id=:x_email_id """
                    cur.execute(sql,{'x_email_id':buyer_email_id})
                    z = cur.fetchone()
                    print(z[0])

                    buyer_name=z[0]
                    buyer_id = int(buyer_identity)
                    print(buyer_id)
                    cur.close()
                    return render_template("buyer_page.html",buyer_name=z[0])
                else:
                    cur.close()
                    return render_template("buyer_signin.html",flag=1)
    
    cur.close()
    return render_template("buyer_signin.html",flag=1)

# Fetches form value into farmer DB

@app.route('/farmer_signup',methods=["POST"])
def f_signup():
    farmer_name = request.form["f_name"]
    farmer_age = request.form["f_age"]
    farmer_gender = request.form["f_gender"]
    farmer_exp = request.form["f_exp"]
    farmer_land_area = request.form["f_landarea"]
    farmer_contact = request.form["f_contact"]
    farmer_email_id = request.form["f_email"]
    farmer_door_no = request.form["f_doorno"]
    farmer_street = request.form["f_street"]
    farmer_locality = request.form["f_locality"]
    farmer_city = request.form["f_city"]
    farmer_pincode = request.form["f_pincode"]

    print(farmer_name,farmer_age,farmer_gender,farmer_contact,farmer_email_id,farmer_exp,farmer_land_area,farmer_door_no,farmer_street,farmer_locality,farmer_city,farmer_pincode)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """insert into farmer (name,age,gender,contact,email_id,experience,land_area,door_no,street,locality,city,pincode) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)"""
    cur.execute(sql,[farmer_name,farmer_age,farmer_gender,farmer_contact,farmer_email_id,farmer_exp,farmer_land_area,farmer_door_no,farmer_street,farmer_locality,farmer_city,farmer_pincode])

    sql = """select farmer_id from farmer where email_id=:x_farmer_email_id"""
    cur.execute(sql,{'x_farmer_email_id':farmer_email_id})
    y = cur.fetchone()

    sql = """select name from farmer where email_id=:x_farmer_email_id"""
    cur.execute(sql,{'x_farmer_email_id':farmer_email_id})
    z = cur.fetchone()

    print(y[0])
    print(z[0])

    conn.commit()
    cur.close()

    return render_template("farmeridpage.html",farmer_id=y[0],fname=z[0])


# Fetches form value into buyer DB

@app.route('/buyer_signup',methods=["POST"])
def b_signup():
    buyer_name = request.form["b_name"]
    buyer_age = request.form["b_age"]
    buyer_gender = request.form["b_gender"]
    buyer_contact = request.form["b_contact"]
    buyer_email_id = request.form["b_email"]
    buyer_door_no = request.form["b_doorno"]
    buyer_street = request.form["b_street"]
    buyer_locality = request.form["b_locality"]
    buyer_city = request.form["b_city"]
    buyer_pincode = request.form["b_pincode"]

    print(buyer_name,buyer_age,buyer_gender,buyer_contact,buyer_email_id,buyer_door_no,buyer_street,buyer_locality,buyer_city,buyer_pincode)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """insert into buyer (name,age,gender,contact,email_id,door_no,street,locality,city,pincode) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"""
    cur.execute(sql,[buyer_name,buyer_age,buyer_gender,buyer_contact,buyer_email_id,buyer_door_no,buyer_street,buyer_locality,buyer_city,buyer_pincode])

    sql = """select buyer_id from buyer where email_id=:x_buyer_email_id"""
    cur.execute(sql,{'x_buyer_email_id':buyer_email_id})
    y = cur.fetchone()

    sql = """select name from buyer where email_id=:x_buyer_email_id"""
    cur.execute(sql,{'x_buyer_email_id':buyer_email_id})
    z = cur.fetchone()

    print(y[0])
    print(z[0])

    conn.commit()
    cur.close()

    return render_template("buyeridpage.html",buyer_id=y[0],bname=z[0])

# My Stock

@app.route('/to_myStock')
def to_myStock():
    global farmer_id
    return_data = {'stock_id':[]}
    #{
    # 'stock_id':[
    #       {'id':4000,'products':[{'name':'','quantity':''},{'name':'','quantity':''}]},
    #       {'id':4043}]
    # }

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """select stock_id from stock where farmer_id=:x_farmer_id"""
    cur.execute(sql,{'x_farmer_id':farmer_id})
    stock_list = cur.fetchall()
    
    for i in stock_list:
        return_data['stock_id'].append({'id':i[0],'products':[]})

    

    for i in range(len(return_data['stock_id'])):
        sql = """select name,available_quantity from holds where stock_id=:x_stock_id"""
        cur.execute(sql,{'x_stock_id':return_data['stock_id'][i]['id']})
        y = cur.fetchall()
        #[('Tomato', 90.0), ('Apple', 120.5)]
        for j in range(len(y)):
            return_data['stock_id'][i]['products'].append({'name':y[j][0],'quantity':y[j][1]})

        
    print(return_data)

    conn.commit()
    cur.close()

    return render_template("myStockPage.html",db_data=return_data)


@app.route('/my_cart')
def my_cart():
    global cart_id
    global buyer_name
    global total_price

    sum=0

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """ select name,quantity,price from cart where cart_id=:1 and buyer_id=:2"""
    cur.execute(sql,{'1':cart_id,'2':buyer_id})
    y = cur.fetchall()

    print(y)

    for i in y:
        sum=sum+i[2]

    print(sum)

    total_price=float(sum)

    print(total_price)

    conn.commit()
    cur.close()

    return render_template("myCart.html",cart_list=y,b_name=buyer_name,total=sum)

# Add stock

@app.route('/to_addStock')
def to_addStock():
    return render_template("stock.html")

@app.route('/add_stock',methods=["POST"])
def addStock():
    global farmer_id

    stock_capacity = request.form["s_cap"]
    stock_door_no = request.form["s_doorno"]
    stock_street = request.form["s_street"]
    stock_locality = request.form["s_locality"]
    stock_city = request.form["s_city"]
    stock_pincode = request.form["s_pincode"]

    print(stock_capacity,stock_door_no,stock_street,stock_locality,stock_city,stock_pincode,farmer_id)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """insert into stock (capacity,door_no,street,locality,city,pincode,farmer_id) values (:1,:2,:3,:4,:5,:6,:7)"""
    cur.execute(sql,[stock_capacity,stock_door_no,stock_street,stock_locality,stock_city,stock_pincode,farmer_id])

    sql = """select stock_id from stock where farmer_id=:x_farmer_id"""
    cur.execute(sql,{'x_farmer_id':farmer_id})
    y = cur.fetchall()

    print(y[0])

    conn.commit()
    cur.close()

    return render_template("farmer_page.html",suc=1)

@app.route('/to_updateStock')
def to_updateStock():
    return render_template("update_stock.html")

@app.route('/stock_update',methods=["POST"])
def stock_update():

    stock_id = request.form["s_id"]
    product_name = request.form["p_name"]
    p_avail = request.form["p_avail"]

    print(type(stock_id),product_name,type(p_avail))

    p1 = int(p_avail)
    p2 = int(stock_id)
    print(product_name)

    print(p1,p2)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()
    print(conn)
    print(cur)
    print("CP1")

    sql = """ select count(available_quantity) from holds where stock_id=:1 and name=:2 """
    cur.execute(sql,{'1':stock_id,'2':product_name})
    q=cur.fetchone()

    count=q[0]

    if count==0:
        sql = """ select product_id from product where name=:1 """
        cur.execute(sql,{'1':product_name})
        w=cur.fetchone()

        prod_id=w[0]

        sql = """ insert into holds (stock_id,product_id,name,available_quantity) values (:1,:2,:3,:4) """
        cur.execute(sql,[stock_id,prod_id,product_name,p_avail])

        conn.commit()
        cur.close()
        return render_template("farmer_page.html",s=1)

    else:
        sql = """update holds set available_quantity=:1 where name=:2 and stock_id=:3"""
        cur.execute(sql,{':1':p1,':2':product_name ,':3':p2 })
        print("CP2")

        conn.commit()
        cur.close()
        return render_template("farmer_page.html",success=1)

@app.route('/to_updateaddress1')
def to_up_add():
    return render_template("update_address1.html")


@app.route('/to_updateaddress2')
def to_upd_add():
    return render_template("update_address2.html")


@app.route('/to_updatelocation')
def to_up_loc():
    return render_template("update_stock_loc.html")


@app.route('/location_update',methods=["POST"])
def loc_update():
    
    s_id = request.form["s_id"]
    s_cap = request.form["s_cap"]
    s_doorno = request.form["s_doorno"]
    s_street = request.form["s_street"]
    s_locality = request.form["s_locality"]
    s_city = request.form["s_city"]
    s_pincode = request.form["s_pincode"]

    print(s_id,s_cap,s_doorno,s_street,s_locality,s_city,s_pincode)

    p1 = int(s_id)
    p2 = int(s_cap)
    p3 = int(s_doorno)
    p4 = int(s_pincode)

    print(p1,p2,p3,p4)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """update stock set capacity=:1 where stock_id=:2"""
    cur.execute(sql,{':1':p2,':2':p1})

    sql = """update stock set door_no=:3 where stock_id=:4"""
    cur.execute(sql,{':1':p3,':2':p1})

    sql = """update stock set street=:5 where stock_id=:6"""
    cur.execute(sql,{':1':s_street,':2':p1})

    sql = """update stock set locality=:7 where stock_id=:8"""
    cur.execute(sql,{':1':s_locality,':2':p1})

    sql = """update stock set city=:9 where stock_id=:10"""
    cur.execute(sql,{':1':s_city,':2':p1})

    sql = """update stock set pincode=:11 where stock_id=:12"""
    cur.execute(sql,{':1':p4,':2':p1})

    conn.commit()
    cur.close()
    return render_template("farmer_page.html",succe=1)


@app.route('/address_update',methods=["POST"])
def add_update():
    global farmer_id

    f_doorno = request.form["f_doorno"]
    f_street = request.form["f_street"]
    f_locality = request.form["f_locality"]
    f_city = request.form["f_city"]
    f_pincode = request.form["f_pincode"]

    print(f_doorno,f_street,f_locality,f_city,f_pincode)

    p1 = int(f_doorno)
    p2 = int(f_pincode)

    print(p1,p2)
    print(type(p1),type(p2))

    print(type(f_doorno))
    print(type(f_street))
    print(type(f_locality))
    print(type(f_city))
    print(type(f_pincode))

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """update farmer set door_no=:1 where farmer_id=:2"""
    cur.execute(sql,{':1':p1,':2':farmer_id})

    sql = """update farmer set street=:3 where farmer_id=:4"""
    cur.execute(sql,{':3':f_street,':4':farmer_id})

    sql = """update farmer set locality=:5 where farmer_id=:6"""
    cur.execute(sql,{':5':f_locality,':6':farmer_id})

    sql = """update farmer set city=:7 where farmer_id=:8"""
    cur.execute(sql,{':7':f_city,':8':farmer_id})

    sql = """update farmer set pincode=:9 where farmer_id=:10"""
    cur.execute(sql,{':9':p2,':10':farmer_id})

    conn.commit()
    cur.close()
    return render_template("farmer_page.html",succ=1)

@app.route('/address_update1',methods=["POST"])
def addr_update():
    global farmer_id

    b_doorno = request.form["b_doorno"]
    b_street = request.form["b_street"]
    b_locality = request.form["b_locality"]
    b_city = request.form["b_city"]
    b_pincode = request.form["b_pincode"]

    print(b_doorno,b_street,b_locality,b_city,b_pincode)

    p1 = int(b_doorno)
    p2 = int(b_pincode)

    print(p1,p2)
    print(type(p1),type(p2))

    print(type(b_doorno))
    print(type(b_street))
    print(type(b_locality))
    print(type(b_city))
    print(type(b_pincode))

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """update buyer set door_no=:1 where buyer_id=:2"""
    cur.execute(sql,{':1':p1,':2':buyer_id})

    sql = """update buyer set street=:3 where buyer_id=:4"""
    cur.execute(sql,{':3':b_street,':4':buyer_id})

    sql = """update buyer set locality=:5 where buyer_id=:6"""
    cur.execute(sql,{':5':b_locality,':6':buyer_id})

    sql = """update buyer set city=:7 where buyer_id=:8"""
    cur.execute(sql,{':7':b_city,':8':buyer_id})

    sql = """update buyer set pincode=:9 where buyer_id=:10"""
    cur.execute(sql,{':9':p2,':10':buyer_id})

    conn.commit()
    cur.close()
    return render_template("buyer_page.html",succ=1)

@app.route('/to_assign_cart')
def assign_cart():
    global buyer_id
    global cart_id

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """ insert into assign (buyer_id) values (:1)"""
    cur.execute(sql,[buyer_id])

    sql = """ select max(cart_id) from assign where buyer_id=:1 """
    cur.execute(sql,{'1':buyer_id})

    y = cur.fetchone()

    print(y[0])

    cart_id = int(y[0])

    conn.commit()
    cur.close()
    return render_template("products.html",succ=1)


@app.route('/to_products')
def to_products():
    return render_template("products.html")

@app.route('/to_check',methods=["POST"])
def to_Check():
    product_id = request.get_json(force=True)
    print(product_id)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """ select available_quantity from holds where product_id=:1 """
    cur.execute(sql,({'1':product_id['prod_id']}))

    y = cur.fetchone()

    print(y)

    conn.commit()
    cur.close()

    # key:value

    if y!=None:
        return {"status":True,'product_id':product_id['prod_id']}
    else:
        return {"status":False}

@app.route('/add_cart',methods=["POST"])
def add_Cart():
    global cart_id

    pro_id = request.form['p_id']
    r_quan = request.form["req_quan"]
    
    print(r_quan)
    print(pro_id)
    
    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """ select count(available_quantity) from holds where product_id=:1 and available_quantity>:2 """
    cur.execute(sql,{'1':pro_id,'2':r_quan})

    y = cur.fetchone()

    print(y[0])

    if int(y[0])==0:
        conn.commit()
        cur.close()
        return render_template("products.html",success=0)
    else:
        sql = """ select stock_id,available_quantity from holds where product_id=:1 and available_quantity>:2 """
        cur.execute(sql,{'1':pro_id,'2':r_quan})

        x = cur.fetchone()

        stock_id=x[0]

        print(stock_id)

        sql = """ select name from product where product_id=:1 """
        cur.execute(sql,{'1':pro_id})
        z = cur.fetchone()

        print(z[0])
        pro_name = z[0]

        sql = """ select price from product where product_id=:1 """
        cur.execute(sql,{'1':pro_id})
        w = cur.fetchone()

        print(w[0])

        t_price = float(w[0])*float(r_quan)
        

        sql = """ insert into cart (cart_id,buyer_id,product_id,name,stock_id,quantity,price) values (:1,:2,:3,:4,:5,:6,:7)"""
        cur.execute(sql,[cart_id,buyer_id,pro_id,pro_name,stock_id,r_quan,t_price])

        conn.commit()
        cur.close()

        return render_template("products.html",success=1)

@app.route('/payment',methods=["POST"])
def payment():
    global buyer_id
    global cart_id
    global total_price

    p_mode = request.form["p_mode"]
    print(p_mode)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    timestamp = 1528797322
    date_time = datetime.fromtimestamp(timestamp)

    print(date_time)

    d = date_time.strftime("%d-%b-%Y")

    print(d)

    sql = """ insert into payment (buyer_id,cart_id,total_amount,p_mode,payment_date) values (:1,:2,:3,:4,:5) """
    cur.execute(sql,[buyer_id,cart_id,total_price,p_mode,d])

    conn.commit()
    cur.close()

    return render_template("buyer_page.html",s=1)

@app.route('/to_delete',methods=["POST"])
def to_delete():
    global cart_id
    pro_name = request.get_json(force=True)
    print(pro_name)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """ delete from cart where cart_id=:1 and name=:2 """
    cur.execute(sql,{'1':cart_id,'2':pro_name['p_name']})

    conn.commit()
    cur.close()

    return {"status":True}

if __name__ == '__main__':
    app.run(debug=True)