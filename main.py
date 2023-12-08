from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '10.80.7.129'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'satdata'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        log_time = details['log']
        _ID = details['id']
        orbit = details['or']
        sendfrom = details['send']
        location = details['loc']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO messages(log_time, ID, orbit, sendfrom, location) VALUES ('%s','%s','%s','%s','%s')" %(log_time,_ID,orbit,sendfrom,location))
        mysql.connection.commit()
        cur.close()
        return 'successfully incert'
    return render_template('web1.html')


if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
