def web_page(line):
    head = """
    <head> 
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
    """

    html = '<html>' + head + '<body><h1>3 Chanel Audio Switch</h1>'
    if line == "0":
        p1 = '<p>Switch is <strong> OFF </strong></p>'
    else:
        p1 = '<p>Line <strong> {} </strong> is active</p>'.format(line)

    if line == "1":
        button1 = '<p><a href="/?line=1"><button class="button button2">Line 1</button></a></p>'
    else:
        button1 = '<p><a href="/?line=1"><button class="button">Line 1</button></a></p>'

    if line == "2":
        button2 = '<p><a href="/?line=2"><button class="button button2">Line 2</button></a></p>'
    else:
        button2 = '<p><a href="/?line=2"><button class="button">Line 2</button></a></p>'

    if line == "3":
        button3 = '<p><a href="/?line=3"><button class="button button2">Line 3</button></a></p>'
    else:
        button3 = '<p><a href="/?line=3"><button class="button">Line 3</button></a></p>'

    if line == "0":
        button4 = '<p><a href="/?line=4"><button class="button button2">OFF</button></a></p>'
    else:
        button4 = '<p><a href="/?line=4"><button class="button">OFF</button></a></p>'

    return html + p1 + button1 + button2 + button3 + button4 + """
    </body>
    </html>"""
