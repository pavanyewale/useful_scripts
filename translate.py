import requests

def translate(sentence,sentence_language,languages):
    translated={}
    for l in languages:
        url = "https://www.google.com/async/translate?yv=3"

        payload="async=translate,sl:{},tl:{},st:{},id:1612512408371,qc:true,ac:false,_id:tw-async-translate,_pms:s,_fmt:pc".format(sentence_language,l,sentence)
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        match='<span id="tw-answ-target-text">'
        res=response.text
        i=res.find(match)
        i=i+len(match)
        res=res[i:]
        i=res.find("</span>")
        res=res[:i]
        translated.update({l:res})
    return translated

print(translate("I m so stupid",'en',['mr','gu','hi','ta','pa','ka','en']))
