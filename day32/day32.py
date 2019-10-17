db.student.insert({
    name:'Dekie',
    age:22,
    score:[60,70,70]
})
db.student.insert({
    name:'Michile',
    age:23,
    score:[85,70,90,95]
})
db.student.insert({
    name:'David',
    age:24,
    score:[90,95,92]
})


db.orders.insert([{
    order_id:2,
    cust_name:'lisi',
    order_date:ISODate(),
    status:2,
    order_detail:{
        product_id:2,
        product_name:'ipad',
        amt:1,
        price:8000
    }},
    {
    order_id:3,
    cust_name:'wangwu',
    order_date:ISODate(),
    status:2,
    order_detail:[{
        product_id:1,
        product_name:'iphone',
        amt:1,
        price:6000
    },
    {   product_id:2,
        product_name:'ipad',
        amt:1,
        price:8000

    }]},
    {
    order_id:4,
    cust_name:'zhaoliu',
    order_date:ISODate(),
    status:2,
    order_detail:{
        product_id:1,
        product_name:'iphone',
        amt:1,
        price:6000
    }}
])


db.orders.find({status:1}).pretty()
db.orders.find({status:{$ne:1}}).pretty()
db.orders.find({$and:[{status:1},{cust_name:'zhangsan'}]}).pretty()
db.orders.find({status:1,cust_name:'zhangsan'}).pretty() 
db.orders.find({},{_id:0}).pretty()
db.orders.find({status:{$in:[1,3,4]}}).pretty()
db.orders.find({$or:[{status:1},{status:3},{status:4}]}).pretty()
db.orders.find({order_detail:{$size:2}}).pretty()

db.acct.find().sort({acct_type:1},{balance:-1})








































