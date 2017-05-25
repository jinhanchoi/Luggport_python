from flask import Flask, render_template, request
from kafka import KafkaConsumer, KafkaClient
import mongoAccess

app = Flask(__name__)

@app.route('/')
def main():
     return render_template("main.html")

@app.route('/spots',methods=['GET'])
def spots():
    topics = list(consumer.topics())
    #topics.remove("__consumer_offsets")
    print(topics)
    print(consumer)
    spots = dao.db['spot']
    for tspot in spots.find():
        print(tspot)
    return render_template("spots.html",spots = spots.find())

@app.route('/create',methods=['POST'])
def createTopic():
    
    name = request.form.get('name')
    location = request.form.get('location')
    # client = KafkaClient(hosts=['0.0.0.0:9092'])
    client.ensure_topic_exists(name)
   
    spot = dao.db['spot']
    if spot.find_one({'name' : name}) is None:
        spot.insert({'name':name,'location':location})
    return render_template("spots.html")
@app.route('/deleteTopic')
def delTopics():
    
    return render_template("spots.html")

@app.route('/mongo')
def testMongo():
    spot = dao.db['spot']
    spot.insert({'_id':'first','name':'testname'})
    return render_template("spots.html")

@app.route('/mongoread')
def testMongoRead():
    spot = dao.db['spot']
    for tspot in spot.find():
        print(tspot)
    return render_template("spots.html")



if __name__ == '__main__':
    consumer = KafkaConsumer(bootstrap_servers=['0.0.0.0:9092'])
    client = KafkaClient(hosts=['0.0.0.0:9092'])
    dao = mongoAccess.MongoAccessObject({'host':'localhost','name':'spots'})
    app.debug = True
    app.run(host='0.0.0.0', port=8088)

