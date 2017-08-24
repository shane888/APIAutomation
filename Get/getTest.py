#/usr/bin/python
#encoding:utf-8

import requests
import unittest


class testClass(unittest.TestCase):
    def testGet(self):
        headers = {

        }


        cookies = dict(

        )

        res = requests.get(

        )

        print res.text
        print res.status_code

        self.assertTrue(u""in res.text)


if __name__ == 'main':
    unittest.main()