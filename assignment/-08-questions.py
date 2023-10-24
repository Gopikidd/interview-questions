# # # li = list(map(str, input('enter the string').split()))
# # # print(li)
# #
# #
# # def fact():
# #     number = input("Enter the number : ")
# #     print(type(number))
# #     if '1' <= number <= '100':
# #         num = int(number)
# #         print(type(num))
# #
# #         if type(num) == int:
# #             fact = 1
# #             for i in range(1, num + 1):
# #                 fact = fact * i
# #
# #             print(f"factorial of {num} is {fact}")
# #         else:
# #             print("--Please Enter Digit only--")
# #
# #
# #     else:
# #         print('enter integer')
# #
# #
# #
# # fact()
#
# if number.isdigit():
#     number = int(number)
#     fact = 1
#     for i in range(1, number + 1):
#         fact = fact * i
#
#     print(f"factorial of {number} is {fact}")
# else:
#     print("--Please Enter Digit only--")

lis = list(map(str, input('enter the value =').split(' ')))

print('list = ', lis)
