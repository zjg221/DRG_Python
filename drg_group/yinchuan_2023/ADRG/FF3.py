from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["D18.000x001","D18.000x836","D18.010","D44.601","I15.200x001","I20.000","I21.001","I21.300x004","I25.500","I47.102","I50.002","I50.907","I70.204","I72.000x032","I72.100x003","I72.100x004","I72.101","I72.400x520","I72.404","I72.811","I73.803","I74.301","I74.302","I77.013","I80.207","I80.302","I80.303","I83.100x001","I83.200x001","I83.900x004","I83.903","I87.115","I87.116","I87.201","I87.202","I97.804","M31.804","Q21.101","Q22.100","R57.000","R57.200","R96.000x001","S45.101","S45.200x002","S55.000x001","S55.100x001","S55.101","S55.200x001","S65.000x002","S65.100x001","S65.100x002","S65.200","S65.500","S65.501","S65.700x001","S75.000","S85.000","S85.100x002","S85.101","S85.300x001","S85.700x001","S95.000","T11.400","T82.800x003","T82.800x005"]
  adrg_zd1=[]
  adrg_ss=["38.0300x005","38.0302","38.0800x002","38.0800x003","38.0801","38.0802","38.0900x001","38.1800x001","38.3000","38.3000x001","38.3301","38.4000","38.4300x001","38.4801","38.6000x011","38.6000x012","38.6000x013","38.6301","38.6302","38.6601","38.6802","38.6901","38.8801","38.8901","38.9300x702","38.9502","38.9800x001","38.9900x002","38.9900x501","38.9900x701","38.9900x901","39.2900x005","39.3100","39.3100x004","39.3100x007","39.3100x010","39.3100x017","39.3100x018","39.3101","39.3102","39.3105","39.3112","39.3113","39.3200","39.3200x010","39.3202","39.3206","39.4900x004","39.5300x015","39.5900x001","39.5900x019","39.5900x021","39.5900x024","39.7900x801","39.8901"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FF3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FF31_group(record):
      return 'FF31'

    if MDCF_DRG.FF33_group(record):
      return 'FF33'

    if MDCF_DRG.FF35_group(record):
      return 'FF35'

    return 'FF3'
  else:
    return ''
