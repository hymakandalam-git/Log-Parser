import pandas as pd
import pprint

log_file = open("serverlogs.txt","r")
ip_address_lst = []
success_lst = []
failed_lst = []
for log in log_file:
    lst = log.split()
    """print(lst)"""
    ip_address_lst.append(lst[0])
    
    success_lst.append(int(lst[-3]))

    failed_lst.append(int(lst[-1]))

total_success = sum(success_lst)
total_failed = sum(failed_lst)

ip_address_lst.append('Total')
success_lst.append(total_success)
failed_lst.append(total_failed)
    
df = pd.DataFrame(columns = ["IP Address","Success","Failed"])
df['IP Address'] = ip_address_lst
df['Success'] = success_lst
df['Failed'] = failed_lst

df.to_csv("output.csv", index = False)

pprint.pprint(df)



"""
    dict = { 'IP Address': ip_address, 'Success': num_lst, 'Failed': fnum_lst}

    df = pd.DataFrame(dict)

    print(df)

"""
