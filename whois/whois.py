import subprocess, re, json, datetime

from bottle import post, request, run, default_app

import tlds


def log(function):
    
    def decorator(*args, **kwargs):
        
        status = function(*args, **kwargs)
        
        file = open("whois.log", "a")
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + status + " " + args[0] + "\n")
        file.close
        
        return status
    
    return decorator


@post("/whois/")
def postIndex():
    
    match = re.match("[a-zA-Z0-9\-\.]+", request.forms.get("query"))
    
    domain = match.group(0).lower() if match else ""
    
    try:
        whois = subprocess.check_output(["whois", domain])
    
    except Exception as e:
        whois = e.output
    
    return json.dumps({
        "status": log(tlds.recognize)(domain, whois),
        "whois": whois
    })


if __name__ == "__main__":
    run(host="0.0.0.0", port=8080)

else:
    application = default_app()
