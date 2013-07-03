# find the largest image counter
ls |grep image |sort |tail -1 |grep -o -E "[0-9]+"
