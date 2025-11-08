# import http.server
# import socketserver

# port= 80
# handler = http.server.SimpleHTTPRequestHandler

# my_web_server = socketserver.TCPServer(("",port),handler)
# print('start to listen to port 80')
# my_web_server.serve_forever()

import flask

app= flask.Flask('guests')


def get_html(page_name):
    html_file = open(page_name+'.html')
    content = html_file.read()
    html_file.close()
    return content

def get_guests():
    guestsdb=open("guestsdb.txt")
    content= guestsdb.read()
    guestsdb.close()
    guests= content.split("\n")
    return guests


@app.route("/")

def homepage():
    return get_html('index')

@app.route("/about")
def about():
    html_page=get_html('about')
    guests=get_guests()
    guests.sort()
    actual_values=""
    for guest in guests:
        if guest.strip():
            actual_values += "<p>"+ guest +"</p>"
    return html_page.replace("$$guests$$",actual_values) 


if __name__ == '__main__':
    app.run(debug=True, port=5500)