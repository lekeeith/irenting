

from flask_session import Session
from flask_wtf import CSRFProtect

import redis






app = create_app(1)


redis_store = redis.StrictRedis()

#
Session(app)

CSRFProtect(app)


@app.route("/index")
def index():
    return "index page"


if __name__ == "__main__":
    app.run
