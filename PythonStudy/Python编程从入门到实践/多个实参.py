# 8-12
def sanmingzi(*args):
    mes = []
    for message in args:
        mes.append(message)
    print("您目前的材料有{}".format(mes))


sanmingzi("辣椒","奶油")
sanmingzi("wobu","nie","wobuzhidao")

# 8-13
def qiche(**kwargs):
    for key,value in kwargs.items():
        kwargs[key] = value
    print(kwargs)
    pass


qiche(dazong= "zm-220",meidi = "ls-990")





