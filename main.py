from flask import Flask, jsonify, request
import csv

from requests import post

allMovies = []

with open("data.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1 :]

likedMovies = []
notLikedMovies = []
moviesNotSeen = []

app = Flask(__name__)

@app.route("/getMovie")
def getMovie() :
    return jsonify({
        "data" : allMovies[0],
        "status" : "Succes"
    })

@app.route("/likedMovie", methods = ["POST"])
def likedMovie() :
    movie = allMovies[0]
    alMovies = allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        "status" : "Succes"
    }), 201

@app.route("/unLikedMovie", methods = ["POST"])
def unLikedMovie() :
    movie = allMovies[0]
    alMovies = allMovies[1:]
    notLikedMovies.append(movie)
    return jsonify({
        "status" : "Succes"
    }), 201

@app.route("/notWatchedMovie", methods = ["POST"])
def notWatchedMovie() :
    movie = allMovies[0]
    alMovies = allMovies[1:]
    moviesNotSeen.append(movie)
    return jsonify({
        "status" : "Succes"
    }), 201


if(__name__) == "__main__" :
    app.run()