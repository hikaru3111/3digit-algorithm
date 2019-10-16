import itertools


#重複ありですべての順列を返す。引数：int、返り値list(int)
def simple_perm(int1):
    #全ての順列が、タプルとして入っているリスト
    list1 = []
    #返り値に使う。すべての順列が入っているリスト。
    list2 = []
    #permutations使うために、int1をリストに変換する。
    int1_list = []
    #操作しやすいために、intからstr型に変換する
    int1 = str(int1)
    #ループの中で一文字ずつのものを結合するために使う
    char = ""
    #int1を一文字ずつlistにいれる。
    for i in range(0,len(int1)):
        int1_list.append(int1[i:i+1])
    #int1_listを並び替えてできる全ての順列をlist1に追加する
    for i in itertools.permutations(int1_list):
        list1.append(i)
    #list1の中の要素がタプルなので、文字列に変換し、さらにintに変換する
    for item in list1:
        char = ""
        for c in item:
            char += c
        #charをintに型を変えて、list2に追加する。
        list2.append(int(char))
        
    return list2

#重複なしですべての順列を返す。
def unique_perm(int1):
    #重複あり順列のリストをとりあえず入れるリスト
    list1 = []
    #重複なしにして入れるリスト
    list2 = []
    list1 = simple_perm(int1)
    #重複を消す
    list2 = list(set(list1))
    return list2



if __name__ == "__main__":
    first=123456
    #second=112233445566
    second=112233
    print_list = []
    #初めのは、重複あり順列でよい
    print_list = simple_perm(first)
    print("順列の個数(重複あり)：{0}".format(len(print_list)))
    print(print_list)
    #二つ目のは重複なし順列で
    print_list = []
    print_list = unique_perm(second)
    print("順列の個数（重複なし）：{0}".format(len(print_list)))
    print(print_list)