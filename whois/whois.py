import os, subprocess, re, json
from bottle import get, post, request, run, default_app

@get("/whois/")
def getIndex():
   
   return "Hello"


@post("/whois/")
def postIndex():
    
    match = re.match("[a-zA-Z0-9\-\.]+", request.forms.get("query"))
    
    query = match.group(0) if match else ""
    
    tld = query.split(".")[-1]
    
    try:
        output = subprocess.check_output(["whois", query])
    
    except Exception as e:
        output = e.output
    
    def com(output):
        return "free" if re.search("No match for", output) else "occupied"
    
    def org(output):
        return "free" if re.search("NOT FOUND", output) else "occupied"
    
    def ru(output):
        return "free" if re.search("No entries found for the selected source", output) else "occupied"
    
    def default(output):
        return "wrong"
    
    functions = {
        "com": com,
        "net": com,
        "org": org,
        "me": org,
        "ru": ru
    }
    
    status = functions.get(tld, default)(output)
    
    whois = output
    
    return json.dumps({
        "status": status,
        "whois": whois
    })


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
else:
    application = default_app()
