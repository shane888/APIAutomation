#usr/bin/python
#encoding:utf-8

import  requests
import  unittest
import ddt

@ddt
class testClass(unittest.TestCase):
    @ddt.date('uiii','hhjjj')
    def testGet(self,device_id):
        #配置headers
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Host':'blog.devtang.com',
            'Connection':'Keep-Alive',
            'Accept-Encoding':'gzip, deflate'

        }

        cookies = dict(
            beacon_id = '',
            search_id = '',

        )

        res = requests.get(
            'http://blog.devtang.com/images/charles-pro-3.png'+ device_id,
            headers = headers,
            cookie = cookies
        )

        print res.text
        print res.status_code

        self.assertTrue(u'' in res.text)

if __name__ == '__main__':
    unittest.main