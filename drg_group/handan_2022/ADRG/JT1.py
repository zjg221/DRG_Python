from drg_group.handan_2022.Base import message,intersect,SS_VALID
from drg_group.handan_2022.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["S20.000","S20.101","S20.200","S20.200x003","S20.201","S20.202","S20.300x001","S20.301","S20.400x001","S20.700","S20.800x002","S20.801","S20.802","S20.803","S21.000","S30.000x001","S30.000x003","S30.000x004","S30.001","S30.002","S30.003","S30.100","S30.100x001","S30.100x002","S30.100x004","S30.100x007","S30.101","S30.104","S30.200x005","S30.200x006","S30.700","S30.800x001","S30.800x002","S30.800x003","S30.800x004","S30.801","S30.900x001","S30.900x002","S30.900x003","S31.001","S31.002","S39.910","S39.911","S40.000x001","S40.000x002","S40.000x003","S40.001","S40.700","S40.701","S40.800x011","S40.800x012","S40.800x021","S40.800x022","S40.800x031","S40.800x032","S40.800x041","S40.800x042","S40.900","S50.000","S50.101","S50.700","S50.701","S50.800x011","S50.800x021","S50.800x031","S50.800x041","S50.800x081","S50.900","S50.901","S60.000x001","S60.100x001","S60.201","S60.202","S60.700","S60.701","S60.800x011","S60.800x012","S60.800x021","S60.800x022","S60.800x023","S60.800x031","S60.800x032","S60.800x033","S60.800x041","S60.800x042","S60.800x043","S60.801","S60.900","S60.900x002","S60.901","S60.902","S70.000","S70.100","S70.700x001","S70.700x002","S70.800x011","S70.800x012","S70.800x021","S70.800x022","S70.800x031","S70.800x032","S70.800x041","S70.800x042","S70.900x001","S70.900x002","S70.900x003","S70.901","S80.000","S80.100x002","S80.101","S80.700","S80.800x011","S80.800x012","S80.800x013","S80.800x021","S80.800x022","S80.800x023","S80.800x031","S80.800x032","S80.800x033","S80.800x041","S80.800x042","S80.800x043","S80.900","S80.901","S90.000","S90.100","S90.200","S90.300x001","S90.300x002","S90.300x003","S90.301","S90.700","S90.800x011","S90.800x012","S90.800x013","S90.800x021","S90.800x022","S90.800x023","S90.800x031","S90.800x032","S90.800x033","S90.800x041","S90.800x042","S90.800x043","S90.900x002","S90.900x003","S90.901","T00.000x001","T00.100x001","T00.200x001","T00.300x001","T00.600x001","T00.800x001","T00.900","T00.900x002","T00.900x003","T00.900x004","T00.900x005","T00.900x006","T00.900x007","T00.901","T00.902","T01.301","T01.800x001","T09.000","T09.000x011","T09.000x021","T09.000x031","T09.000x041","T09.000x051","T11.000","T11.000x021","T11.000x031","T11.000x041","T11.000x051","T11.001","T11.101","T13.000","T13.000x011","T13.000x021","T13.000x031","T13.000x041","T13.000x051","T14.000","T14.000x003","T14.000x011","T14.000x021","T14.000x031","T14.000x041","T14.001","T14.002","T14.003","T14.101","T79.700","Z41.105"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合JT1入组条件，匹配规则：主诊断匹配')
    
    if MDCJ_DRG.JT19_group(record):
      return 'JT19'

    return ''
  else:
    return ''
