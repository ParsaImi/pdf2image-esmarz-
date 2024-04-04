from pymongo import MongoClient

def start():
    client = MongoClient('mongodb+srv://imicorp:BNCjJPAswlcwQP93@cluster0.mh1eamh.mongodb.net/')
    db = client['roads']['posts']
    all_roads = list(db.find({}))
     #conn = db[f'{name}']
    return all_roads
# how to use db
# makemyrx_db = client['sample_medicines']
# medicines_collection = makemyrx_db['medicinedetails']