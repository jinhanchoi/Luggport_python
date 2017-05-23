from flask import Flask, render_template
from kafka import KafkaConsumer, KafkaClient

app = Flask(__name__)

@app.route('/')
def main():
     return render_template("main.html")

@app.route('/spots',methods=['GET'])
def spots():
    topics = list(consumer.topics())
    topics.remove("__consumer_offsets")
    print(topics)
    print(consumer)
    return render_template("spots.html",topics = topics)

@app.route('/create')
def createTopic():
    client = KafkaClient(hosts=['0.0.0.0:9092'])
    client.ensure_topic_exists('newnew_topic')
    return render_template("spots.html")
if __name__ == '__main__':
    consumer = KafkaConsumer(bootstrap_servers=['0.0.0.0:9092'])
    app.debug = True
    app.run(host='0.0.0.0', port=8088)

