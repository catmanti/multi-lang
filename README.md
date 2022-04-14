# multi-lang
Multi language support website for English and Sinhala
go to: multi-lang/lib64/python3.10/site-packages/django/conf/locale
add folder: si
copy all the files in en folder to it
Now change __init__.py file
add:
```in  LANG_INFO = {
"si": {
    "bidi": False,
    "code": "ro",
    "name": "Sinhala",
    "name_local": "සිංහල",
     },
}
```
