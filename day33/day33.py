
db.orders.find()

db.orders.update({},{$set:{order_date:ISODate()}},false,true)

db.orders.find({order_date:{$gt:ISODate('2018-12-13T06:35:54')}})

db.orders.find().count()

db.orders.find().sort({order_date:-1})

db.orders.update({},{$set:{payment_status:''}},false,true)

db.orders.find({'order_detail.product_id':'1'})

db.orders.







































