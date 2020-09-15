# function that takes in an list
def divisible_by_three(list):
    # loop through the list
    for each_value in list: # not == range(len(list))
        # perform logic (if) constraining the data %3 == 0
        if each_value %3 == 0:
            # console.log(data[i])
            # print 'each_value'
            print(each_value)

test_list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

# divisible_by_three(test_list)

def convert_array_of_strings_to_integers(list):
    for i in list:
        rtn_list = []
        my_list = i.split()
        print(my_list)
        for each_value in my_list:
            if each_value == "one":
                rtn_list.append("1")
            if each_value == "two" or each_value == "twenty":
                rtn_list.append("2")
            if each_value == "three" or each_value == "thirty":
                rtn_list.append("3")
            if each_value == "four" or each_value == "forty":
                rtn_list.append("4")
            if each_value == "five" or each_value == "fifty":
                rtn_list.append("5")
            if each_value == "six" or each_value == "sixty":
                rtn_list.append("6")
            if each_value == "seven" or each_value == "seventy":
                rtn_list.append("7")
            if each_value == "eight" or each_value == "eighty":
                rtn_list.append("8")
            if each_value == "nine" or each_value == "ninety":
                rtn_list.append("9")
            if each_value == "ten":
                rtn_list.append("10")
            if each_value == "eleven":
                rtn_list.append("11")
            if each_value == "twelve":
                rtn_list.append("12")
            if each_value == "thirteen":
                rtn_list.append("13")
            if each_value == "fourteen":
                rtn_list.append("14")
            if each_value == "fifteen":
                rtn_list.append("15")
            if each_value == "sixteen":
                rtn_list.append("16")
            if each_value == "seventeen":
                rtn_list.append("17")
            if each_value == "eighteen":
                rtn_list.append("18")
            if each_value == "nineteen":
                rtn_list.append("19")
            if each_value == "hundred":
                pass
        rtn_list = "".join(rtn_list)
        print(rtn_list)

# def convert_array_of_strings_to_integers(list, callback):
#     for i in list:
#         rtn_list = []
#         my_list = i.split()
#         # print(my_list)
#         for each_value in my_list:
#             if each_value == "one":
#                 rtn_list.append("1")
#             if each_value == "two" or each_value == "twenty":
#                 rtn_list.append("2")
#             if each_value == "three" or each_value == "thirty":
#                 rtn_list.append("3")
#             if each_value == "four" or each_value == "forty":
#                 rtn_list.append("4")
#             if each_value == "five" or each_value == "fifty":
#                 rtn_list.append("5")
#             if each_value == "six" or each_value == "sixty":
#                 rtn_list.append("6")
#             if each_value == "seven" or each_value == "seventy":
#                 rtn_list.append("7")
#             if each_value == "eight" or each_value == "eighty":
#                 rtn_list.append("8")
#             if each_value == "nine" or each_value == "ninety":
#                 rtn_list.append("9")
#             if each_value == "ten":
#                 rtn_list.append("10")
#             if each_value == "eleven":
#                 rtn_list.append("11")
#             if each_value == "twelve":
#                 rtn_list.append("12")
#             if each_value == "thirteen":
#                 rtn_list.append("13")
#             if each_value == "fourteen":
#                 rtn_list.append("14")
#             if each_value == "fifteen":
#                 rtn_list.append("15")
#             if each_value == "sixteen":
#                 rtn_list.append("16")
#             if each_value == "seventeen":
#                 rtn_list.append("17")
#             if each_value == "eighteen":
#                 rtn_list.append("18")
#             if each_value == "nineteen":
#                 rtn_list.append("19")
#             if each_value == "hundred":
#                 pass
#         for list_items in rtn_list:
#             rtn_list = "".join(list_items)
#             return callback(rtn_list)


        

test_list_two = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]

test_list_two = [int(i) for i in test_list_two]
print(test_list_two)

# print(test_list_two)

convert_array_of_strings_to_integers(test_list_two)