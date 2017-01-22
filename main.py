#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    fortunes = [
    "Good stuff.",
    "Medium stuff.",
    "Bad stuff."
    ]

    index = random.randint(0, len(fortunes)-1)

    return fortunes[index]


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Diet Fortune Cookie</h1><h2>All of the fortunes, none of the calories</h2>"

        fortune = getRandomFortune()
        fortune_sentence = 'Your fortune: <strong>' + fortune + '</strong>'
        fortune_paragraph = '<p>' + fortune_sentence + '</p>'

        lucky_number = random.randint(1,100)
        number_sentence = 'Your lucky number is: <strong>' + str(lucky_number) + '</strong>'
        number_paragraph = '<p>' + number_sentence + '</p>'

        cookie_again_button = "<a href='.'><button>Thank you, I'll have another.</button></a>"

        content = header + fortune_paragraph + number_paragraph + cookie_again_button

        self.response.write(content)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
