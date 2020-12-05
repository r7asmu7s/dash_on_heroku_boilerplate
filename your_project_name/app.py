# imports
import dash

# create the app
app = dash.Dash()

# set server here to work along with gunicorn
server = app.server

# run server
if __name__ == '__main__':
    app.run_server()