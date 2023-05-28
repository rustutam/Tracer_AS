import sys
from sys import argv
from re import findall
from subprocess import check_output
from json import loads
from urllib import request

LEN_IP = 20
LEN_COUNTRY = 20
LEN_AS = 10
LEN_DIF = 60


def main():
    DN = argv[1]
    try:
        res = check_output('tracert -4 -d -h 40 ' + DN,
                                      shell=True).decode('cp866')
    except:
        print("Incorrect domain")
        sys.exit(1)
    ip_list = findall('\d+.\d+.\d+.\d+', res)
    ip_list.pop(0)
    i = 1
    print("-" * LEN_DIF)
    for ip in ip_list:
        info = get_ip_inf(ip)
        if 'bogon' in info:
            print(str(i) + '\t' + correct_output(info['ip'], LEN_IP) + '\t' +
                  correct_output("-", LEN_AS))
        else:
            try:
                print(str(i) + '\t' + correct_output(str(info['ip']),
                                                     LEN_IP) + '\t'
                      + correct_output(str(info['country']).split(" ")[0] + "/"
                                       + info['city'],
                                       LEN_COUNTRY) +
                      '\t' + correct_output(str(info['org']).split()[0],
                                            LEN_AS) +
                      '\t' + ' '.join((info['org'].split()[1::])))
            except:
                continue
        i += 1
    print("-" * LEN_DIF)


def get_ip_inf(ip):
    return loads(request.urlopen('https://ipinfo.io/' + ip + '/json').read())


def correct_output(a, out_len):
    res = a
    for i in range(out_len - len(a)):
        res += " "
    return res


if __name__ == '__main__':
    main()
