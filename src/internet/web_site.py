def web_page(pin):

    html = """
    <html><head> 
        <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,"> 
        <style>
            html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
            h1{color: #0F3376; padding: 2vh;}
            p{font-size: 1.5rem;}
            .button{display: inline-block; background-color: #e7bd3b; border: none; 
                border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
            .button2{background-color: #4286f4;}
        </style></head>
    <body> 
        <h1>ESP Web Server</h1> 
        <p>Pin <strong>""" + pin + """</strong> is active</p>
        <p><a href="/?led=1"><button class="button">LED 1</button></a></p>
        <p><a href="/?led=2"><button class="button">LED 2</button></a></p>
        <p><a href="/?led=3"><button class="button">LED 3</button></a></p>
        <p><a href="/?led=4"><button class="button">LED 4</button></a></p>
    </body>
    </html>"""
    return html
