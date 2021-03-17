# Read only

def read_only():
    ''' a method that only reads the file '''
    try:
        file1 = open('data.txt')
        text = file1.read()
        print(text)
        file1.close()
    except FileNotFoundError:
        text = None
        print(text)

def write_only():
    ''' a method that writes to a file '''
    file2 = open('more_data.txt', 'w')
    file2.write('tomatoes')
    file2.close()

# Python will know to close this file (even if there are errors)
with open('data.txt') as f:
    txt = f.read()
    print(txt)

# def read_food_sales():
#     all_dates = []
#     all_regions = []
#     all_cities = []
#     with open('sampledatafoodsales.csv') as f:
#         data = f.readlines()

#         for food_sale in data:
#             split_food_sale = food_sale.split(',')

#             order_date = split_food_sale[0]
#             print(order_date)
#             # append order_date to all-dates list
#             all_dates.append(order_date)
    # print(all_dates)

#     for regions in data:
#         split_food_sale = food_sale.split(',')
#         region = split_food_sale[0]
#         print(region)

#         all_regions.append(region)
#     print(all_regions)
        

#     with open('dates.txt', 'w') as f:
#         for date in all_dates:
#                 f.write(date)
#                 f.write('\n')

# def append_text():
#     ''' Append data to an existing file '''
#     with open('dates.dates.txt', 'a') as f:
#         f.write('3/17/2021')
#         print('done')
    


# if __name__ == '__main__':
#     # read_only()
#     write_only()
#     read_food_sales()

def read_food_sales():
    all_regions = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()

        for food_sale in data:
            split_food_sale = food_sale.split(',')

            region = split_food_sale[0]
            print(region)
            # append order_date to all-dates list
            all_regions.append(region)
    print(all_regions)

if __name__ == '__main__':
    # read_only()
    write_only()
    read_food_sales()