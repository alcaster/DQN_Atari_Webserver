from flask import Flask, render_template, Response
from flask_jsglue import JSGlue

from cameras.camera_gym import CameraGymGame1

app = Flask(__name__)
jsglue = JSGlue(app)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/game1')
def game1():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(CameraGymGame1()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
