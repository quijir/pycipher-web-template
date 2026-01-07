from js import document, window, navigator
from pyodide.ffi import create_proxy
import math

def encode(text,key,chars):
  return "nothing"
def decode(text,key,chars):
  return "no decode function"
# replace these with ur own and name it encode/decode ^^

def copy_encode(event):
    text = document.getElementById("encode").innerText
    navigator.clipboard.writeText(text)
def copy_decode(event):
    text = document.getElementById("decode").innerText
    navigator.clipboard.writeText(text)
document.getElementById("copy-encode").onclick = copy_encode
document.getElementById("copy-decode").onclick = copy_decode

def collect_encode(event=None):
    form = document.getElementById("formencode")
    if not form:
        return
    data = {el.name: el.value for el in form.elements if el.name}
    out = encode(
        data.get("input", ""),
        data.get("key", ""),
        data.get("charset", "abcdefghijklmnopqrstuvwxyz")
    )
    document.querySelector("#encode").innerHTML = out if out else "no input"
def collect_decode(event=None):
    form = document.getElementById("formdecode")
    if not form:
        return
    data = {el.name: el.value for el in form.elements if el.name}
    out = decode(
        data.get("input", ""),
        data.get("key", ""),
        data.get("charset", "abcdefghijklmnopqrstuvwxyz")
    )
    document.querySelector("#decode").innerHTML = out if out else "no input"

def attach_listeners():
    encode_form = document.getElementById("formencode")
    decode_form = document.getElementById("formdecode")

    if encode_form is None or decode_form is None:
        window.setTimeout(attach_listeners, 100)
        return

    global encode_proxy, decode_proxy
    encode_proxy = create_proxy(collect_encode)
    decode_proxy = create_proxy(collect_decode)
    encode_form.addEventListener("input", encode_proxy)
    decode_form.addEventListener("input", decode_proxy)
    collect_encode()
    collect_decode()

attach_listeners()



