def add_update_url_ip(url_ip,dict):
    dict.update(url_ip)

def delete_url(url,dict):
    if search_url(url,dict):
        del dict[url]
    else:
        print('url was not found')

def search_url(url,dict):
    if url in dict.keys():
        return True
    else:
        return False


def menu():
    selection = int(input('Enter your selection:\n1 - Add URL and IP Address\n2 - Delete URL\n3 - Update new IP to existing URL\n4 - Print all URLs and IP Addresses\n5 - search for URL\n'))
    while selection <1 or selection>5:
        selection = int(input('Enter your selection:\n1 - Add URL and IP Address\n2 - Delete URL\n3 - Update new IP to existing URL\n4 - Print all URLs and IP Addresses\n5 - search for URL\n'))
        continue
    return selection

#### Main Dev
dns = {'www.abc.com':'192.168.1.1','www.abd.com':'192.168.1.2','www.abe.com':'192.168.1.3','www.abf.com':'192.168.1.4','www.abg.com':'192.168.1.5',}

select = menu()

if select ==1:
    url = input('Enter the URL: ')
    ip = input('Enter the IP Address: ')
    url_ip= {url:ip}
    if search_url(url, dns):
        print('url already exists')
    else:
        add_update_url_ip(url_ip, dns)
    print('DNS: ', dns, '\nlength is ', str(len(dns)))

elif select == 2:
    url = input('Enter the URL: ')
    delete_url(url, dns)
    print('DNS: ', dns, '\nlength is ', str(len(dns)))

elif select == 3:
    url = input('Enter the URL: ')
    ip = input('Enter the new IP Address: ')
    url_ip = {url: ip}
    if search_url(url,dns):
        add_update_url_ip(url_ip, dns)
        print('DNS: ', dns, '\nlength is ', str(len(dns)))
    else:
        print('url was not found')

elif select == 4:
    print('DNS: ', dns, '\nlength is ',str(len(dns)))

elif select == 5:
    url = input('Enter the URL: ')
    bol = search_url(url,dns)
    print(str(bol))




