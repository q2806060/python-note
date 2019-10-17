db.acct.insert({
    acct_no:'622345000001',
    acct_name:'Jerry',
    balance:5000.00
})

db.acct.find().pretty()

db.acct.insert({
    acct_no:'622345000002',
    acct_name:'Tom',
    acct_type:1,
    balance:123456.78
})

db.acct.insert([
    {
        acct_no:'622345000003',
        acct_name:'Mario',
        acct_type:1,
        balance:123456.78
    },
    {
        acct_no:'622345000004',
        acct_name:'Cookie',
        acct_type:1,
        balance:134446.78
    }
])

db.acct.save({
    acct_no:'622345000005',
    acct_name:'Emma',
    acct_type:2,
    balance:10000
})




















