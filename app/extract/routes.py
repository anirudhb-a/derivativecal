from app.extract import bp 



@bp.route("/test",methods=["GET"])
def index():
  from app.extract.service import publisher_data
  data = publisher_data()
  print(data)
  
  return "extract data"