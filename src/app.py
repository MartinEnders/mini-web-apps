from flask import Flask
app = Flask(__name__)

from datetime import date, timedelta

html_template = """<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"
  \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">

<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"de\" lang=\"de\">
  <head>
    <title>{}</title>
    <meta http-equiv=\"Content-type\" content=\"text/html; charset=utf-8\" />

    <style type='text/css'>
        /* <![CDATA[ */
          html {{height: 100%;}}
          body {{height: 90%;}}
          table {{width: 100%; height: 100%;}}
        /* ]]> */
    </style>
  </head>
  <body>
     <table >
        <tr><td valign='middle' align='center'><div>{}</div></td></tr>
     </table>
<div>
<small>Impressum: V.i.S.d.P. für diese Seite und ihren Inhalt:
Dr. Martin Enders, 
Am Letten 25a, 
96317 Kronach, 
martin@martin-enders.de, 
Tel: 0049 157 321 458 72 
</small>
</div>

  </body>
</html>
"""

sm_zusammen = date(2011, 6, 12)
sm_verheirated = date(2019, 4, 25)
sm_jenaer_str = date(2012, 3, 17)
sm_linnea = date(2020, 6, 4)

gc_verheirated = date(2015, 12, 23)

def get_heute():
    return date.today()

def sm_zusammen_seit():
    tage = get_heute() - sm_zusammen
    return "Sophia und Martin sind seit {} Tagen zusammen.".format(tage.days)

def sm_verheiratet_seit():
    tage = get_heute() - sm_verheirated
    return "Sophia und Martin sind seit {} Tagen verheiratet.".format(tage.days)

def gc_verheiratet_seit():
    tage = get_heute() - gc_verheirated
    return "Conny und Georg sind seit {} Tagen verheiratet.".format(tage.days)

def sm_linnea_seit():
    tage = get_heute() - sm_linnea
    return "Linnea ist {} Tage ({} Wochen) alt.".format(tage.days, int(tage.days/7))

def sm_jenaer_str_seit():
    tage = get_heute() - sm_jenaer_str
    return "Sophia und Martin wohnen seit {} Tagen zusammen in der Jenaer Str. in Erlangen.".format(tage.days)

@app.route('/sm')
def sm():
    facts = [sm_zusammen_seit(), sm_jenaer_str_seit(), sm_verheiratet_seit(), sm_linnea_seit()]
    html_facts = "\n".join(["<div>"+f+"</div>" for f in facts])
    return html_template.format("Sophia und Martin Facts", html_facts)

@app.route('/ggco')
def gc():
    facts = [gc_verheiratet_seit()]
    html_facts = "\n".join(["<div>"+f+"</div>" for f in facts])
    return html_template.format("GGCO Facts", html_facts)    

@app.route('/')
def main():
    return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>mini-web-apps.di2.io</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
  </head>
  <body>
    <ul>
     <li><a href='/sm'>Sophia & Martin</a></li>
     <li><a href='https://ggco.de'>GGCO</a></li>
    </ul>
  </body>
</html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=False)
