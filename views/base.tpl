% setdefault("current_user", None)
<!doctype html>
<html>
    <head>
        <link href="/static/styles/main.css" rel="stylesheet"> 
    </head>
    <body>
        <div class="wrapper">
            <header>
                <h3>Crypto Tracker {{ f" - Portfolio for {current_user}" if current_user else "" }}</h3>
            </header>
            
            <main>
                {{!base}}
            </main>
            <footer>
                % include("footer.tpl")
            </footer>
        </div>
         
    </body>
</html>