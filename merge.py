import csv

with open("data.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]
    headers = data[0]
    
headers.append("poster_link")

with open("final.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    
with open("links.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovieLinks = data[1:]

for movieItem in allMovies :
    posterFound = any(movieItem[8]in movieLinkItems for movieLinkItems in allMovieLinks)
    if posterFound :
        for movieLinkItem in allMovieLinks :
            if movieItem[8] == movieLinkItem[0]:
                movieItem.append(movieLinkItem[1])
                if len(movieItem) == 28:
                    with open("final.csv", "a+") as f:
                        csv_writer = csv.writer(f)
                        csv_writer.writerow(movieItem)
            