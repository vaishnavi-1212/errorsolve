# #!/usr/bin/env python
# #
# # Copyright 2007 Google Inc.
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.
# #
# import webapp2

# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Hello world!')

# app = webapp2.WSGIApplication([
#     ('/', MainHandler)
# ], debug=True)

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Define your HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
        </body>
        </html>
        """

        # Set the response content type to HTML
        self.response.headers['Content-Type'] = 'text/html'

        # Write the HTML content to the response
        self.response.write(html_content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


# import webapp2

# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         # Define your HTML content
#         html_content = """
#         <!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>My Portfolio</title>
#         </head>
#         <body>
#             <header>
#                 <nav>
#                     <ul>
#                         <li><a href="#home">Home</a></li>
#                         <li><a href="#about">About</a></li>
#                         <li><a href="#projects">Projects</a></li>
#                     </ul>
#                 </nav>
#             </header>
#             <main>
#                 <section id="home">
#                     <h1>Welcome to My Portfolio</h1>
#                     <p>Hello! I'm [Your Name], a [Your Profession].</p>
#                 </section>
#                 <section id="about">
#                     <h2>About Me</h2>
#                     <p>This is the about section. Here you can write something about yourself.</p>
#                 </section>
#                 <section id="projects">
#                     <h2>My Projects</h2>
#                     <p>This is the projects section. Showcase your projects here.</p>
#                 </section>
#             </main>
#             <footer>
#                 <p>&copy; 2024 [Your Name]</p>
#             </footer>
#         </body>
#         </html>
#         """

#         # Set the response content type to HTML
#         self.response.headers['Content-Type'] = 'text/html'

#         # Write the HTML content to the response
#         self.response.write(html_content)

# app = webapp2.WSGIApplication([
#     ('/', MainHandler)
# ], debug=True)



