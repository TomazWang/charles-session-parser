import json
import sys


def parse_chlsj(filename, data):
    host = data['host']
    path = data['path']
    client_address = data['clientAddress']
    method = data['method']
    request = data['request']
    response = data['response']

    out_file = open(filename, 'w')

    line_sum = '# ' + method + ' ' + host + path
    out_file.write(line_sum)
    out_file.write('\n\n')

    # Request
    out_file.write('+ Request')
    out_file.write('\n\n')

    # request header
    out_file.write('\t' + '> Headers' + '\n')

    for header in request['header']['headers']:
        out_file.write('\t\t')
        out_file.write(header['name'])
        out_file.write(': ')
        out_file.write(header['value'])
        out_file.write('\n')

    out_file.write('\n\n\n')

    # request body
    out_file.write('\t' + '> Body' + '\n')
    body_content_json = request['body']['text']
    parsed_body_json = json.loads(body_content_json)
    parsed_body_str = json.dumps(parsed_body_json, indent=4, sort_keys=True)
    for line in parsed_body_str.split('\n'):
        out_file.write('\t\t')
        out_file.write(line)
        out_file.write('\n')
    out_file.write('\n\n\n')

    out_file.write('===========================================================================')
    out_file.write('\n\n\n')

    # Response
    response_code = response['status']
    out_file.write('+ Response (' + str(response_code) + ')')
    out_file.write('\n\n')

    # response header
    out_file.write('\t' + '> Headers' + '\n')

    for header in response['header']['headers']:
        out_file.write('\t\t')
        out_file.write(header['name'])
        out_file.write(': ')
        out_file.write(header['value'])
        out_file.write('\n')

    out_file.write('\n\n\n')

    # response body
    out_file.write('\t' + '> Body' + '\n')
    body_content_json = response['body']['text']
    parsed_body_json = json.loads(body_content_json)
    parsed_body_str = json.dumps(parsed_body_json, indent=4, sort_keys=True)
    for line in parsed_body_str.split('\n'):
        out_file.write('\t\t')
        out_file.write(line)
        out_file.write('\n')
    out_file.write('\n\n\n\n')

    out_file.close()
    print('file output: '+filename)


def main(args):
    in_file_name = args[0]
    out_file_name = in_file_name.split('.')[0] + '_parse.txt'
    if len(args) > 2:
        out_file_name = args[1] + '.txt'

    if in_file_name.endswith('.chlsj'):
        with open(in_file_name) as in_file:
            datas = json.load(in_file)
            if len(datas) > 1:
                i = 1
                for data in datas:
                    out_file_name_with_no = out_file_name.replace('.txt', '_' + str(i) + '.txt')
                    parse_chlsj(out_file_name_with_no, data)
                    i = i + 1
            else:
                parse_chlsj(out_file_name, datas[0])

        print('Process complete!')

    else:
        print('Unrecognized file type.')


if __name__ == '__main__':
    main(sys.argv[1:])
