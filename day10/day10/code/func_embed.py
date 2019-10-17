def fn_outer():
    print("fn_outer调用开始...")

    def fn_inner():
        print("fn_inner被调用")
    fn_inner()
    fn_inner()

    print("fn_outer调用结束!")

fn_outer()
