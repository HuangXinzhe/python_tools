# ===================================1、位置参数===================================
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int)  # 位置参数，可以定义参数类型
# args = parser.parse_args()
# print(args.square ** 2)  # python argparse_tutorial.py 位置参数/-h  (-h/--help为帮助信息)


# ===================================2、可选参数===================================
# import argparse
#
# parser = argparse.ArgumentParser()
# # parser.add_argument("--verbosity", help="increase output verbosity")  # python argparse_tutorial.py --verbosity 1  （可选参数给出显示信息）
# # args = parser.parse_args()
# # if args.verbosity:
# #     print("verbosity turned on")
#
# parser.add_argument("--verbose", help="increase output verbosity", action="store_true")  # 可选参数  python argparse_tutorial.py --verbose  给出可选参数既有输出（仅有true/false）
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")



# ===================================3、位置参数与可选参数结合===================================
