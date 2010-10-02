from distutils.core import setup, Extension
import os.path

kw = {
	'name':"AES-256 cryptographic library for Python",
	'version':"0.1",
	'description':"AES-256 cryptographic library for Python.",
	'ext_modules':[
		Extension('aes256', sources = [os.path.join('src', 'aes256.c')])
	]
}

setup(**kw)