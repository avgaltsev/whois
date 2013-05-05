import os, subprocess, re, json
from bottle import get, post, request, run, default_app

@get("/whois/")
def getIndex():
   
   return "Hello"


@post("/whois/")
def postIndex():
    
    query = request.forms.get("query")
    
    try:
        output = subprocess.check_output(["whois", query])
    
    except Exception as e:
        output = e.output
    
    if output in [
        "No whois server is known for this kind of object.\n",
        "This TLD has no whois server.\n"
    ]:
        status = "wrong"
    
    else:
        status = "occupied"
    
    whois = output
    
    return json.dumps({
        "status": status,
        "whois": whois
    })
    
    #return json.dumps({
    #    "status": "free"
    #})


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
else:
    application = default_app()
