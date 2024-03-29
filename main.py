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

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from time import time, localtime , strftime

class MainPage(webapp.RequestHandler):
  def get(self):
    fecha = strftime("%d %b %Y %H:%M:%S", localtime())


    template_values = {
      'fecha' : fecha ,    
      }

    path = os.path.join(os.path.dirname(__file__), 'mapa.html')
    self.response.out.write(template.render(path, template_values))
    

def main():
  app = webapp.WSGIApplication([('/', MainPage)],debug=True)
  util.run_wsgi_app(app)


if __name__ == '__main__':
  main()
