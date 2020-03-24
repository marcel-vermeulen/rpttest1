import os
import requests
import json
import pandas as pd
import pandas.io.json as json_normalize

basepath = os.path.abspath(os.path.dirname(__file__))
datapath = os.path.join(basepath,"data")

# VMware Security Advisories - https://www.vmware.com/security/advisories.html
esxi_rls_json = os.path.join(datapath,"esxiReleases.json")

print(esxi_rls_json)

def json2df(fname):
	#load json object
	with open(fname) as f:
		data = json.load(f)
	df_raw = pd.DataFrame(data['data']['esxiReleases'])
	print(df_raw.info())

	return df_raw

def esxi_clean(df):
	L = ['GA', 'U']
	pat = r'(\b{}\b)'.format('|'.join(L))
	df_new = df[df['friendlyName'].str.contains(pat, case=False, na=False)]

	print(df_new.info())

	return df_new

def get_esxireleases(esxi_rls_json):
	dfEsxi_raw = pd.DataFrame()
	dfEsxi_raw = json2df(esxi_rls_json)
	print(dfEsxi_raw.info())
	#'''
	dfEsxi_cln = pd.DataFrame()
	dfEsxi_cln = esxi_clean(dfEsxi_raw)
	print(dfEsxi_cln[['minorRelease','releaseLevel','releaseDate','build']])
	#'''

	return dfEsxi_cln