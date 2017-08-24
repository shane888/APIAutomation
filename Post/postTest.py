#/usr/bin/python
#encoding:utf-8

import requests
import unittest


class testClass(unittest.TestCase):
    def testPost(self):
        keyword = {
          #request body 中的内容
        }

        headers = {

        }
        cookies = dict(

        )

        res = requests.post(

        )

        print res.text
        print res.status_code

        self.assertTrue(u""in res.text)


if __name__ == 'main':
    unittest.main()